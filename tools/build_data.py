# -*- coding: utf-8 -*-
"""Baut daten/bdg.json aus den RIS-Rohtexten (XML-Fassung, bereits zu Text gewandelt) und den Fragen.
Aufruf: python3 -I build_data.py <ordner_mit_N.txt> <ausgabe.json>
"""
import json, re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fragen_bdg import FRAGEN

GRUPPEN = [
  ("Dienstverhältnis", ["2","4","5","7","10","11","20","21","22"]),
  ("Versetzung & Zuteilung", ["36","38","39","40","41"]),
  ("Dienstpflichten", ["43","43a","44","45","45a","45b","46","47","52","53","54","55","56","59","60"]),
  ("Dienstzeit & Bezüge", ["47a","48","48a","48c","49","50","51","145","62","63"]),
  ("Urlaub & Freistellung", ["65","68","69","70","71","74","75","75d","76","78e"]),
  ("Disziplinarrecht", ["90","92","94","96","109","112","131"]),
  ("Haftung", ["AHG","Regress","OHG","PolBEG"]),
]
HAFTUNG = {   # Kachel -> (Anzeigename, Titel, [(Unterordner im Textordner, Paragraf)])
  "AHG": ("AHG", "Amtshaftungsgesetz", [("ahg", p) for p in ("1","2","3","4")]),
  "Regress": ("Regress", "Rückersatz an das Organ (AHG § 3 und § 4)", [("ahg", "3"), ("ahg", "4")]),
  "OHG": ("OHG", "Organhaftpflichtgesetz", [("ohg", p) for p in ("1","2","3","4","5")]),
  "PolBEG": ("PolBEG", "Polizeibefugnis-Entschädigungsgesetz", [("polbeg", p) for p in ("1","2","3","4")]),
}
ORDER = [n for g in GRUPPEN for n in g[1]]
src, out = sys.argv[1], sys.argv[2]
import json as _json
try:
    ABGERUFEN = _json.load(open(os.path.join(src, "meta.json"), encoding="utf-8"))["abgerufen"]   # schreibt fetch_ris.py
except Exception:
    raise SystemExit("meta.json im Textordner fehlt: Texte zuerst mit fetch_ris.py holen")

def pretty(t):
    t = t.replace("GehGganz", "GehG ganz")
    t = re.sub(r"(?<=\S) {2,}", " ", t)
    t = re.sub(r"(?<=[\.\;\:\)a-zäöüß\d])\((\d{1,2}[a-z]?)\)(?=\s?[A-ZÄÖÜa-zäöü])", r"\n(\1)", t)
    t = re.sub(r"(?<![\d/§])(?<!Nr)(\d{1,2}[a-z]?)\.(?=[A-ZÄÖÜa-zäöü])", r"\n\1. ", t)
    t = re.sub(r"(?<=[a-zäöüß,;\.:])\s?([a-c])\)(?=[A-Za-zäöüÄÖÜ])", r"\n  \1) ", t)
    t = re.sub(r"(?<=\d,)(\d{1,2}[a-z]?)\.\s", r"\n\1. ", t)
    t = re.sub(r"(?<=[a-zäöüß])\.(?=[A-ZÄÖÜ][a-zäöü])", ". ", t)
    t = re.sub(r"\n{2,}", "\n", t)
    return t.strip()

# Darstellungsfehler im RIS-Rohtext (verklebte Wörter, verlorene Gedankenstriche, Schlusssätze nach Aufzählungen)
FIXES = [
  ("bestraft wurde,und dies", "bestraft wurde,\nund dies"),
  ("übersteigt.Das Dienstverhältnis wird jedoch", "übersteigt.\nDas Dienstverhältnis wird jedoch"),
  ("hatten,tätig zu werden", "hatten,\ntätig zu werden"),
  ("Reisegebühren,nicht zu berücksichtigen", "Reisegebühren,\nnicht zu berücksichtigen"),
  ("eines anderenerforderlich", "eines anderen\nerforderlich"),
  ("selbstgelegenen", "selbst gelegenen"),
  ("befindet,darf eine", "befindet,\ndarf eine"),
  ("Verwaltungsstrafverfahrensbei der", "Verwaltungsstrafverfahrens\nbei der"),
  ("aufsichtsbehörde.Im Verfahren vor der Bundesdisziplinarbehörde im PTA-Bereich", "aufsichtsbehörde.\nIm Verfahren vor der Bundesdisziplinarbehörde im PTA-Bereich"),
  ("wird  sofern der", "wird – sofern der"),
  ("Verfahren ist  gehemmt", "Verfahren ist – gehemmt"),
]
# Muster mit Platzhaltern für unsichtbare Sonderzeichen (z. B. geschützte Leerzeichen)
RFIXES = [
  (r"(§\s*76)gekündigt", r"\1 gekündigt"),
  (r"(\S)\s{2,}unbeschadet des (§\s*74)\s{2,}Anspruch", r"\1 – unbeschadet des \2 – Anspruch"),
]
USED = set()

# Skriptum-Etappe: neue Fragen (hinten angehängt), ausgeschlossene bestehende Fragen (x), Korrekturen
SKR = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "skriptum_fragen.json"), encoding="utf-8"))

