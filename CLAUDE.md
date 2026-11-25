# Übergabe: LexCoach (Lern-App, früher „Rechtstrainer“)

Diese Datei liest ein neues Chat-Fenster zuerst. Sie ersetzt das Gedächtnis des alten Fensters. Aktuell halten, wenn sich etwas Wichtiges ändert.

## Worum es geht
iPhone-taugliche Lern-App (PWA) mit Multiple-Choice-Fragen zu österreichischen Gesetzen. Gewählte Paragrafen werden abgefragt, 4 Aussagen je Frage (0 bis 4 richtig), Punkte 0 bis 4. Erstes Gesetz: BDG 1979 (18 Paragrafen, 56 Fragen). Später StGB, SPG, VStG. Die App soll auch andere iPhone-Nutzer per Link erreichen.
Eigentümer: GitHub-Konto `mathiasweb-create` (Name im Impressum: Mathias Blanck). Repo: `lernapp` (öffentlich, App im Wurzelordner). Live (GitHub Pages, baut `main`): `https://mathiasweb-create.github.io/lernapp/`.
Die App wurde am 2026-11-24 aus dem Repo `foto-text-zu-word` (Foto-Text-App, unabhängig) herausgelöst. Das Repo `mathiasweb-create/Pruefungssimulation-` ist unbenutzt; das Löschen ist über die Umgebung nicht möglich (Proxy sperrt, HTTP 403), der Nutzer muss es selbst in GitHub löschen (Settings › Danger Zone).
Bedienbare Vorschau für neue Entwürfe (Artefakt, wird bei Änderungen aktualisiert): https://claude.ai/artifact/SWuLN8FVZr3e7g9jZyxNyH. Organigramm (privat): https://claude.ai/artifact/DQNYxT7s9U4vBWsFMbtxK4

## Arbeitsregeln des Nutzers (immer einhalten)
- Antworten auf Deutsch, einfache Sprache, kurz. Bei Sprach- oder Diktatmodus nur das Nötigste, nichts wiederholen. Fachbegriffe (Branch, Pull Request, Merge, Deployment) kurz erklären.
- Anweisungen kritisch prüfen (falsche Angaben, Widersprüche, einfachere Wege), beratend mitdenken, bewährte Workflows nennen, inhaltliche Rückfragen stellen (gern mit dem Fragewerkzeug und Auswahlknöpfen).
- Grafiken und Vorschauen: modern, nüchtern, kompakt, einfach, übersichtlich. **Vorschauen immer als bedienbares Artefakt** (Artifact-Tool), nicht als Datei.
- **Änderungswünsche zuerst nur im `BACKLOG.md` sammeln**, Brainstorm (Verbesserungen, Fehler, Risiken), gebaut wird erst nach dem Kommando „umsetzen“. Vor jeder Backlog-Anpassung den Code auf Richtigkeit prüfen (Tests laufen lassen).
- Nach Änderungen: testen, committen, auf den Entwicklungsbranch `claude/foto-text-zu-word-status-7vvwht` pushen. **Pull Requests anlegen und mergen nie selbstständig.** Vorher immer das Fragewerkzeug (`AskUserQuestion`) mit Auswahlknöpfen („Pull Request anlegen und mergen“ / „Noch nicht“) verwenden und auf den Klick warten (Nutzerwunsch 2026-11-25, gilt immer). Danach Bereitstellung prüfen.
- **Selbstständig arbeiten:** Vorgänge (Pull Requests, Sitzungen, Repo-Zugriffe) selbst erledigen und dafür die Genehmigung anfordern. Den Nutzer nicht auf Handarbeit verweisen, außer wenn es technisch nur er kann.
- **Hilfsagenten nach eigenem Ermessen** nutzen und dem Nutzer kurz auflisten, welcher Agent was erledigt. Prüfungen großer Mengen oder Code-Reviews an Opus-Agenten (nur lesen) geben, Befunde danach selbst gegenprüfen.
- **Stand in dieser Datei nach jedem Meilenstein aktualisieren** (Merge, Push, Prüfung), nicht erst kurz vor einer Kontext-Verdichtung.

