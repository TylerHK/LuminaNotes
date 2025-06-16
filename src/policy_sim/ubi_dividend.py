"""Simple AI dividend UBI model."""

from typing import List

import pandas as pd
import typer

app = typer.Typer(add_completion=False)


def compute_payments(pop: int, gdp: float, ai_share: float, dividend_pct: float, years: int) -> pd.DataFrame:
    """Return a DataFrame with annual per-capita payment."""
    data = []
    for year in range(years):
        pool = gdp * ai_share * dividend_pct
        payment = pool / pop
        data.append({"year": year + 1, "payment": payment})
    return pd.DataFrame(data)


@app.command()
def main(
    pop: int = typer.Option(..., help="Population size"),
    gdp: float = typer.Option(..., help="Annual GDP"),
    ai_share: float = typer.Option(0.1, help="Share of GDP from AI"),
    dividend_pct: float = typer.Option(0.2, help="Percent of AI GDP returned"),
    years: int = typer.Option(1, help="Number of years to simulate"),
):
    df = compute_payments(pop, gdp, ai_share, dividend_pct, years)
    typer.echo(df.to_string(index=False))


if __name__ == "__main__":  # pragma: no cover
    app()

