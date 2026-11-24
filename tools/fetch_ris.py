# -*- coding: utf-8 -*-
"""Holt Paragrafentexte (aktuelle Fassung) aus dem RIS über die offizielle OGD-Schnittstelle und speichert sie als Textdateien.

Aufruf:  python3 -I fetch_ris.py <Gesetzesnummer> <Ausgabeordner> <Paragraf,Paragraf,...>
Beispiel (BDG 1979):  python3 -I fetch_ris.py 10008470 ./ris_bdg 4,10,11,20,43a
Danach:   python3 -I build_data.py ./ris_bdg ../daten/bdg.json

Netzwerk: data.bka.gv.at und ogd.ris.bka.gv.at müssen erreichbar sein (in der Cloud-Umgebung freischalten).
Die Gesetzesnummer steht in der RIS-Adresse (…Gesetzesnummer=10008470)."""
import json, re, subprocess, sys, html, os, datetime

def curl(u):
    return subprocess.run(["curl", "-s", "-m", "60", u], capture_output=True, text=True).stdout

def main():
    gesetz, out, paras = sys.argv[1], sys.argv[2], sys.argv[3].split(",")
    os.makedirs(out, exist_ok=True)
    heute = datetime.date.today().isoformat()
    for p in paras:
        u = ("https://data.bka.gv.at/ris/api/v2.6/Bundesrecht?Applikation=BrKons&Gesetzesnummer=%s"
             "&Abschnitt.Von=%s&Abschnitt.Bis=%s&Abschnitt.Typ=Paragraph&Fassung.FassungVom=%s&DokumenteProSeite=Fifty") % (gesetz, p, p, heute)
        try:
            d = json.loads(curl(u))
        except Exception as e:
            print(p, "FEHLER", e); continue
        refs = d["OgdSearchResult"]["OgdDocumentResults"].get("OgdDocumentReference") or []
        refs = refs if isinstance(refs, list) else [refs]
        for x in refs:
            b = x["Data"]["Metadaten"]["Bundesrecht"]["BrKons"]
            if b.get("ArtikelParagraphAnlage", "").replace(" ", "") != "§" + p:
                continue
            urls = x["Data"]["Dokumentliste"]["ContentReference"]["Urls"]["ContentUrl"]
            xml = [u2["Url"] for u2 in urls if u2["DataType"] == "Xml"][0]
            t = curl(xml)
            t = re.sub(r"<(script|style).*?</\1>", "", t, flags=re.S)
            t = re.sub(r"</(absatz|abs|gldsym|ueberschrift|li|p|erlaeut|div)>|<br\s*/?>", "\n", t)
            t = html.unescape(re.sub(r"<[^>]+>", "", t))
            t = re.sub(r"\n\s*\n+", "\n", t).strip()
            open(os.path.join(out, p + ".txt"), "w", encoding="utf-8").write(t)
            print(p, len(t), b.get("ArtikelParagraphAnlage"), "in Kraft seit", b.get("Inkrafttretensdatum"))
            break
        else:
            print(p, "NICHT GEFUNDEN")

if __name__ == "__main__":
    main()
