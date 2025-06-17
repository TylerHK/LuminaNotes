"""Convert a macro JSON file to markdown summary and timeline plot."""

import json
from pathlib import Path
from typing import Any, Dict, List

import matplotlib.pyplot as plt
import pandas as pd
import typer

app = typer.Typer(add_completion=False)


@app.command()
def convert(
    macro: Path,
    markdown_out: Path = typer.Option(Path("macro_summary.md")),
    png_out: Path = typer.Option(Path("macro_timeline.png")),
):
    """Generate markdown summary and a timeline image."""
    events: List[Dict[str, Any]] = json.loads(macro.read_text())
    steps = [e for e in events if e.get("type") == "step"]
    if not steps:
        typer.echo("No steps found in macro")
        return
    t0 = steps[0]["time"]
    for s in steps:
        s["elapsed"] = s["time"] - t0
    df = pd.DataFrame(steps)
    md_lines = [
        "| step | prompt | response | elapsed (s) |",
        "|------|--------|----------|-------------|",
    ]
    for i, row in df.iterrows():
        md_lines.append(
            f"| {i+1} | {row['prompt']} | {row['response']} | {row['elapsed']:.2f} |"
        )
    markdown_out.write_text("\n".join(md_lines), encoding="utf-8")
    plt.figure()
    plt.plot(df.index + 1, df["elapsed"], marker="o")
    plt.xlabel("Step")
    plt.ylabel("Elapsed (s)")
    plt.tight_layout()
    plt.savefig(png_out)
    typer.echo(f"Wrote {markdown_out} and {png_out}")


if __name__ == "__main__":  # pragma: no cover
    app()
