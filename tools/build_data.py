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
    text = pretty(joined)
    if n == "38":
        text += "\n(Die Tabelle zur Verwendungsgruppen-Zusammenfassung in Abs. 10 ist hier nicht abgebildet – siehe RIS.)"
    qs = []
    for k, (ref, stmts) in enumerate(FRAGEN[n]):
        assert len(stmts) == 4, (n, k)
        s = []
        for st in stmts:
            s.append({"t": st[0], "w": bool(st[1]), "k": (st[2] if len(st) > 2 else "")})
        qs.append({"id": "bdg-%s-%d" % (n, k + 1), "ref": ref, "s": s})
    paras.append({"n": n, "label": "§ " + n, "title": title, "stand": stand, "text": text, "q": qs})

data = {
  "gesetz": "BDG",
  "name": "Beamten-Dienstrechtsgesetz 1979",
  "quelle": "RIS – Bundesrecht konsolidiert (data.bka.gv.at, Gesetzesnummer 10008470)",
  "abgerufen": "2026-11-24",
  "paragrafen": paras,
}
os.makedirs(os.path.dirname(out), exist_ok=True)
json.dump(data, open(out, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(paras), "Paragrafen,", sum(len(p["q"]) for p in paras), "Fragen")
