import json
import math
from pathlib import Path

from energy_balance import bulb_geometry, compute, siebel_cp

HERE = Path(__file__).parent


def test_geometry_12cm():
    d, v = bulb_geometry(12)
    assert math.isclose(d, 3.8197, rel_tol=1e-4)
    assert math.isclose(v, 29.18, rel_tol=1e-3)


def test_siebel_water_like():
    assert math.isclose(siebel_cp(1.0), 4.19, rel_tol=1e-6)


def test_results_file_matches_inputs():
    inp = json.loads((HERE / "inputs.json").read_text(encoding="utf-8"))
    saved = json.loads((HERE / "results.json").read_text(encoding="utf-8"))
    assert compute(inp) == saved


def test_power_monotonic_in_throughput():
    inp = json.loads((HERE / "inputs.json").read_text(encoding="utf-8"))
    p = [row["absorbed_kw"][1] for row in compute(inp)["power"]]
    assert p == sorted(p)


def test_modules_cover_unrounded_output():
    inp = json.loads((HERE / "inputs.json").read_text(encoding="utf-8"))
    one = next(r for r in compute(inp)["power"] if r["throughput_t_per_h"] == 1.0)
    # 7 x 1.5 kW = 10.5 kW < 10.52 kW unrounded lower bound
    assert one["modules_needed"] == [8, 23]
