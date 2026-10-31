"""Run the AGENTS.md demo repo's tests (run from this folder)."""
import pathlib, subprocess, sys
root = pathlib.Path(__file__).resolve().parents[2]
r = subprocess.run([sys.executable, "-m", "unittest", "discover", "-s", "tests", "-v"], cwd=root / "agents-take")
sys.exit(r.returncode)
