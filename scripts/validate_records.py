"""Validate repository records against their JSON Schemas.

Usage: python scripts/validate_records.py [--root PATH]

Each rule maps a glob of record files to the schema they must satisfy.
Every tracked *.json file is also checked to be well-formed JSON.
Exits non-zero if any file fails.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from jsonschema import Draft202012Validator
from jsonschema.exceptions import SchemaError

# (record glob, schema path) relative to the repository root.
RULES: list[tuple[str, str]] = [
    ("data/bestway_recipes/*.json", "bestway/schema/bestway_schema.json"),
    ("Lumina/*/metadata.json", "schemas/lumina_project_metadata.schema.json"),
    ("swarm_sync/*.json", "schemas/swarm_sync_record.schema.json"),
    ("swarm_sync/swarm_index.json", "schemas/swarm_sync_index.schema.json"),
    ("src/omniintent/tokenizer_spec.json", "schemas/tokenizer_spec.schema.json"),
    ("tests/tokenizer_spec.json", "schemas/tokenizer_spec.schema.json"),
]

SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "site"}


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def check_well_formed(root: Path) -> list[str]:
    errors = []
    for path in sorted(root.rglob("*.json")):
        if SKIP_DIRS & set(path.relative_to(root).parts):
            continue
        try:
            load_json(path)
        except (json.JSONDecodeError, UnicodeDecodeError) as exc:
            errors.append(f"{path.relative_to(root)}: invalid JSON: {exc}")
    return errors


def check_rules(root: Path) -> tuple[list[str], int]:
    errors: list[str] = []
    checked = 0
    for pattern, schema_rel in RULES:
        schema_path = root / schema_rel
        try:
            schema = load_json(schema_path)
            Draft202012Validator.check_schema(schema)
        except (OSError, ValueError, SchemaError) as exc:
            errors.append(f"{schema_rel}: bad schema: {exc}")
            continue
        validator = Draft202012Validator(schema)
        for path in sorted(root.glob(pattern)):
            # The generated index maps keywords to timestamps; it is not a packet.
            if pattern == "swarm_sync/*.json" and path.name == "swarm_index.json":
                continue
            rel = path.relative_to(root)
            try:
                data = load_json(path)
            except ValueError:  # malformed JSON is reported by check_well_formed
                errors.append(f"{rel}: skipped schema check (unreadable JSON)")
                continue
            checked += 1
            for err in sorted(validator.iter_errors(data), key=lambda e: tuple(str(p) for p in e.path)):
                loc = "/".join(str(p) for p in err.path) or "<root>"
                errors.append(f"{rel}: {loc}: {err.message} (schema {schema_rel})")
    return errors, checked


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--root", type=Path, default=Path(__file__).resolve().parents[1]
    )
    args = parser.parse_args(argv)
    root = args.root.resolve()

    errors = check_well_formed(root)
    rule_errors, checked = check_rules(root)
    errors += rule_errors
    for line in errors:
        print(f"FAIL {line}")
    print(
        f"Checked {checked} record(s) against {len(RULES)} rule(s); {len(errors)} error(s)."
    )
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
