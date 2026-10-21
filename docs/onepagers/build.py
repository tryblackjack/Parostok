"""Збирає одноаркушники Parostok у HTML і PDF (A4, одна сторінка).

python3 build.py  → out/*.html, out/*.pdf
PDF друкує Chromium (/opt/pw-browsers/chromium) у headless-режимі.
"""
import base64
import html
import subprocess
import sys
from pathlib import Path

from content import CONTACT, EQUIPMENT, SPECS, TULIP

HERE = Path(__file__).parent
OUT = HERE / "out"
CHROME = "/opt/pw-browsers/chromium"

FIG = {
    "en": ("flower bud", "field penetrates ≈ 1 cm", "bulb 32–45 mm"),
    "fr": ("bourgeon floral", "pénétration du champ ≈ 1 cm", "bulbe 32–45 mm"),
    "nl": ("bloemknop", "indringdiepte ≈ 1 cm", "bol 32–45 mm"),
}

CSS = """
@page { size: A4; margin: 0; }
:root { --blue:#1d5aa8; --blue-dark:#123d73; --ink:#1b2430; --muted:#5b6675; --line:#d9e1ea; --tint:#eef3f9; }
* { box-sizing:border-box; }
html, body { margin:0; padding:0; background:#fff; }
body { width:210mm; height:297mm; overflow:hidden; font-family:Carlito, "Liberation Sans", sans-serif;
       color:var(--ink); font-size:10pt; line-height:1.34; -webkit-print-color-adjust:exact; print-color-adjust:exact; }
header { background:var(--blue); color:#fff; padding:10mm 14mm 7.5mm; }
.brand { display:flex; justify-content:space-between; align-items:baseline; }
.mark { font-weight:800; letter-spacing:.18em; font-size:13pt; }
.kicker { text-transform:uppercase; letter-spacing:.12em; font-size:8pt; opacity:.85; }
h1 { font-size:19pt; line-height:1.15; margin:5mm 0 2.5mm; font-weight:750; }
.lead { font-size:10.2pt; max-width:170mm; margin:0; opacity:.95; }
main { padding:6mm 14mm 0; }
h2 { font-size:10.4pt; color:var(--blue-dark); margin:0 0 2mm; padding-bottom:1.2mm; border-bottom:1.5px solid var(--blue); }
.grid { display:grid; grid-template-columns: 1fr 1fr; gap:7mm; }
.grid + section { margin-top:4mm; }
.fig img { width:100%; display:block; border:1px solid var(--line); border-radius:2mm; }
.cap { color:var(--muted); font-size:7.8pt; margin-top:1.5mm; }
ul { margin:0; padding-left:4.2mm; }
li { margin:0 0 1.2mm; }
table { width:100%; border-collapse:collapse; font-size:9.2pt; }
td { padding:0.85mm 0; border-bottom:1px solid var(--line); vertical-align:top; }
td.v { text-align:right; font-weight:650; white-space:nowrap; padding-left:3mm; }
section { margin-bottom:3.6mm; }
.box { background:var(--tint); border-left:3px solid var(--blue); padding:3mm 4mm; border-radius:1mm; }
.plan td { padding:1.6mm 1.5mm; }
.plan td.n { width:7mm; font-weight:800; color:var(--blue); }
.plan td.t, .plan td.c { white-space:nowrap; text-align:right; color:var(--muted); }
.plan td.c { font-weight:650; color:var(--ink); }
.total { margin-top:2mm; font-weight:650; }
footer { position:absolute; left:0; right:0; bottom:0; padding:4mm 14mm 6mm; border-top:1px solid var(--line);
         font-size:8pt; color:var(--muted); display:flex; justify-content:space-between; gap:6mm; }
footer .c { color:var(--ink); font-weight:600; }
svg text { font-family:Carlito, "Liberation Sans", sans-serif; }
"""


def esc(s):
    return html.escape(s, quote=False)


def ul(items):
    # items may contain <b> markup written in content.py; nothing else is HTML
    return "<ul>" + "".join(f"<li>{i}</li>" for i in items) + "</ul>"


