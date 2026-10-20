"""Детермінований розрахунок енергобалансу СВЧ-обробки луковиць тюльпана.

Вхід: inputs.json поруч зі скриптом. Вихід: results.json (stdout або --write).
Розрахунок дає діапазони (min/max) з інтервальних вхідних даних;
жодне значення не є виміряним.
"""
import json
import math
import sys
from pathlib import Path

HERE = Path(__file__).parent


def bulb_geometry(c_cm):
    d_cm = c_cm / math.pi
    v_cm3 = math.pi * d_cm ** 3 / 6
    return d_cm, v_cm3


def siebel_cp(w):
    return 3.35 * w + 0.84


def compute(inp):
    rho_lo, rho_hi = inp["bulb_density_kg_m3"]["value"]
    sf_lo, sf_hi = inp["shape_factor_vs_sphere"]["value"]
    w_lo, w_hi = inp["moisture_wet_basis"]["value"]
    t_in = inp["t_inlet_c"]["value"]
    t_lo, t_hi = inp["t_core_target_c"]["value"]
    eta_m = inp["magnetron_efficiency"]["value"]
    eta_c = inp["applicator_coupling_efficiency"]["value"]
    dp = inp["penetration_depth_cm_2450"]["value"]

    grades = []
    for c_lo, c_hi in inp["bulb_grades_cm"]["value"]:
        d_lo, v_lo = bulb_geometry(c_lo)
        d_hi, v_hi = bulb_geometry(c_hi)
        m_lo = v_lo * sf_lo * rho_lo / 1000  # г
        m_hi = v_hi * sf_hi * rho_hi / 1000
        grades.append({
            "grade_cm": f"{c_lo}/{c_hi}",
            "diameter_mm": [round(d_lo * 10, 1), round(d_hi * 10, 1)],
            "mass_g": [round(m_lo, 1), round(m_hi, 1)],
            "radius_to_penetration_depth": [round(d_lo / 2 / dp, 2), round(d_hi / 2 / dp, 2)],
        })

    cp_lo, cp_hi = siebel_cp(w_lo), siebel_cp(w_hi)
    dt_lo, dt_hi = t_lo - t_in, t_hi - t_in
    q_lo = cp_lo * dt_lo / 3.6  # кВт*год/т
    q_hi = cp_hi * dt_hi / 3.6
    eta_lo = eta_m[0] * eta_c[0]
    eta_hi = eta_m[1] * eta_c[1]

    module_kw = inp["mw_module_kw"]["value"]
    power = []
    for g in inp["throughput_t_per_h"]["value"]:
        absorbed = [q_lo * g, q_hi * g]
        gen = [absorbed[0] / eta_c[1], absorbed[1] / eta_c[0]]
        power.append({
            "throughput_t_per_h": g,
            "absorbed_kw": [round(absorbed[0], 1), round(absorbed[1], 1)],
            "mw_generator_output_kw": [round(gen[0], 1), round(gen[1], 1)],
            "modules_needed": [math.ceil(gen[0] / module_kw), math.ceil(gen[1] / module_kw)],
            "mains_for_mw_kw": [round(absorbed[0] / eta_hi, 1), round(absorbed[1] / eta_lo, 1)],
        })

    width = inp["belt_width_m"]["value"]
    k = inp["bulb_footprint_factor"]["value"]
    m_b = inp["design_bulb_mass_g"]["value"]
    d_b = inp["design_bulb_diameter_mm"]["value"] / 1000
    t_exp = inp["exposure_time_s"]["value"]
    conveyor = []
    for g in inp["throughput_t_per_h"]["value"]:
        bulbs_per_h = g * 1e6 / m_b
        area_m2_per_h = bulbs_per_h * (k * d_b) ** 2
        v_m_s = area_m2_per_h / width / 3600
        conveyor.append({
            "throughput_t_per_h": g,
            "bulbs_per_h": round(bulbs_per_h),
            "belt_speed_mm_s": round(v_m_s * 1000, 1),
            "mw_zone_length_m": [round(v_m_s * t_exp[0], 2), round(v_m_s * t_exp[1], 2)],
        })

    return {
        "status": "COMPUTED_FROM_ASSUMPTIONS",
        "cp_kj_kgk": [round(cp_lo, 3), round(cp_hi, 3)],
        "delta_t_k": [dt_lo, dt_hi],
        "specific_energy_kwh_per_t": [round(q_lo, 2), round(q_hi, 2)],
        "overall_efficiency": [round(eta_lo, 3), round(eta_hi, 3)],
        "grades": grades,
        "power": power,
        "conveyor_monolayer": conveyor,
    }


def main(argv):
    inp = json.loads((HERE / "inputs.json").read_text(encoding="utf-8"))
    out = json.dumps(compute(inp), ensure_ascii=False, indent=2) + "\n"
    if "--write" in argv:
        (HERE / "results.json").write_text(out, encoding="utf-8")
    sys.stdout.write(out)


if __name__ == "__main__":
    main(sys.argv[1:])
