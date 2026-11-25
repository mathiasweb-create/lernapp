# LexCoach (PWA)

Multiple-Choice-Training für Gesetzestexte. Läuft im Browser, lässt sich auf dem iPhone-Home-Bildschirm installieren und funktioniert danach offline.

## Auf dem iPhone installieren
1. Die Seite in **Safari** öffnen (`https://mathiasweb-create.github.io/lernapp/`).
2. Teilen-Symbol → **Zum Home-Bildschirm**. Die App fragt beim ersten Öffnen selbst danach und zeigt die Schritte (auch unter Einstellungen › Zum Home-Bildschirm).

## Bedienung
- **Startseite:** Bei jedem Öffnen zuerst die Startseite mit Lexi (Maskottchen), den Gesetzen und den Neuigkeiten zum Gesetz (die zuletzt geänderten Paragrafen, Antippen öffnet das ganze Gesetz im RIS; Quelle `daten/news.json`). Titel „LexCoach“ antippen = zurück zur Startseite.
- **Erster Start:** Hinweis „Zum Home-Bildschirm?“ (einmalig), danach eine kurze Tour mit Überspringen und Abbrechen. Die Tour lässt sich unter Einstellungen › Tutorial wiederholen.
- **Lernen:** Paragrafen in Themen-Kästen wählen (Kasten antippen = öffnen, Feld links = ganze Gruppe wählen). Beim ersten Öffnen ist nichts gewählt. Start-Knopf zeigt die Fragenzahl.
- **Frage:** Konkrete Fragestellung im Kasten, 4 Aussagen, alle zutreffenden ankreuzen. Danach Auflösung mit Erklärung bei falschen Aussagen und dem Gesetzestext.
- **Klausuren:** Auswahl unter „Lernen“ (Abschnitt „Klausuren“, antippen zum Öffnen) unter einem Namen speichern, laden oder entfernen. Der Reiter „Klausuren“ ist die Übersicht: Start, Teilen, Entfernen. „Start“ beginnt eine Klausur mit allen Fragen der gespeicherten Paragrafen; das Ergebnis (Punkte, Prozent, Note) kommt in die **Historie** unter „Statistik“.
- **Verweise:** Strichliert unterstrichene Verweise auf andere Paragrafen oder Gesetze in den Aussagen antippen: ein kleines Fenster beschreibt kurz, worum es geht (Quelle `daten/verweise.json`).
- **Einstellungen (Zahnrad):** Notenschlüssel (Standard: Note 1 ab 87,5 %, 2 ab 75 %, 3 ab 62,5 %, 4 ab 50 %, darunter 5), Lernen (Fragen pro Durchlauf per Schieberegler, Reihenfolge, nur unsichere Fragen), Darstellung (Hell/Dunkel/System, Schriftgröße, Bewegungen reduzieren, Sprüche von Lexi), Zum Home-Bildschirm, Tutorial und Rechtliches (Impressum, Datenschutz, Nutzung und Haftung, Quellen und Lizenzen).
- **Lexi:** Der Fuchs begleitet die App. Er bewegt sich bei einer neuen Frage und beim Ergebnis (bei Note 1 hüpft er mit Konfetti) und sagt gelegentlich einen kurzen Spruch.
- **Statistik:** Lernstand je Themenfeld und Historie, Filter nach Gesetz, unter „Mehr“: Historie löschen, Fortschritt zurücksetzen, gemeldete Fragen kopieren.
- **Safari und Home-Bildschirm-App sind getrennt:** Auf dem iPhone haben Safari und die installierte App je einen eigenen Speicher. Klausuren, Historie, Fortschritt und eine über einen Link übernommene Auswahl gelten nur dort, wo sie angelegt wurden. Am besten Klausuren nur in der Home-Bildschirm-App anlegen.
- **Teilen** (Symbol oben rechts): App-Link per Teilen-Menü des iPhones, Link kopieren oder QR-Code. Optional mit Paragrafenauswahl: `…/lernapp/#BDG:4,10,43a`.

