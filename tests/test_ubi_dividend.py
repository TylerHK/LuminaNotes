import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from policy_sim.ubi_dividend import compute_payments


def test_compute_payments():
    df = compute_payments(pop=100, gdp=1000, ai_share=0.1, dividend_pct=0.5, years=1)
    assert df.loc[0, "payment"] == 0.5
