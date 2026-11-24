# Übergabe: Rechtstrainer (Lern-App)

Diese Datei liest ein neues Chat-Fenster zuerst. Sie ersetzt das Gedächtnis des alten Fensters. Aktuell halten, wenn sich etwas Wichtiges ändert.

## Worum es geht
iPhone-taugliche Lern-App (PWA) mit Multiple-Choice-Fragen zu österreichischen Gesetzen. Gewählte Paragrafen werden abgefragt, 4 Aussagen je Frage (0 bis 4 richtig), Punkte 0 bis 4. Erstes Gesetz: BDG 1979 (18 Paragrafen, 56 Fragen). Später StGB, SPG, VStG. Die App soll auch andere iPhone-Nutzer per Link erreichen.
Eigentümer: GitHub-Konto `mathiasweb-create`. Repo: `foto-text-zu-word` (Ordner `lernapp/`). Live (GitHub Pages): `https://mathiasweb-create.github.io/foto-text-zu-word/lernapp/`.
Der Ordner `lernapp/` gehört fachlich NICHT zur Foto-Text-App im Repo-Root. Eine Trennung in ein eigenes Repo ist als Wunsch 10 im Backlog.

## Arbeitsregeln des Nutzers (immer einhalten)
- Antworten auf Deutsch, einfache Sprache, kurz. Bei Sprach- oder Diktatmodus nur das Nötigste.
- Anweisungen kritisch prüfen (falsche Angaben, Widersprüche, einfachere Wege) und beratend mitdenken, bewährte Workflows nennen.
- Grafiken: modern, nüchtern, kompakt, einfach, übersichtlich.
- **Änderungswünsche zuerst nur im `BACKLOG.md` sammeln.** Vor jeder Umsetzung ein Brainstorm (Verbesserungen, Fehler). Gebaut wird erst nach dem ausdrücklichen Kommando „umsetzen“.
- Nach Änderungen: testen, committen, auf den Entwicklungsbranch pushen. Pull Request erstellen oder mergen nur, wenn der Nutzer es verlangt.
- Der Nutzer will sich an Fachbegriffe gewöhnen (implementieren, Branch, Pull Request, Merge, Deployment). Begriffe kurz erklären.

## Entscheidungen (nicht erneut diskutieren)
- Technik: reine Web-App (HTML, JS, CSS), keine Frameworks, kein Server. Daten und Fortschritt nur lokal im Browser (`localStorage`). Keine Fremdserver-Skripte (QR-Generator liegt lokal in `vendor/`).
- Stil A (blau, Fragekasten, Tab-Leiste Lernen · Stacks · Statistik), Hell und Dunkel, fünf Themenfarben.
- Punkte je Frage: je Aussage +1 (richtig angekreuzt oder richtig ausgelassen), −1 (falsch behandelt), Minimum 0, Maximum 4. Anzeige nur als Punktezahl, Gesamtwertung Prozent und Punktezahl. „Sicher“ = 4 Punkte.
- Fragen: konkrete Fragestellung, Aussagen nie sehr kurz, Falschaussagen überwiegend inhaltlich plausibel (nur gelegentlich ein Wort getauscht), bei jeder falschen Aussage kurze Erklärung mit Fundstelle.
- Paragrafen-Auswahl in aufklappbaren Themen-Kästen (ab 10 Paragrafen), Stacks speicher- und teilbar, Link `…/lernapp/#BDG:4,10,43a`.
- Repo bleibt öffentlich. Nur der Eigentümer verändert den Code (Wunsch 9, GitHub-Einstellungen, Aufgabe des Eigentümers).

## Dateien
- `index.html` – ganze App. `sw.js` – Offline-Cache (Netz zuerst). `manifest.webmanifest`, Icons.
- `daten/bdg.json` – erzeugt, nicht von Hand ändern. Quelle: `tools/fragen_bdg.py` (Fragen) und RIS-Texte.
- `tools/fetch_ris.py` holt Gesetzestexte, `tools/build_data.py` baut die JSON, `tools/make_icons.py` die Icons.
- `BACKLOG.md` – Wünsche und Stand. `README.md` – Bedienung und Ablauf.

## Befehle
```
python3 -I tools/fetch_ris.py 10008470 /tmp/ris_bdg 4,10,11,20,38,39,43,43a,44,46,49,53,56,65,76,94,112,131
python3 -I tools/build_data.py /tmp/ris_bdg daten/bdg.json
python3 -m http.server 8123      # lokal testen (im Repo-Root), dann …/lernapp/ öffnen
```
Fragen-IDs `bdg-<§>-<Nr>` nie umnummern, neue Fragen hinten anhängen (sonst passt der Lernfortschritt nicht). Neue Dateien in `sw.js` (`ASSETS`) eintragen und `VERSION` erhöhen.

## Stolpersteine in der Cloud-Umgebung
- RIS-Texte nur über `data.bka.gv.at` und `ogd.ris.bka.gv.at` (Hosts in der Umgebung „foto-text-zu-word“ freigeschaltet). Die RIS-Webseite blockt Bots.
- `sleep` im Vordergrund ist gesperrt. Lange zusammengesetzte Shell-Befehle werden manchmal pauschal abgelehnt: einzeln ausführen, Dateien mit dem Schreib-Werkzeug anlegen.
- `github.io` ist von der Umgebung aus nicht erreichbar (Live-Seite nur über die GitHub-API-Status oder den Nutzer prüfen).
- Playwright ist vorinstalliert (`NODE_PATH=$(npm root -g) node test.js`). Python-Pakete per `pip install` möglich.

## Stand (2026-11-24)
- Wünsche 1 bis 8 umgesetzt und auf `main` (Pull Requests #1 und #2). Wunsch 9 offen (Nutzer). Wunsch 10 (Apps trennen) in Besprechung.
- Offene Prüfungen: Test auf echtem iPhone, Stichprobe der Fragen gegen den Gesetzestext durch den Nutzer.
- Nächste mögliche Schritte: Apps trennen, StGB/SPG/VStG ergänzen, Wiederholungsintervalle.
