import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "validate_records", ROOT / "scripts" / "validate_records.py"
)
validate_records = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validate_records)


def test_repository_records_are_valid():
    assert validate_records.main(["--root", str(ROOT)]) == 0


def test_invalid_record_is_reported(tmp_path, capsys):
    for _, schema_rel in validate_records.RULES:
        dest = tmp_path / schema_rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text((ROOT / schema_rel).read_text())
    (tmp_path / "data" / "bestway_recipes").mkdir(parents=True)
    (tmp_path / "data" / "bestway_recipes" / "bad.json").write_text(
        json.dumps({"title": "x"})
    )
    (tmp_path / "broken.json").write_text("{not json")
    assert validate_records.main(["--root", str(tmp_path)]) == 1
    out = capsys.readouterr().out
    assert "bad.json: <root>: 'context' is a required property" in out
    assert "broken.json: invalid JSON" in out
    assert "bad schema" not in out
