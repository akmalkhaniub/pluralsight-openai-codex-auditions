"""Verify the intentional red state, green and refactored examples, and test sensitivity."""
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parent
def run_at(folder):
    return subprocess.run(
        [sys.executable, "-m", "unittest", "-v", "test_discounts"],
        cwd=folder, capture_output=True, text=True
    )

expected_tests = (ROOT / "demo-code/test_discounts.py").read_bytes()
for stage in ("red", "green", "refactored"):
    source = ROOT / "rehearsal" / stage
    assert (source / "test_discounts.py").read_bytes() == expected_tests
    with tempfile.TemporaryDirectory() as tmp:
        for name in ("discount_service.py", "test_discounts.py"):
            shutil.copyfile(source / name, Path(tmp) / name)
        result = run_at(tmp)
        expected_code = 1 if stage == "red" else 0
        assert result.returncode == expected_code, result.stderr
        assert "Ran 8 tests" in result.stderr, result.stderr
        if stage == "red":
            assert "errors=8" in result.stderr and "NotImplementedError" in result.stderr
        print(stage + ": verified expected result")

reference = (ROOT / "rehearsal/refactored/discount_service.py").read_text()
mutants = {
    "exclusive threshold": reference.replace('>= Decimal("100.00")', '> Decimal("100.00")'),
    "wrong rounding": reference.replace("ROUND_HALF_UP", "ROUND_HALF_EVEN"),
    "missing discount": reference.replace('Decimal("0.90")', 'Decimal("1.00")'),
}
for name, code in mutants.items():
    with tempfile.TemporaryDirectory() as tmp:
        (Path(tmp) / "discount_service.py").write_text(code)
        (Path(tmp) / "test_discounts.py").write_bytes(expected_tests)
        result = run_at(tmp)
        assert result.returncode != 0 and "FAIL:" in result.stderr, name
        print(name + ": detected by tests")
print("All rehearsal and sensitivity checks passed.")
