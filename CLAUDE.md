# Übergabe: Rechtstrainer (Lern-App)

Diese Datei liest ein neues Chat-Fenster zuerst. Sie ersetzt das Gedächtnis des alten Fensters. Aktuell halten, wenn sich etwas Wichtiges ändert.

## Worum es geht
iPhone-taugliche Lern-App (PWA) mit Multiple-Choice-Fragen zu österreichischen Gesetzen. Gewählte Paragrafen werden abgefragt, 4 Aussagen je Frage (0 bis 4 richtig), Punkte 0 bis 4. Erstes Gesetz: BDG 1979 (18 Paragrafen, 56 Fragen). Später StGB, SPG, VStG. Die App soll auch andere iPhone-Nutzer per Link erreichen.
Eigentümer: GitHub-Konto `mathiasweb-create`. Repo: `lernapp` (eigenes Repo, App im Wurzelordner). Live (GitHub Pages): `https://mathiasweb-create.github.io/lernapp/`.
Die App wurde am 2026-11-24 aus dem Repo `foto-text-zu-word` (Foto-Text-App, unabhängig) herausgelöst (Wunsch 10, Verlauf erhalten).

## Arbeitsregeln des Nutzers (immer einhalten)
- Antworten auf Deutsch, einfache Sprache, kurz. Bei Sprach- oder Diktatmodus nur das Nötigste.
- Anweisungen kritisch prüfen (falsche Angaben, Widersprüche, einfachere Wege) und beratend mitdenken, bewährte Workflows nennen.
- Grafiken: modern, nüchtern, kompakt, einfach, übersichtlich.
- **Änderungswünsche zuerst nur im `BACKLOG.md` sammeln.** Vor jeder Umsetzung ein Brainstorm (Verbesserungen, Fehler). Gebaut wird erst nach dem ausdrücklichen Kommando „umsetzen“.
- Nach Änderungen: testen, committen, auf den Entwicklungsbranch pushen. Pull Request erstellen oder mergen nur, wenn der Nutzer es verlangt.
- **Stand in dieser Datei immer vor einer Verdichtung des Kontexts aktualisieren** (Wunsch des Nutzers; der Nutzer hat die automatische Verdichtung auf etwa die Hälfte des Fensters, 500k Token, gestellt). Konkret: nach jedem Meilenstein (Merge, Push, abgeschlossene Prüfung) den Abschnitt „Stand“ erneuern und pushen, nicht erst kurz vor Schluss. Den genauen Füllstand kann der Assistent nicht messen.
- **Genehmigung per Auswahlknopf:** Bei jedem offenen Pull Request danach mit dem Fragewerkzeug (AskUserQuestion) „Jetzt genehmigen und mergen / Später“ anbieten. Ein Klick auf „Jetzt genehmigen“ gilt als Zustimmung zum Merge; danach Bereitstellung prüfen.
- **Genehmigung per Auswahlknopf:** Bei jedem offenen Pull Request danach mit dem Fragewerkzeug (AskUserQuestion) „Jetzt genehmigen und mergen / Später“ anbieten. Ein Klick auf „Jetzt genehmigen“ gilt als Zustimmung zum Merge; danach Bereitstellung prüfen.
- **Selbstständig arbeiten:** Vorgänge (Pull Requests, Sitzungen, Zugriffe auf Repos) selbst erledigen und dafür die Genehmigung anfordern. Den Nutzer nicht auf Handarbeit verweisen, außer wenn es technisch nur er kann (z. B. Merge im Browser).
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
- `daten/verweise.json` – Kurzbeschreibungen der Verweise (Pop-up), aus RIS-Texten erstellt, `match` = exakter Text in den Aussagen.
- `daten/bdg.json` – erzeugt, nicht von Hand ändern. Quelle: `tools/fragen_bdg.py` (Fragen) und RIS-Texte.
- `tools/fetch_ris.py` holt Gesetzestexte, `tools/build_data.py` baut die JSON, `tools/make_icons.py` die Icons.
- `BACKLOG.md` – Wünsche und Stand. `README.md` – Bedienung und Ablauf.

## Befehle
```
python3 -I tools/fetch_ris.py 10008470 /tmp/ris_bdg 4,10,11,20,38,39,43,43a,44,46,49,53,56,65,76,94,112,131
python3 -I tools/build_data.py /tmp/ris_bdg daten/bdg.json
python3 -m http.server 8123      # lokal testen (im Repo-Wurzelordner), dann http://localhost:8123/ öffnen
```
Fragen-IDs `bdg-<§>-<Nr>` nie umnummern, neue Fragen hinten anhängen (sonst passt der Lernfortschritt nicht). Neue Dateien in `sw.js` (`ASSETS`) eintragen und `VERSION` erhöhen.