## Entscheidungen (nicht erneut diskutieren)
- Technik: reine Web-App (HTML, JS, CSS), keine Frameworks, kein Server. Daten und Fortschritt nur lokal im Browser (`localStorage`). Keine Fremdserver-Skripte (QR-Generator liegt lokal in `vendor/`).
- Stil A (blau, Fragekasten, niedrige Tab-Leiste Start · Lernen · Klausuren · Statistik), Hell und Dunkel (auch per Einstellung), fünf Themenfarben.
- Punkte je Frage: je Aussage +1 (richtig angekreuzt oder richtig ausgelassen), −1 (falsch behandelt), Minimum 0, Maximum 4. „Sicher“ = 4 Punkte. Notenschlüssel Standard 87,5/75/62,5/50 %, einstellbar.
- Fragen: konkrete Fragestellung, Aussagen nie sehr kurz, Falschaussagen überwiegend inhaltlich plausibel, bei jeder falschen Aussage kurze Erklärung mit Fundstelle.
- Bei jedem Öffnen zuerst die **Startseite** (Lexi, Gesetze, Neuigkeiten, bei Link `#BDG:…` direkt Lernen). Lernen: nichts vorgewählt, Themen-Kästen, „Klausuren“ eingeklappt, Speichern und Entfernen dort. Reiter Klausuren nur Übersicht (Start, Teilen, Entfernen). Statistik mit Gesetz-Filter und eingeklapptem „Mehr“.
- Erster Start: Home-Bildschirm-Hinweis („Wird empfohlen, du Fuchs.“), dann Tutorial (6 Schritte, Hervorhebung echter Elemente, „Überspringen“ springt an andere Stelle und wirkt erst nach 2 bis 10 Klicks, „Abbrechen“ zeigt Lexi: „Keiner mag Klugscheißer.“).
- **Lexi** (Fuchs, Schal im Wind, Windkringel und Herbstblatt auf der Startseite, Comic-Sprechblasen mit Spitze zum Mund): bewegt sich nur bei neuer Frage (Hüpfer) und Ergebnis (Note 1: hüpft mit Konfetti, Note 5: Kopf hängen). Sprüche selten und dezent: Huggi Guggi · Den Truthahn würgen · Kollege Lenz · Willkommen im Kurs, Kollege Zorn · Maschinengewehr Gottes · Diesen Hier! (wütend, Mittelfinger verpixelt) · Hundsviech-Paragraf · Dann gehn ma sitzen (Gitter) · Meine Damen und Herren. Schalter „Sprüche von Lexi“ und „Bewegungen reduzieren“ in den Einstellungen.
- Rechtliches (Einstellungen): Impressum (Privatperson Mathias Blanck, E-Mail, Anschrift und Wohnort als schwarze Balken, Nutzerentscheidung, rechtlich fraglich), Datenschutz, Nutzung und Haftung, Quellen und Lizenzen. **In den Rechtstexten kein Hinweis auf KI-Erstellung**; der Hinweis im Seitenfuß der Lernen-Seite („von einer KI … erstellt“) bleibt. Nutzungsvorbehalt gegen KI-Auswertung (§ 42h Abs. 6 UrhG): `LICENSE`, `robots.txt`, Meta-Tags `noai`/`tdm-reservation`, Hinweis im Quelltext. Rechtsgrundlagen sind im RIS im Wortlaut geprüft.
- Repo bleibt öffentlich. Nur der Eigentümer verändert den Code (Wunsch 9, Aufgabe des Eigentümers: Zwei-Faktor, keine Mitwirkenden, Regel für `main`).

## Technischer Überblick
- `index.html`: App. Zustand `S` (Ansicht `S.view`: start, home, stacks, stats, quiz, result, settings; Unterseite `S.set`), Einstellungen `SET`, Aktionen per Event-Delegation (`ACT`, `data-act`). `render()` zeichnet die Ansicht, danach Sprechblasen (`LX.paintAll`) und Overlay (`renderOverlay`: Home-Bildschirm-Hinweis `S.pop`, Tutorial `S.tour`). Doppeltipp-Schutz: nach jedem Knopf aus `NAV` sind 450 ms lang alle Tipps gesperrt.
- `lexi.js` (Figur `Lexi.svg(mood, klassen)`, Sprechblasen `paint`, `say`, Idle-Sprüche), `lexi.css` (Animationen, Blasen, Tutorial, Einstellungen, Neuigkeiten), `legal.js` (Rechtstexte), `daten/news.json` (Neuigkeiten, von Hand aus den Bundesgesetzblättern im RIS, Paragrafen der App erscheinen blau), `daten/verweise.json` (Pop-up-Texte, `match` = exakter Text in Aussagen), `daten/bdg.json` (erzeugt, nicht von Hand ändern; Quelle `tools/fragen_bdg.py` und RIS), `sw.js` (Offline-Cache, Netz zuerst; neue Dateien in `ASSETS`, `VERSION` erhöhen, aktuell `rt-v9`), `manifest.webmanifest`, Icons, `vendor/qrcode.js` (MIT).
- `localStorage`-Schlüssel (Präfix `rt.` bleibt, damit Daten erhalten bleiben): `rt.law`, `rt.sel.<Gesetz>`, `rt.open.<Gesetz>`, `rt.onlyOpen`, `rt.hist2` (Fortschritt je Frage), `rt.stacks` (Klausuren), `rt.klausur` (Historie, max. 200), `rt.grades`, `rt.flags`, `rt.set` (lim, ord, theme, font, rm, says), `rt.a2hs`, `rt.tour`.
- Fragen-IDs `bdg-<§>-<Nr>` nie umnummern, neue Fragen hinten anhängen. Safari und Home-Bildschirm-App haben getrennten Speicher.
- `tools/`: `fetch_ris.py` (RIS-Texte, auch für andere Gesetze: `python3 -I tools/fetch_ris.py <Gesetzesnummer> <Ordner> <Paragrafen>`), `build_data.py`, `fragen_bdg.py`, `make_icons.py`, `test_app.js` (Playwright-Test der ganzen App).