MULTI_CSS = """
@page { size: A4; margin: 12mm 0 12mm; }
@page :first { margin-top: 0; }
body { height:auto; overflow:visible; }
footer { position:static; margin-top:6mm; }
.keep { break-inside: avoid; }
"""


def page(lang, title, body_header, body_main, foot, multi=False):
    css = CSS + (MULTI_CSS if multi else "")
    return f"""<!doctype html>
<html lang="{lang}"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title><style>{css}</style></head>
<body>{body_header}<main>{body_main}</main>
<footer><span class="c">{esc(CONTACT)}</span><span>{esc(foot)}</span></footer>
</body></html>"""


def header(t):
    return f"""<header><div class="brand"><span class="mark">PAROSTOK</span><span class="kicker">{esc(t['kicker'])}</span></div>
<h1>{esc(t['title'])}</h1><p class="lead">{esc(t['lead'])}</p></header>"""


def equipment(code, t, img_b64, photo_b64):
    specs = "".join(f"<tr><td>{esc(k)}</td><td class='v'>{esc(v)}</td></tr>" for k, v in SPECS[code])
    main = f"""
<div class="grid">
  <div class="fig"><img src="data:image/webp;base64,{img_b64}" alt="Parostok"><div class="cap">{esc(t['caption'])}</div>
    <img src="data:image/jpeg;base64,{photo_b64}" alt="" style="margin-top:3mm;height:27mm;object-fit:cover"><div class="cap">{esc(t['photo'])}</div></div>
  <div>
    <section><h2>{esc(t['h_how'])}</h2>{ul([esc(x) for x in t['how']])}</section>
    <section><h2>{esc(t['h_specs'])}</h2><table>{specs}</table></section>
  </div>
</div>
<section><h2>{esc(t['h_evidence'])}</h2>{ul(t['evidence'])}</section>
<section><h2>{esc(t['h_conf'])}</h2>{ul(t['conf'])}</section>
<section class="box"><h2 style="border:0;padding:0;margin-bottom:1mm">{esc(t['h_for'])}</h2>{esc(t['for'])}</section>
"""
    return page(t["lang"], f"Parostok — {t['title']}", header(t), main, t["foot"])


def bulb_svg(code):
    bud, depth, size = FIG[code]
    return f"""<svg viewBox="0 0 400 180" width="100%" role="img" aria-label="{esc(depth)}">
  <circle cx="80" cy="86" r="70" fill="#f3e6cf" stroke="#b08a52" stroke-width="2"/>
  <circle cx="80" cy="86" r="70" fill="none" stroke="#1d5aa8" stroke-width="30" stroke-opacity=".22"/>
  <circle cx="80" cy="86" r="55" fill="none" stroke="#1d5aa8" stroke-width="1" stroke-dasharray="4 3"/>
  <path d="M80 62 C 68 74, 70 98, 80 110 C 90 98, 92 74, 80 62 Z" fill="#d9534f" opacity=".85"/>
  <line x1="91" y1="86" x2="168" y2="86" stroke="#1b2430" stroke-width="1"/>
  <text x="172" y="90" font-size="12" fill="#1b2430">{esc(bud)}</text>
  <line x1="138" y1="44" x2="168" y2="32" stroke="#1b2430" stroke-width="1"/>
  <text x="172" y="36" font-size="12" fill="#1d5aa8">{esc(depth)}</text>
  <text x="80" y="174" font-size="12" text-anchor="middle" fill="#5b6675">{esc(size)}</text>
</svg>"""


