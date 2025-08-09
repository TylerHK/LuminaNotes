import json
import sys
from pathlib import Path


REQUIRED_KEYS = {"version", "entities", "relations"}


def main() -> None:
    if len(sys.argv) < 2:
        print("FAIL: provide path to JSON file")
        raise SystemExit(1)
    path = Path(sys.argv[1])
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # pragma: no cover - CLI feedback
        print(f"FAIL: {exc}")
        raise SystemExit(1)
    missing = REQUIRED_KEYS - data.keys()
    if missing:
        print(f"FAIL: missing keys: {', '.join(sorted(missing))}")
        raise SystemExit(1)
    print("OK")


if __name__ == "__main__":
    main()
