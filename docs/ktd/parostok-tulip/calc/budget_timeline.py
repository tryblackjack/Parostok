"""Детермінований кошторис і календарний графік ДКР «Паросток-Т».

Вхід: budget_inputs.json. Вихід: budget_results.json (stdout або --write).
Нижня межа = мінімальні тривалості, ставки і ціни; верхня = максимальні.
Етапи послідовні; етап з season_start_months чекає на найближчий дозволений місяць.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent


def labour_month_eur(inp, role):
    lab = inp["labour"]
    gross = lab["roles_uah_gross"][role]["value"]
    esv = lab["esv_rate"]["value"]
    oh = lab["overhead_factor"]["value"]
    fx = inp["fx"]["eur_uah"]["value"]
    return [gross[i] * (1 + esv) * oh[i] / fx for i in (0, 1)]


def purchase_eur(inp, p):
    if "eur" in p:
        return list(p["eur"])
    unit = inp["unit_prices"][p["unit"]]["value"]
    qty = p["qty"] if isinstance(p["qty"], list) else [p["qty"], p["qty"]]
    return [qty[0] * unit[0], qty[1] * unit[1]]


def add_months(ym, n):
    y, m = ym
    m += n
    return (y + (m - 1) // 12, (m - 1) % 12 + 1)


def wait_for_season(ym, allowed):
    while ym[1] not in allowed:
        ym = add_months(ym, 1)
    return ym


def fmt(ym):
    return f"{ym[0]:04d}-{ym[1]:02d}"


def schedule(inp, bound):
    y, m = map(int, inp["start"]["value"].split("-"))
    cur = (y, m)
    rows = []
    for st in inp["stages"]:
        start = cur
        if "season_start_months" in st:
            start = wait_for_season(cur, st["season_start_months"])
        end = add_months(start, st["months"][bound])
        rows.append({"id": st["id"], "start": fmt(start), "end": fmt(end),
                     "idle_months_waiting_season": (start[0] - cur[0]) * 12 + start[1] - cur[1]})
        cur = end
    return rows


def compute(inp):
    stages = []
    cum = [0.0, 0.0]
    for st in inp["stages"]:
        lab = [0.0, 0.0]
        for role, fte in st["labour_fte"].items():
            rate = labour_month_eur(inp, role)
            for i in (0, 1):
                lab[i] += fte * st["months"][i] * rate[i]
        pur = [0.0, 0.0]
        for p in st["purchases"]:
            c = purchase_eur(inp, p)
            pur[0] += c[0]
            pur[1] += c[1]
        tot = [lab[i] + pur[i] for i in (0, 1)]
        cum = [cum[i] + tot[i] for i in (0, 1)]
        stages.append({"id": st["id"], "name": st["name"],
                       "labour_eur": [round(x) for x in lab],
                       "purchases_eur": [round(x) for x in pur],
                       "total_eur": [round(x) for x in tot],
                       "cumulative_eur": [round(x) for x in cum]})
    k = inp["contingency"]["value"]
    gate = next(s for s in stages if s["id"] == "S2")["cumulative_eur"]
    return {
        "status": "COMPUTED_FROM_ASSUMPTIONS",
        "labour_month_eur": {r: [round(x) for x in labour_month_eur(inp, r)]
                             for r in inp["labour"]["roles_uah_gross"]},
        "stages": stages,
        "to_gate_S2_eur": gate,
        "to_gate_S2_with_contingency_eur": [round(gate[0] * (1 + k[0])), round(gate[1] * (1 + k[1]))],
        "total_eur": [round(cum[0]), round(cum[1])],
        "total_with_contingency_eur": [round(cum[0] * (1 + k[0])), round(cum[1] * (1 + k[1]))],
        "schedule_fast": schedule(inp, 0),
        "schedule_slow": schedule(inp, 1),
    }


def main(argv):
    inp = json.loads((HERE / "budget_inputs.json").read_text(encoding="utf-8"))
    out = json.dumps(compute(inp), ensure_ascii=False, indent=2) + "\n"
    if "--write" in argv:
        (HERE / "budget_results.json").write_text(out, encoding="utf-8")
    sys.stdout.write(out)


if __name__ == "__main__":
    main(sys.argv[1:])
