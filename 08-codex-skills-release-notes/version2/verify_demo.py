"""Check the release-notes skill script against the demo repo (run from this folder)."""
import pathlib, subprocess, sys
root = pathlib.Path(__file__).resolve().parents[2]
out = subprocess.run([sys.executable, str(root / "skills-kit/release-notes/scripts/collect_changes.py"), "v1.2.0"],
                     cwd=root / "skills-take", capture_output=True, text=True, check=True).stdout
for needle in ("next-version: 2.0.0", "rename /orders/list to /orders (#46)", "add gift-wrap option (#41)", "skipped: 3"):
    assert needle in out, needle
print(out); print("Skill script verified.")