## Punkte pro Frage (immer 4 Aussagen, 0 bis 4 richtig möglich)
- Je Aussage +1 Punkt, wenn richtig behandelt (richtig angekreuzt oder richtig ausgelassen), −1 Punkt, wenn falsch behandelt (falsch angekreuzt oder falsch ausgelassen).
- Pro Frage mindestens 0, höchstens 4 Punkte. Anzeige bei der Frage nur als Punktezahl, in der Auswertung Prozent, Punktezahl mit Höchstpunktzahl und Note.
- „Sicher“ gilt eine Frage bei 4 Punkten (letztes Ergebnis).

## Inhalt
- `index.html` – App (Oberfläche, Logik). `lexi.js` und `lexi.css` – Maskottchen Lexi, Sprechblasen, Tutorial- und Einstellungs-Gestaltung. `legal.js` – Rechtstexte. `sw.js` – Offline-Cache (Netz zuerst, sonst Cache). `manifest.webmanifest`, Icons.
- `daten/news.json` – Neuigkeiten je Gesetz (geänderte Paragrafen aus den Bundesgesetzblättern im RIS, von Hand zusammengefasst, Stand im Feld `stand`). `LICENSE`, `robots.txt` – Nutzungsvorbehalt (Alle Rechte vorbehalten, KI-Crawler gesperrt).
- `daten/bdg.json` – BDG 1979, §§ 4, 10, 11, 20, 38, 39, 43, 43a, 44, 46, 49, 53, 56, 65, 76, 94, 112, 131 (Gesetzestext aus dem RIS, 56 Fragen).
- `tools/fetch_ris.py` – holt die Gesetzestexte aus dem RIS. `tools/fragen_bdg.py` – Fragen (Quelltext). `tools/build_data.py` baut daraus die JSON-Datei (Abrufdatum kommt aus `meta.json`). `tools/make_icons.py` – Icons.
- `vendor/qrcode.js` – QR-Generator „qrcode-generator“ von Kazuhiko Arase (MIT-Lizenz, Text in `vendor/qrcode.LICENSE`), lokal eingebunden, damit die App ohne Fremdserver läuft.
- `BACKLOG.md` – Änderungswünsche und Stand der Umsetzung.
- StGB, SPG, VStG: in der App als „bald“ vorgesehen.

## Änderungen veröffentlichen
Änderungen an Fragen oder App committen und nach `main` bringen (Pull Request mergen). GitHub Pages veröffentlicht nach ca. 1 Minute. Die App holt beim Öffnen immer die neueste Fassung und fällt offline auf den gespeicherten Stand zurück. Neue Dateien in `sw.js` (`ASSETS`) eintragen und `VERSION` erhöhen.
Gespeicherte Klausuren, Historie und der Lernfortschritt bleiben auf dem Gerät erhalten. Fragen-IDs (`bdg-<§>-<Nr>`) nicht umnummerieren: neue Fragen immer **hinten anhängen**, sonst passt der Fortschritt nicht mehr zur Frage.

## Neues Gesetz / neue Paragrafen ergänzen
1. Texte aus dem RIS holen (offizielle Schnittstelle `data.bka.gv.at/ris/api/v2.6`, Gesetzesnummer des Gesetzes).
2. Fragen in einer neuen `fragen_<gesetz>.py` schreiben (Fragestellung, 4 Aussagen, Erklärung bei falschen), `build_data.py` entsprechend aufrufen (Gruppen/Themenfelder dort festlegen).
3. Gesetz in `index.html` (`LAWS`) auf `ready:true` setzen, Datei in `sw.js` (`ASSETS`) aufnehmen und `VERSION` erhöhen.

Hinweis: Die Fragen wurden von einer KI aus dem Wortlaut erstellt und können Fehler enthalten. Keine Rechtsberatung. © 2026 Mathias Blanck, Alle Rechte vorbehalten (siehe `LICENSE`).
