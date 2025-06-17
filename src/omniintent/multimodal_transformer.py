"""Placeholder transformer implementation with demo loop."""

import pathlib

import typer

from .macro_recorder import log_event, save_json, start_record, stop_record

app = typer.Typer(add_completion=False)


class MultimodalTransformer:
    """A stub multimodal transformer model."""

    def __init__(self):
        self.config = {}

    def forward(self, *inputs):
        raise NotImplementedError("Model forward pass not implemented")


@app.command()
def demo(
    record: bool = typer.Option(False, help="Record interaction"),
    macro_path: pathlib.Path = typer.Option(
        pathlib.Path("macros/demo.json"), help="Output macro JSON"
    ),
):
    """Simple interactive demo for the transformer."""
    model = MultimodalTransformer()
    if record:
        start_record()
    typer.echo("Type 'quit' to exit.")
    while True:
        prompt = input(">>> ")
        if prompt.lower() in {"quit", "exit"}:
            break
        response = f"Echo: {prompt}"
        print(response)
        if record:
            log_event(prompt, response)
    if record:
        stop_record()
        save_json(macro_path)
        typer.echo(f"Saved macro to {macro_path}")


if __name__ == "__main__":  # pragma: no cover
    app()
