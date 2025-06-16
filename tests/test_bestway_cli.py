import json
import os
import sys
from pathlib import Path

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from typer.testing import CliRunner

from bestway.CLI.ingest import app

runner = CliRunner()

def test_ingest_creates_json(tmp_path):
    source = Path("bestway/templates/recipe_template.md")
    out_path = Path("data/bestway_recipes/recipe_template.json")
    if out_path.exists():
        out_path.unlink()
    result = runner.invoke(app, [str(source)])
    assert result.exit_code == 0
    assert out_path.exists()
    data = json.loads(out_path.read_text())
    assert data["title"] == "Sample Recipe"
    out_path.unlink()
