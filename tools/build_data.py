# -*- coding: utf-8 -*-
"""Baut daten/bdg.json aus den RIS-Rohtexten (XML-Fassung, bereits zu Text gewandelt) und den Fragen.
Aufruf: python3 -I build_data.py <ordner_mit_N.txt> <ausgabe.json>
"""
import json, re, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from fragen_bdg import FRAGEN

ORDER = ["4","10","11","20","38","39","43","43a","44","46","49","53","56","65","76","94","112","131"]
src, out = sys.argv[1], sys.argv[2]

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

paras = []
for n in ORDER:
    raw = open(os.path.join(src, n + ".txt"), encoding="utf-8").read().split("\n")
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
    qs = []
    for k, (ref, frage, stmts) in enumerate(FRAGEN[n]):
        assert len(stmts) == 4, (n, k)
        s = []
        for st in stmts:
            w = bool(st[1]); korr = st[2] if len(st) > 2 else ""
            assert (w and not korr) or ((not w) and korr), (n, k, st[0][:40])
            s.append({"t": st[0], "w": w, "k": korr})
        qs.append({"id": "bdg-%s-%d" % (n, k + 1), "ref": ref, "f": frage, "s": s})
    paras.append({"n": n, "label": "§ " + n, "title": title, "stand": stand, "text": text, "q": qs})

GRUPPEN = [
  ("Dienstverhältnis", ["4","10","11","20"]),
  ("Versetzung & Zuteilung", ["38","39"]),
  ("Dienstpflichten", ["43","43a","44","46","49","53","56"]),
  ("Urlaub & Freistellung", ["65","76"]),
  ("Disziplinarrecht", ["94","112","131"]),
]
assert sorted(sum([g[1] for g in GRUPPEN], [])) == sorted(ORDER)

data = {
  "gesetz": "BDG",
  "name": "Beamten-Dienstrechtsgesetz 1979",
  "quelle": "RIS – Bundesrecht konsolidiert (data.bka.gv.at, Gesetzesnummer 10008470)",
  "abgerufen": "2026-11-24",
  "gruppen": [{"name": g[0], "paras": g[1]} for g in GRUPPEN],
  "paragrafen": paras,
}
os.makedirs(os.path.dirname(out), exist_ok=True)
json.dump(data, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
missing = [a for a,b in FIXES + RFIXES if a not in USED]
assert not missing, ("Korrektur ohne Treffer", missing)
print(len(paras), "Paragrafen,", sum(len(p["q"]) for p in paras), "Fragen")
