from __future__ import annotations

from dataclasses import dataclass, field
from hashlib import sha256
import json
import os
import re
import tempfile
import unicodedata
import uuid

TRIGGER_PHRASES = (
    "preserve",
    "save",
    "archive",
    "remember this",
    "capture le delta",
    "capture the delta",
)


def _fold(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    value = value.casefold().strip()
    return re.sub(r"\s+", " ", value)


def is_preserve_command(text: str) -> bool:
    folded = _fold(text)
    return folded.startswith("preserve") or folded.startswith("save") or folded.startswith("archive") or folded.startswith("remember this") or folded.startswith("capture le delta") or folded.startswith("capture the delta")


def parse_preserve_request(text: str) -> dict[str, object]:
    if not is_preserve_command(text):
        raise ValueError("not a Preserve/Save request")
    folded = _fold(text)
    checkpoint = any(token in folded for token in ("checkpoint", "handoff", "transfer pack", "point de reprise"))
    if checkpoint:
        scope = "checkpoint"
    elif "decision" in folded:
        scope = "decision"
    elif "session" in folded or "tout ce qui est nouveau" in folded:
        scope = "session"
    else:
        scope = "current_delta"
    return {"requested_scope": scope, "checkpoint": checkpoint}


def fingerprint(text: str) -> str:
    return sha256(_fold(text).encode("utf-8")).hexdigest()


@dataclass(frozen=True)
class Candidate:
    candidate_id: str
    content: str
    topic: str
    marker: str | None = None
    target_path: str | None = None
    proposed_path: str | None = None
    relation: str = "additive"
    supersedes: str | None = None
    provenance: str | None = None

    @property
    def fingerprint(self) -> str:
        return fingerprint(self.content)


@dataclass(frozen=True)
class GitDocument:
    path: str
    content: str


@dataclass(frozen=True)
class Mutation:
    action: str
    path: str
    candidate_id: str
    preserve_history: bool = False
    lineage_ref: str | None = None


@dataclass
class PreservationState:
    last_marker: str | None = None
    last_git_sha: str | None = None
    last_transaction_id: str | None = None
    preserved_fingerprints: set[str] = field(default_factory=set)
    pending_queue_ids: set[str] = field(default_factory=set)


@dataclass
class PreservationTransaction:
    transaction_id: str
    reconciliation: dict[str, list[str]]
    amend: list[Mutation]
    create: list[Mutation]
    consumed_fingerprints: set[str]
    final_marker: str | None
    escalate_key_memory: bool = False
    offline_queue_package_id: str | None = None
    remote_verified: bool = False
    status: str = "READY_TO_PERSIST"

    def next_state(self, *, last_git_sha: str | None, transaction_id: str | None = None) -> PreservationState:
        # Backwards-compatible helper for callers that already performed external verification.
        if not last_git_sha:
            raise ValueError("verified remote SHA is required to advance preservation boundary")
        return PreservationState(
            last_marker=self.final_marker,
            last_git_sha=last_git_sha,
            last_transaction_id=transaction_id or self.transaction_id,
            preserved_fingerprints=set(self.consumed_fingerprints),
        )

    def advance_state(self, prior: PreservationState, *, verified_sha: str | None) -> PreservationState:
        if not verified_sha:
            raise ValueError("verified remote SHA is required to advance preservation boundary")
        return PreservationState(
            last_marker=self.final_marker,
            last_git_sha=verified_sha,
            last_transaction_id=self.transaction_id,
            preserved_fingerprints=set(self.consumed_fingerprints),
            pending_queue_ids=set(prior.pending_queue_ids),
        )


def _document_contains(doc: GitDocument, candidate: Candidate) -> bool:
    return _fold(candidate.content) in _fold(doc.content)


def plan_preservation(
    candidates: list[Candidate],
    git_truth: dict[str, GitDocument],
    state: PreservationState,
    *,
    github_available: bool = True,
    checkpoint: bool = False,
) -> PreservationTransaction:
    reconciliation = {key: [] for key in ("duplicate", "additive", "conflicting", "superseding", "new_topic")}
    amend: list[Mutation] = []
    create: list[Mutation] = []
    consumed = set(state.preserved_fingerprints)
    final_marker = state.last_marker

    for candidate in candidates:
        final_marker = candidate.marker or final_marker
        if candidate.fingerprint in state.preserved_fingerprints:
            reconciliation["duplicate"].append(candidate.candidate_id)
            consumed.add(candidate.fingerprint)
            continue

        target = git_truth.get(candidate.target_path) if candidate.target_path else None
        if target and _document_contains(target, candidate):
            reconciliation["duplicate"].append(candidate.candidate_id)
            consumed.add(candidate.fingerprint)
            continue

        relation = candidate.relation.casefold()
        if relation in {"contradiction", "conflicting"}:
            reconciliation["conflicting"].append(candidate.candidate_id)
        elif relation in {"superseding", "supersession", "reversal"}:
            reconciliation["superseding"].append(candidate.candidate_id)
        elif target:
            reconciliation["additive"].append(candidate.candidate_id)
        else:
            reconciliation["new_topic"].append(candidate.candidate_id)

        if target:
            amend.append(
                Mutation(
                    action="amend",
                    path=target.path,
                    candidate_id=candidate.candidate_id,
                    preserve_history=relation in {"contradiction", "conflicting", "superseding", "supersession", "reversal"},
                    lineage_ref=candidate.supersedes,
                )
            )
        else:
            path = candidate.proposed_path
            if path:
                create.append(Mutation(action="create", path=path, candidate_id=candidate.candidate_id))
        consumed.add(candidate.fingerprint)

    tx_id = f"preserve-{uuid.uuid4().hex[:12]}"
    offline_id = None
    status = "READY_TO_PERSIST"
    if not github_available:
        offline_id = f"GQ-{tx_id.upper()}"
        status = "STAGED — NOT COMMITTED"

    return PreservationTransaction(
        transaction_id=tx_id,
        reconciliation=reconciliation,
        amend=amend,
        create=create,
        consumed_fingerprints=consumed,
        final_marker=final_marker,
        escalate_key_memory=checkpoint,
        offline_queue_package_id=offline_id,
        remote_verified=False,
        status=status,
    )


def load_state(path: str) -> PreservationState:
    if not os.path.exists(path):
        return PreservationState()
    with open(path, "r", encoding="utf-8") as handle:
        data = json.load(handle)
    return PreservationState(
        last_marker=data.get("last_marker"),
        last_git_sha=data.get("last_git_sha"),
        last_transaction_id=data.get("last_transaction_id"),
        preserved_fingerprints=set(data.get("preserved_fingerprints", [])),
        pending_queue_ids=set(data.get("pending_queue_ids", [])),
    )


def save_state(path: str, state: PreservationState) -> None:
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    payload = {
        "last_marker": state.last_marker,
        "last_git_sha": state.last_git_sha,
        "last_transaction_id": state.last_transaction_id,
        "preserved_fingerprints": sorted(state.preserved_fingerprints),
        "pending_queue_ids": sorted(state.pending_queue_ids),
    }
    directory = os.path.dirname(path) or "."
    fd, tmp = tempfile.mkstemp(prefix=".preserve-state-", suffix=".json", dir=directory, text=True)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as handle:
            json.dump(payload, handle, indent=2, ensure_ascii=False)
            handle.write("\n")
        os.replace(tmp, path)
    except Exception:
        try:
            os.unlink(tmp)
        except FileNotFoundError:
            pass
        raise


def route_executor(*, code_change: bool, broad_git_mutation: bool) -> str:
    """Return the default execution surface after semantic reconciliation."""
    if code_change:
        return "Codex"
    if broad_git_mutation:
        return "Manus"
    return "ChatGPT"


def build_offline_queue_manifest(
    transaction: PreservationTransaction,
    *,
    target_repository: str,
) -> dict:
    if transaction.status != "STAGED — NOT COMMITTED" or not transaction.offline_queue_package_id:
        raise ValueError("transaction is not an offline-staged preservation")
    mutations = []
    for mutation in [*transaction.amend, *transaction.create]:
        mutations.append(
            {
                "action": mutation.action,
                "path": mutation.path,
                "candidate_id": mutation.candidate_id,
                "preserve_history": mutation.preserve_history,
                "lineage_ref": mutation.lineage_ref,
            }
        )
    return {
        "queue_package_id": transaction.offline_queue_package_id,
        "transaction_id": transaction.transaction_id,
        "status": "STAGED — NOT COMMITTED",
        "target_repository": target_repository,
        "mutations": mutations,
        "reconciliation": transaction.reconciliation,
        "required_completion_gate": "push + verify remote SHA before advancing preserve boundary",
    }