# Stufen (1 leicht, 2 mittel, 3 schwer) der älteren Fragen: tools/fragen_level.json {id: Stufe}; neue Fragen tragen "lv" selbst
try: LEVELS = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "fragen_level.json"), encoding="utf-8"))
except FileNotFoundError: LEVELS = {}

def parse_par(dirname, n):
    raw = open(os.path.join(dirname, n + ".txt"), encoding="utf-8").read().split("\n")
    # Stand (Inkrafttreten)
    stand = ""
    for i, l in enumerate(raw):
        if l.startswith("Inkrafttretensdatum") and i + 1 < len(raw):
            stand = raw[i + 1].strip(); break
    ti = raw.index("Text")
    body = raw[ti + 1:]
    # Paragraph-Zeile "§ N." suchen
    pi = next(i for i, l in enumerate(body) if re.fullmatch(r"§\s*%s\." % re.escape(n), l.strip()))
    title = body[pi - 1].strip()
    rest = body[pi + 1:]
    joined = "\n".join(rest)
    joined = re.split(r"Schlagworte\n|Zuletzt aktualisiert", joined)[0]
    for a, b in FIXES:
        if a in joined:
            joined = joined.replace(a, b); USED.add(a)
    for a, b in RFIXES:
        if re.search(a, joined):
            joined = re.sub(a, b, joined); USED.add(a)
    joined = re.sub(r"\s*…+\.?\s*\n?", ": ", joined)                 # Fristen-Tabelle (§ 10 Abs. 2): Punktlinien -> Doppelpunkt
    joined = re.sub(r"(?<=[a-zäöüß])\.(?=Z \d)", ".\n", joined)    # „…Zentralstelle.Z 1 und 2“
    text = pretty(joined)
    return title, stand, text

paras = []
for n in ORDER:
    if n in HAFTUNG:
        label, title, quellen = HAFTUNG[n]
        stands, parts = [], []
        for sub, par in quellen:
            t, st, tx = parse_par(os.path.join(src, sub), par)
            parts.append("§ %s. %s\n%s" % (par, t, tx)); stands.append(st)
        stand, text = max(stands), "\n\n".join(parts)
    else:
        label, (title, stand, text) = "§ " + n, parse_par(src, n)
    qs = []
    for k, (ref, frage, stmts) in enumerate(FRAGEN.get(n, [])):
        if len(stmts) != 4: raise SystemExit("Frage %s-%d: genau 4 Aussagen nötig" % (n, k + 1))
        s = []
        for st in stmts:
            w = bool(st[1]); korr = st[2] if len(st) > 2 else ""
            if not ((w and not korr) or ((not w) and korr)): raise SystemExit("Frage %s-%d: falsche Aussagen brauchen eine Erklärung, richtige nicht: %s" % (n, k + 1, st[0][:40]))
            s.append({"t": st[0], "w": w, "k": korr})
        qs.append({"id": "bdg-%s-%d" % (n, k + 1), "ref": ref, "f": frage, "s": s, "lv": LEVELS.get("bdg-%s-%d" % (n, k + 1), 2)})
    for qid, fx in SKR.get(n, {}).get("fix", {}).items():   # Korrekturen an bestehenden Fragen (ID bleibt)
        q = next(q for q in qs if q["id"] == qid)
        for ai, d in fx.items():
            st = q["s"][int(ai) - 1]
            for key, val in d.items(): st[key] = val
            if st["w"]: st["k"] = ""
    for q in qs:
        if q["id"] in SKR.get(n, {}).get("exclude", []): q["x"] = 1
    for nq in SKR.get(n, {}).get("new", []):
        if len(nq["s"]) != 4: raise SystemExit("Skriptum-Frage in %s: genau 4 Aussagen nötig" % n)
        nid = "bdg-%s-%d" % (n, len(qs) + 1)
        qs.append({"id": nid, "ref": nq["ref"], "f": nq["f"], "s": [{"t": x["t"], "w": bool(x["w"]), "k": x["k"]} for x in nq["s"]], "lv": nq.get("lv", LEVELS.get(nid, 2))})
    paras.append({"n": n, "label": label, "title": title, "stand": stand, "text": text, "q": qs})

if sorted(sum([g[1] for g in GRUPPEN], [])) != sorted(ORDER): raise SystemExit("Gruppen und Paragrafenliste passen nicht zusammen")

data = {
  "gesetz": "BDG",
  "name": "Beamten-Dienstrechtsgesetz 1979",
  "quelle": "RIS – Bundesrecht konsolidiert (data.bka.gv.at, Gesetzesnummer 10008470)",
  "abgerufen": ABGERUFEN,
  "gruppen": [{"name": g[0], "paras": g[1]} for g in GRUPPEN],
  "paragrafen": paras,
}
os.makedirs(os.path.dirname(out), exist_ok=True)
json.dump(data, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
missing = [a for a,b in FIXES + RFIXES if a not in USED]
if missing: raise SystemExit("Korrektur ohne Treffer: %r" % (missing,))
print(len(paras), "Paragrafen,", sum(1 for p in paras for q in p["q"] if not q.get("x")), "Fragen im Pool,", sum(1 for p in paras for q in p["q"] if q.get("x")), "ausgeschlossen")
