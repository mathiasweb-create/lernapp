# -*- coding: utf-8 -*-
"""Holt Paragrafentexte (aktuelle Fassung) aus dem RIS über die offizielle OGD-Schnittstelle und speichert sie als Textdateien.

Aufruf:  python3 -I fetch_ris.py <Gesetzesnummer> <Ausgabeordner> <Paragraf,Paragraf,...>
Beispiel (BDG 1979):  python3 -I fetch_ris.py 10008470 ./ris_bdg 4,10,11,20,43a
Danach:   python3 -I build_data.py ./ris_bdg ../daten/bdg.json

Schreibt je Paragraf <Paragraf>.txt und eine meta.json (Abrufdatum). Endet mit Fehlercode 1, wenn ein Paragraf fehlt.
Netzwerk: data.bka.gv.at und ogd.ris.bka.gv.at müssen erreichbar sein (in der Cloud-Umgebung freischalten).
Die Gesetzesnummer steht in der RIS-Adresse (…Gesetzesnummer=10008470)."""
import json, re, subprocess, sys, html, os, datetime

def curl(u):
    r = subprocess.run(["curl", "-sSf", "-m", "60", u], capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError("Abruf fehlgeschlagen (%s): %s" % (r.returncode, r.stderr.strip()[:200]))
    return r.stdout

def hole(gesetz, p, heute):
    u = ("https://data.bka.gv.at/ris/api/v2.6/Bundesrecht?Applikation=BrKons&Gesetzesnummer=%s"
         "&Abschnitt.Von=%s&Abschnitt.Bis=%s&Abschnitt.Typ=Paragraph&Fassung.FassungVom=%s&DokumenteProSeite=Fifty") % (gesetz, p, p, heute)
    d = json.loads(curl(u))
    refs = d["OgdSearchResult"]["OgdDocumentResults"].get("OgdDocumentReference") or []
    refs = refs if isinstance(refs, list) else [refs]
    for x in refs:
        b = x["Data"]["Metadaten"]["Bundesrecht"]["BrKons"]
        if b.get("ArtikelParagraphAnlage", "").replace(" ", "") != "§" + p:
            continue
        urls = x["Data"]["Dokumentliste"]["ContentReference"]["Urls"]["ContentUrl"]
        xml = [u2["Url"] for u2 in urls if u2["DataType"] == "Xml"]
        if not xml:
            raise RuntimeError("keine XML-Adresse")
        t = curl(xml[0])
        t = re.sub(r"<(script|style).*?</\1>", "", t, flags=re.S)
        t = re.sub(r"</(absatz|abs|gldsym|ueberschrift|li|p|erlaeut|div)>|<br\s*/?>", "\n", t)
        t = html.unescape(re.sub(r"<[^>]+>", "", t))
        t = re.sub(r"\n\s*\n+", "\n", t).strip()
        if len(t) < 200 or "\nText\n" not in "\n" + t + "\n":
            raise RuntimeError("Text zu kurz oder ohne Textteil (%d Zeichen)" % len(t))
        return t, b.get("Inkrafttretensdatum")
    raise RuntimeError("Paragraf nicht gefunden")

def main():
    if len(sys.argv) != 4:
        raise SystemExit(__doc__)
    gesetz, out, paras = sys.argv[1], sys.argv[2], [x.strip() for x in sys.argv[3].split(",") if x.strip()]
    os.makedirs(out, exist_ok=True)
    heute = datetime.date.today().isoformat()
    fehler = []
    for p in paras:
        try:
            t, ab = hole(gesetz, p, heute)
        except Exception as e:
            fehler.append(p); print(p, "FEHLER:", e); continue
        open(os.path.join(out, p + ".txt"), "w", encoding="utf-8").write(t)
        print(p, len(t), "Zeichen, in Kraft seit", ab)
    json.dump({"abgerufen": heute, "gesetzesnummer": gesetz}, open(os.path.join(out, "meta.json"), "w", encoding="utf-8"))
    if fehler:
        print("Nicht geholt:", ", ".join(fehler)); sys.exit(1)

if __name__ == "__main__":
    main()
