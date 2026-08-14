from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import unittest

MODULE_DIR = Path(__file__).resolve().parents[1]
ROOT = MODULE_DIR.parents[1]
MEMORY_DIR = ROOT / "03_Modules" / "YOS_Memory"
for path in (str(MODULE_DIR), str(MEMORY_DIR)):
    if path not in sys.path:
        sys.path.insert(0, path)


class CanonicalExecutionContractTests(unittest.TestCase):
    def test_module_contract_is_not_implemented_yet(self):
        self.assertIsNone(
            importlib.util.find_spec("canonical_execution"),
            "RED gate: canonical_execution unexpectedly exists before implementation",
        )


if __name__ == "__main__":
    unittest.main()
