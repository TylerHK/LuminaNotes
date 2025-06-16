import json
import pathlib

import typer
import yaml
from jsonschema import validate

app = typer.Typer(add_completion=False)

SCHEMA_PATH = pathlib.Path(__file__).resolve().parents[1] / "schema" / "bestway_schema.json"
DATA_DIR = pathlib.Path(__file__).resolve().parents[2] / "data" / "bestway_recipes"


def parse_front_matter(path: pathlib.Path) -> dict:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        raise ValueError("Missing front matter")
    _, fm, _ = text.split("---", 2)
    return yaml.safe_load(fm)


@app.command()
def ingest(markdown: pathlib.Path) -> None:
    """Validate a recipe template and emit JSON."""
    data = parse_front_matter(markdown)
    schema = json.loads(SCHEMA_PATH.read_text())
    validate(instance=data, schema=schema)
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    out_path = DATA_DIR / (markdown.stem + ".json")
    out_path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    typer.echo(f"Wrote {out_path}")


if __name__ == "__main__":  # pragma: no cover
    app()