## Befehle
```
python3 -I tools/fetch_ris.py 10008470 /tmp/ris_bdg 4,10,11,20,38,39,43,43a,44,46,49,53,56,65,76,94,112,131
python3 -I tools/build_data.py /tmp/ris_bdg daten/bdg.json
python3 -m http.server 8123      # Testserver im Repo-Ordner
NODE_PATH=$(npm root -g) timeout 280 node tools/test_app.js      # Test (Server muss laufen)
```

## Stolpersteine in der Cloud-Umgebung
- RIS nur über `data.bka.gv.at` (Suche) und `ogd.ris.bka.gv.at` (Dokumente, z. B. Bundesgesetzblatt als XML: `…/Dokumente/BgblAuth/BGBLA_2025_I_100/BGBLA_2025_I_100.xml`) erreichbar. Die RIS-Webseite blockt Bots, `github.io` ist nicht erreichbar (Live-Stand über `gh api repos/mathiasweb-create/lernapp/deployments` prüfen).
- `sleep` im Vordergrund ist gesperrt, stattdessen Schleife mit Zeitlimit oder Hintergrundaufgabe. Hintergrundaufgaben enden nach 30 Minuten, für längere `timeout` setzen (Testserver: 7200000). Lange zusammengesetzte Shell-Befehle (mehrere Dateien schreiben, Server starten, Tests) werden vom Berechtigungsprüfer manchmal pauschal abgelehnt: einzeln ausführen, Dateien mit Schreib- und Bearbeiten-Werkzeug ändern.
- Playwright ist vorinstalliert. Testskripte immer mit Zeitlimit (`timeout 120 node …`), keine Schleifen ohne Abbruch, Klicks auf Navigationsknöpfe mit mindestens 0,6 s Abstand (Doppeltipp-Schutz).
- GitHub: nur `gh api` (REST). Pull Request anlegen: `gh api -X POST repos/mathiasweb-create/lernapp/pulls -f title=… -f head=… -f base=main -f body=…`, mergen: `gh api -X PUT …/pulls/<N>/merge -f merge_method=merge`. Repo-Einstellungen, Pages-Anforderung und Repo-Löschen sind gesperrt. PR-Texte enden mit der Zeile „🤖 Generated with [Claude Code]…“ und der Sitzungs-URL.
- Gesetzestexte nie mit `head -n -1` o. ä. beschneiden. Immer die ganze Datei lesen oder `daten/bdg.json` (Feld `text`) nutzen.
- Der Arbeitsordner kann sich zwischen Sitzungen ändern (`/home/user/lernapp` oder `/home/user`); Scratchpad-Pfad steht im Systemhinweis.

## Stand (2026-11-25, abends)
- **Live auf `main`:** Wünsche 1 bis 8, 10 bis 14 und 16 bis 35 (PR #6 bis #11, Bereitstellung erfolgreich). **Neu im Backlog:** Wunsch 36 (Skripten als Themenvorgabe für den Fragenpool, noch offen). Playwright-Test und Code-Review (Opus) durch, Befunde behoben.
- **Noch offen:** Test auf echtem iPhone (Nutzer), Wohnort und Anschrift im Impressum (Balken, rechtlich fraglich) und rechtliche Prüfung der Texte, Pop-up für Verweise auf Absätze („Abs. 1“), Export/Import der Historie (Daten nur im Browser), Wunsch 9 (Aufgabe des Nutzers), Stichprobe der Fragen, Sprüche-Liste („Den Truthahn würgen“ ist derb, Nutzer hat nicht entschieden), `robots.txt` wirkt nur im Domain-Hauptverzeichnis (Nutzer lehnte Repo `mathiasweb-create.github.io` ab). Hinweis: Verweise stecken technisch in Knöpfen (Screenreader-Nachteil, war schon vorher so).
- **Nächste mögliche Schritte:** StGB/SPG/VStG ergänzen (Daten mit `tools/`, `LAWS` in `index.html` auf `ready:true`, `news.json` ergänzen), Wiederholungsintervalle, Export/Import der Historie, strenger Prüfungsmodus (Zeitlimit).

## Startsatz für einen neuen Chat
„Lies zuerst CLAUDE.md und BACKLOG.md im Repo mathiasweb-create/lernapp (Branch main), fasse den Stand in fünf Zeilen zusammen, halte dich an die Arbeitsregeln und warte auf meine Anweisung.“
