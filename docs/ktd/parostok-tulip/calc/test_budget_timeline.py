import json
from pathlib import Path

from budget_timeline import add_months, compute, wait_for_season

HERE = Path(__file__).parent


def load():
    return json.loads((HERE / "budget_inputs.json").read_text(encoding="utf-8"))


def test_month_arithmetic():
    assert add_months((2026, 11), 2) == (2027, 1)
    assert add_months((2027, 12), 12) == (2028, 12)
    assert wait_for_season((2028, 2), [9, 10, 11]) == (2028, 9)
    assert wait_for_season((2028, 10), [9, 10, 11]) == (2028, 10)


def test_results_file_matches_inputs():
    saved = json.loads((HERE / "budget_results.json").read_text(encoding="utf-8"))
    assert compute(load()) == saved


def test_bounds_ordered_and_cumulative():
    r = compute(load())
    for s in r["stages"]:
        assert s["total_eur"][0] <= s["total_eur"][1]
    assert r["stages"][-1]["cumulative_eur"] == r["total_eur"]


def test_field_trial_starts_in_season():
    r = compute(load())
    for sched in (r["schedule_fast"], r["schedule_slow"]):
        s6 = next(s for s in sched if s["id"] == "S6")
        assert int(s6["start"][5:]) in (9, 10, 11)