## Stolpersteine in der Cloud-Umgebung
- RIS-Texte nur über `data.bka.gv.at` und `ogd.ris.bka.gv.at` (Hosts in der Cloud-Umgebung freigeschaltet). Die RIS-Webseite blockt Bots.
- `sleep` im Vordergrund ist gesperrt. Lange zusammengesetzte Shell-Befehle werden manchmal pauschal abgelehnt: einzeln ausführen, Dateien mit dem Schreib-Werkzeug anlegen.
- `github.io` ist von der Umgebung aus nicht erreichbar (Live-Seite nur über die GitHub-API-Status oder den Nutzer prüfen).
- Playwright ist vorinstalliert (`NODE_PATH=$(npm root -g) node test.js`). Python-Pakete per `pip install` möglich.
- **Pull Requests:** Nur mit ausdrücklicher Zustimmung des Nutzers im Chat selbst per API mergen und danach die Bereitstellung prüfen (siehe Stand). Das Pages-Anfordern (`pages/builds`) und `pages` allgemein sind in der Umgebung gesperrt.
- Gesetzestexte nie mit `head -n -1` o. ä. beschneiden, sonst fehlt der letzte Absatz (so ging § 44 Abs. 3 beim Lesen verloren). Immer die ganze Datei lesen oder `daten/bdg.json` (Feld `text`) nutzen.
- Prüfen großer Mengen (alle Fragen gegen Gesetzestext, Code-Review) an stärkere Hilfsagenten delegieren (Modell Opus, nur lesen), Befunde danach selbst gegen den Gesetzestext gegenprüfen.

## Stand (2026-11-25)
- **Wünsche 1 bis 8, 10 bis 14, 16, 17 umgesetzt und gemergt** (PR #3, live per GitHub Pages bestätigt: Bereitstellung `74afe0a`, Status success). Verweis-Pop-ups, Prozent/Maximum/Note, Zahnrad mit Notenschlüssel (Standard 87,5/75/62,5/50), Easter Egg bei 100 % (ab 5 Fragen), Klausuren mit Start und Historie (nur vollständig beantwortete, bewusst gestartete Klausuren). „Stack“ heißt überall „Klausur“.
- **Apps getrennt, Alt-Repo bereinigt:** `lernapp/` ist aus `foto-text-zu-word` entfernt (PR #4, vom Nutzer gemergt). Pages für `lernapp` läuft.
- **Merge per API:** Entgegen früherer Erfahrung hat ein per API gemergter PR (#3) die Veröffentlichung ausgelöst. Mit ausdrücklicher Zustimmung des Nutzers im Chat darf der Assistent PRs selbst mergen und danach die Bereitstellung prüfen (`gh api repos/mathiasweb-create/lernapp/deployments`).
- **Rechte:** `.claude/settings.json` erlaubt `add_repo` ohne Rückfrage. Sitzungen für andere Repos mit `create_session` starten.
- **Noch offen:** Pop-up für Verweise auf Absätze („Abs. 1“), Export/Import der Historie (Daten liegen nur im Browser), Test auf echtem iPhone, Stichprobe der Fragen, Wunsch 9 (Aufgabe des Nutzers). Nächste mögliche Schritte: StGB/SPG/VStG, Wiederholungsintervalle.

## Verlauf (älter) – Stand 2026-11-24, ca. 23:05 UTC
- **Apps getrennt (Wunsch 10):** Dieses Repo `lernapp` enthält den vollen Verlauf der App samt allen Korrekturen aus beiden Prüfungen (Stand des früheren Pull Requests #3). Adresse künftig `https://mathiasweb-create.github.io/lernapp/`. Alte Adresse (`…/foto-text-zu-word/lernapp/`) wird nicht weiter gepflegt.
- **Noch zu tun vom Nutzer:** (1) Pages einschalten: Safari, Desktop-Ansicht, `https://github.com/mathiasweb-create/lernapp/settings/pages`, Source „Deploy from a branch“, `main`, `/ (root)`, Save (in der GitHub-App nicht möglich); (2) im alten Repo `foto-text-zu-word` den Pull Request #3 selbst mergen (entfernt `lernapp/` dort, Arbeits-Branch `claude/iphone-learning-app-quiz-mgk932`, letzter Commit `d5e5f53`); (3) App auf dem iPhone neu zum Home-Bildschirm hinzufügen (neuer Speicher).
- **Arbeitsort:** Dieses Repo liegt in der Cloud-Sitzung unter `/home/user/lernapp`. Entwicklungs-Branch in diesem Repo: `main` (Nutzer hat die Trennung ausdrücklich freigegeben). Künftige Änderungen: Branch, Pull Request, Nutzer mergt selbst.
- **Fachprüfung der Fragen und Code-Prüfung (Opus):** abgeschlossen und umgesetzt (siehe Verlauf). Tests: Playwright, lokaler Server im Wurzelordner, Klicks auf „Prüfen“/„Weiter“ mit mindestens 0,45 s Abstand.
- **Wünsche:** 1 bis 8 und 10 umgesetzt. 9 offen (Aufgabe des Nutzers: Zwei-Faktor-Anmeldung, keine Mitwirkenden, Regel für `main`).
- **Noch offen:** Test auf echtem iPhone, Stichprobe der Fragen. Organigramm (privat): https://claude.ai/artifact/DQNYxT7s9U4vBWsFMbtxK4
- **Nächste mögliche Schritte:** StGB/SPG/VStG ergänzen, Wiederholungsintervalle.
