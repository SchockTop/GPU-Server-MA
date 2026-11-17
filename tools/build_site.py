"""Builds index.html (self-contained overview page) from research/*.csv.

Usage: python tools/build_site.py
Reads  research/gpu-master-table.csv and, if present, research/prices-b2b.csv.
"""
import csv, json, pathlib, re

ROOT = pathlib.Path(__file__).resolve().parent.parent
R = ROOT / "research"


def num(s):
    m = re.match(r"\s*(\d+(?:\.\d+)?)(?![\d.]*\s*x)", str(s).replace(",", ""))
    return float(m.group(1)) if m else None


def vendor(group):
    if group.startswith("GeForce"):
        return "geforce"
    if group.startswith("AMD"):
        return "amd"
    if group.startswith("Intel"):
        return "intel"
    return "nvpro"


cards = []
for r in csv.DictReader(open(R / "gpu-master-table.csv", encoding="utf-8", newline="")):
    cond = r["condition"]
    cards.append({
        "name": r["name"], "vendor": vendor(r["group"]), "group": r["group"],
        "used": cond.lower().startswith("used") or "(used)" in r["name"],
        "cond": cond, "price": num(r["price_lowest_eur_brutto"]),
        "typ": num(r["price_typical_eur_brutto"]), "src": r["price_source"],
        "vram": num(r["vram_gb"]), "mem": r["memory_type"], "bw": num(r["bandwidth_gbs"]),
        "cores": num(r["cuda_cores_or_shaders"]), "tensor": r["tensor_cores"], "rt": r["rt_cores"],
        "fp32": num(r["fp32_tflops"]), "fp16": r["fp16_bf16_tensor_dense_tflops"],
        "tdp": num(r["tdp_w"]), "slots": r["slots"], "cooling": r["cooling"],
        "ecc": r["ecc"], "vgpu": r["vgpu"], "mig": r["mig"],
        "blender": num(r["blender_4_5_median"]), "bn": num(r["blender_n"]),
        "bnote": r["blender_note"], "llm": num(r["llama7b_q4_tg128"]), "lnote": r["llama_note"],
    })

b2b = []
p = R / "prices-b2b.csv"
if p.exists():
    for r in csv.DictReader(open(p, encoding="utf-8", newline="")):
        b2b.append({k: (r.get(k) or "").strip() for k in
                    ["card", "sku", "reseller", "price_net_eur", "price_brutto_eur",
                     "shown_as", "availability", "url", "evidence"]})

html = (ROOT / "tools" / "template.html").read_text(encoding="utf-8")
html = html.replace("/*CARDS*/[]", json.dumps(cards, ensure_ascii=False))
html = html.replace("{{N}}", str(len(cards)))
html = html.replace("/*B2B*/[]", json.dumps(b2b, ensure_ascii=False))
(ROOT / "index.html").write_text(html, encoding="utf-8")
print("index.html written:", len(cards), "cards,", len(b2b), "b2b prices")
