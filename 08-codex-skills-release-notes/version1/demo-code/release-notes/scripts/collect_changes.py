"""Group conventional commits since a tag and suggest the next version."""
import re
import subprocess
import sys

PATTERN = re.compile(r"^(\w+)(?:\(([^)]*)\))?(!)?: (.+?)(?: \(#(\d+)\))?$")


def git(*args):
    return subprocess.run(["git", "-c", "safe.directory=*", *args], capture_output=True, text=True, check=True).stdout.strip()


def main():
    tag = sys.argv[1] if len(sys.argv) > 1 else git("describe", "--tags", "--abbrev=0")
    subjects = git("log", f"{tag}..HEAD", "--reverse", "--pretty=%s").splitlines()
    groups = {"breaking": [], "feat": [], "fix": []}
    skipped = 0
    for line in subjects:
        m = PATTERN.match(line)
        if not m:
            skipped += 1
            continue
        kind, _scope, bang, summary, pr = m.groups()
        entry = f"- {summary}" + (f" (#{pr})" if pr else "")
        if bang:
            groups["breaking"].append(entry)
        elif kind in ("feat", "fix"):
            groups[kind].append(entry)
        else:
            skipped += 1
    major, minor, patch = (int(x) for x in tag.lstrip("v").split("."))
    if groups["breaking"]:
        nxt = f"{major + 1}.0.0"
    elif groups["feat"]:
        nxt = f"{major}.{minor + 1}.0"
    else:
        nxt = f"{major}.{minor}.{patch + 1}"
    print(f"since: {tag}\nnext-version: {nxt}\nskipped: {skipped}")
    for key, title in (("breaking", "Breaking changes"), ("feat", "Features"), ("fix", "Fixes")):
        print(f"\n[{title}]")
        print("\n".join(groups[key]) or "(none)")


if __name__ == "__main__":
    main()
