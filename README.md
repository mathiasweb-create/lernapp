# Rechtstrainer (PWA)

Multiple-Choice-Training für Gesetzestexte. Läuft im Browser, lässt sich auf dem iPhone-Home-Bildschirm installieren und funktioniert danach offline.

## Auf dem iPhone installieren
1. Die Seite in **Safari** öffnen (`…/lernapp/`).
2. Teilen-Symbol → **Zum Home-Bildschirm**.
3. Fertig – die App öffnet sich im Vollbild.

## Punkte pro Frage (je 4 Aussagen, 0 bis 4 richtig möglich)
- +1 für jede richtig angekreuzte Aussage, −1 für jede fälschlich angekreuzte, Minimum 0.
- Ist keine Aussage richtig: nichts ankreuzen = 1 Punkt.

## Inhalt
- `daten/bdg.json` – BDG 1979, §§ 4, 10, 11, 20, 38, 39, 43, 43a, 44, 46, 49, 53, 56, 65, 76, 94, 112, 131 (Gesetzestext aus dem RIS, 56 Fragen).
- `tools/fragen_bdg.py` – Fragen (Quelltext). `tools/build_data.py` baut daraus die JSON-Datei.
- StGB, SPG, VStG: in der App als „bald“ vorgesehen.

## Neues Gesetz / neue Paragrafen ergänzen
1. Texte aus dem RIS holen (offizielle Schnittstelle `data.bka.gv.at/ris/api/v2.6`, Gesetzesnummer des Gesetzes).
2. Fragen in einer neuen `fragen_<gesetz>.py` schreiben, `build_data.py` entsprechend aufrufen.
3. Gesetz in `index.html` (`LAWS`) auf `ready:true` setzen, Datei in `sw.js` (`ASSETS`) aufnehmen und `VERSION` erhöhen.

Hinweis: Die Fragen wurden von einer KI aus dem Wortlaut erstellt und können Fehler enthalten. Keine Rechtsberatung.
