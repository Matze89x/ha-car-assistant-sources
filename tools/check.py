"""Check this source before you push it: python3 tools/check.py

Every package listed in integrations/index.json and plugins/index.json needs a folder named like its id with a plugin.json inside,
the ids must match, and the version in the index should be the one in plugin.json. Exit code 1 when something is wrong."""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
ID = re.compile(r"^[a-z0-9][a-z0-9_-]{1,40}$")
problems = []


def load(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as exc:
        problems.append(f"{path.relative_to(ROOT)}: {exc}")
        return None


for kind in ("integrations", "plugins"):
    index = load(ROOT / kind / "index.json")
    if not isinstance(index, dict) or not isinstance(index.get("packages"), list):
        problems.append(f"{kind}/index.json: needs a list under 'packages'")
        continue
    seen = set()
    for item in index["packages"]:
        pid = item.get("id") if isinstance(item, dict) else None
        if not isinstance(pid, str) or not ID.match(pid):
            problems.append(f"{kind}/index.json: bad or missing id {pid!r}")
            continue
        if pid in seen:
            problems.append(f"{kind}/index.json: id {pid} listed twice")
        seen.add(pid)
        manifest = load(ROOT / kind / pid / "plugin.json")
        if not isinstance(manifest, dict):
            continue
        if manifest.get("id") != pid:
            problems.append(f"{kind}/{pid}/plugin.json: id must be {pid!r}")
        if str(manifest.get("version", "")) != str(item.get("version", "")):
            problems.append(f"{kind}/{pid}: version differs between index.json and plugin.json")
    for folder in sorted(p.name for p in (ROOT / kind).iterdir() if p.is_dir()):
        if folder not in seen:
            problems.append(f"{kind}/{folder}: folder is not listed in {kind}/index.json")

print("\n".join(problems) if problems else "OK")
sys.exit(1 if problems else 0)