def line_svg(labels):
    crates, feeder, layer, mw, eq, n, check, crates2 = labels
    boxes = [(crates, "#ffffff"), (feeder, "#ffffff"), (layer, "#ffffff"), (mw, "#1d5aa8"),
             (eq, "#dbe6f4"), (check, "#ffffff"), (crates2, "#ffffff")]
    w, gap, x = 92, 14, 4
    parts = []
    for i, (label, fill) in enumerate(boxes):
        ink = "#ffffff" if fill == "#1d5aa8" else "#1b2430"
        words = label.split(" ")
        lines = [label] if len(label) <= 13 or len(words) == 1 else [" ".join(words[:-1]), words[-1]]
        y0 = 48 if len(lines) == 1 else 41
        spans = "".join(f'<tspan x="{x + w / 2}" y="{y0 + 13 * k}">{esc(s)}</tspan>' for k, s in enumerate(lines))
        parts.append(f'<rect x="{x}" y="22" width="{w}" height="44" rx="6" fill="{fill}" stroke="#1d5aa8" stroke-width="1.5"/>'
                     f'<text font-size="11.5" text-anchor="middle" fill="{ink}">{spans}</text>')
        if i < len(boxes) - 1:
            ax = x + w
            parts.append(f'<path d="M{ax + 2} 44 L{ax + gap - 3} 44" stroke="#1b2430" stroke-width="1.4" marker-end="url(#a)"/>')
        if i == 3:
            mw_x = x
        x += w + gap
    bracket = f'<path d="M{mw_x} 74 L{mw_x} 80 L{mw_x + 2 * w + gap} 80 L{mw_x + 2 * w + gap} 74" fill="none" stroke="#1d5aa8" stroke-width="1.2"/>' \
              f'<text x="{mw_x + w + gap / 2}" y="95" font-size="11" text-anchor="middle" fill="#1d5aa8">{esc(n)}</text>'
    return f"""<svg viewBox="0 0 {x} 100" width="100%" role="img" aria-label="{esc(mw)}">
  <defs><marker id="a" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" orient="auto"><path d="M0 0 L8 4 L0 8 z" fill="#1b2430"/></marker></defs>
  {''.join(parts)}{bracket}
</svg>"""


def tulip(code, t):
    plan = "".join(f"<tr><td class='n'>{esc(n)}</td><td>{esc(d)}</td><td class='t'>{esc(tm)}</td></tr>"
                   for n, d, tm in t["plan"])
    specs = "".join(f"<tr><td>{esc(k)}</td><td class='v'>{esc(v)}</td></tr>" for k, v in t["specs"])
    main = f"""
<section class="keep"><h2>{esc(t['h_line'])}</h2>{line_svg(t['line'])}<div class="cap">{esc(t['line_cap'])}</div></section>
<div class="grid">
  <section><h2>{esc(t['h_why'])}</h2>{ul([esc(x) for x in t['why']])}<div style="max-width:78mm;margin:3mm auto 0">{bulb_svg(code)}</div></section>
  <section><h2>{esc(t['h_specs'])}</h2><table>{specs}</table><div class="cap">{esc(t['specs_note'])}</div></section>
</div>
<section class="box keep"><h2 style="border:0;padding:0;margin-bottom:1mm">{esc(t['h_status'])}</h2>{esc(t['status'])}</section>
<div class="grid keep" style="break-before:page">
  <section><h2>{esc(t['h_design'])}</h2>{ul(t['design'])}</section>
  <section><h2>{esc(t['h_seek'])}</h2>{ul([esc(x) for x in t['seek']])}</section>
</div>
<section class="keep"><h2>{esc(t['h_plan'])}</h2><table class="plan">{plan}</table><div class="total">{esc(t['plan_total'])}</div></section>
"""
    return page(t["lang"], f"Parostok — {t['title']}", header(t), main, t["foot"], multi=True)


def pdf(html_path, pdf_path):
    subprocess.run([CHROME, "--headless=new", "--no-sandbox", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={pdf_path}", html_path.as_uri()],
                   check=True, capture_output=True, timeout=120)


def main():
    OUT.mkdir(exist_ok=True)
    img = base64.b64encode((HERE / "parostok_new_design.webp").read_bytes()).decode()
    photo = base64.b64encode((HERE / "lab_test_2026.jpg").read_bytes()).decode()
    docs = []
    for code in ("en", "fr", "nl"):
        docs.append((f"parostok_equipment_{code}", equipment(code, EQUIPMENT[code], img, photo)))
        docs.append((f"parostok_tulip_bulbs_{code}", tulip(code, TULIP[code])))
    for name, doc in docs:
        h = OUT / f"{name}.html"
        h.write_text(doc, encoding="utf-8")
        if "--no-pdf" not in sys.argv:
            pdf(h, OUT / f"{name}.pdf")
        print(name)


if __name__ == "__main__":
    main()
