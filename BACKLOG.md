# Änderungswünsche (Backlog)

**Regeln**
1. Wünsche hier nur **sammeln**. Nichts wird umgesetzt, bevor es ausdrücklich verlangt wird.
2. Vor jeder Umsetzung gibt es ein **Brainstorm**: Verbesserungen, Risiken, Fehler, einfachere Alternativen.
3. Erst nach dem Kommando „umsetzen“ (für einzelne Punkte oder alle) wird gebaut, getestet und gepusht.

**Status:** `neu` → `besprochen` → `freigegeben` → `umgesetzt`

## Wünsche

| Nr | Datum | Wunsch | Status | Notizen |
|----|-------|--------|--------|---------|
| 1 | 2026-11-24 | **Konkrete Fragestellungen** statt „Welche Aussagen sind richtig?“. Konkrete Frage + passende Antwortoptionen, **nie sehr kurze Antworten**. | umgesetzt | Alle 56 Fragen neu formuliert, Fragestellung im Kasten. |
| 2 | 2026-11-24 | **Punktesystem:** max. 4 Punkte je Frage; −1 je falsch angekreuzter oder falsch ausgelassener Aussage (Variante a, Minimum 0). Anzeige: bei Fragen nur Punktezahl, in der Gesamtwertung Prozent und Punktezahl. | umgesetzt | Fortschritt neu gestartet (Schlüssel `rt.hist2`), „sicher“ = 4 Punkte. |
| 3 | 2026-11-24 | **Falschaussagen:** nur gelegentlich durch Änderung eines einzelnen Wortes, überwiegend inhaltlich plausibel falsch. | umgesetzt | Überwiegend inhaltlich plausible Falschaussagen (Verwechslung, falsche Rechtsfolge), nur noch vereinzelt Zahlen- oder Wortwechsel. |
| 4 | 2026-11-24 | **Kurze Erklärung bei falschen Aussagen** (1 bis 2 Sätze, mit Fundstelle). | umgesetzt | Erscheint nach der Antwort bei jeder falschen Aussage. |
| 5 | 2026-11-24 | **Stil A (Klar):** Fragestellung im Kasten, mehr Farbe, Tab-Leiste (Lernen · Stacks · Statistik). | umgesetzt | Hell und Dunkel, fünf Themenfarben. |
| 6 | 2026-11-24 | **Gruppierte Paragrafenauswahl** (aufklappbare Kästen je Themenfeld). | umgesetzt | Gruppen ab 10 Paragrafen, Schnellwahl je Gruppe, offene Gruppen werden gemerkt, Suchfeld ab 30 Paragrafen. |
| 7 | 2026-11-24 | **Teilen-Button:** Link der App teilen und versenden. | umgesetzt | Teilen-Menü des iPhones, Kopieren, QR-Code (lokal eingebunden). |
| 8 | 2026-11-24 | **Stack teilen:** Link enthält die Paragrafenauswahl. | umgesetzt | Format `#BDG:4,10,43a`, nur Auswahl, nie Fortschritt; ungültige Angaben werden abgefangen. |
| 9 | 2026-11-24 | **Nur der Eigentümer darf die App verändern.** | offen (Aufgabe des Eigentümers) | GitHub-Einstellungen: Zwei-Faktor-Anmeldung, keine Mitwirkenden, Regel für `main` (Pull Request verlangen, Force-Push und Löschen blockieren). Code bleibt öffentlich. |
| 10 | 2026-11-24 | **Apps trennen:** Die Foto-Text-App hat nichts mit dem Rechtstrainer zu tun und soll separat liegen. | umgesetzt (2026-11-24) | Eigenes öffentliches Repo `lernapp` mit vollem Verlauf, die App liegt im Repo-Wurzelordner. Neue Adresse `https://mathiasweb-create.github.io/lernapp/`. Im alten Repo wird `lernapp/` entfernt. Jetzt günstig, da noch keine Links verteilt sind. |
| 11 | 2026-11-24 | **Verweise auf andere Gesetze und Paragrafen** in den Antwortmöglichkeiten (z. B. „§ 302 StGB“, „AVG“, „§ 43 BDG“): Antippen öffnet ein Pop-up mit kurzer Beschreibung. Verweise mit dieser Funktion sind **dauerhaft strichliert unterstrichen**. Pop-up auch **vor** der Antwort. | besprochen | Entscheidungen vom Nutzer: dauerhaft unterstrichen, Pop-up vor der Antwort erlaubt, gilt auch für Verweise auf andere Paragrafen. |
| 12 | 2026-11-24 | **Ergebnis in Prozent** und die **maximal erreichbare Punktezahl** angeben. Es gibt einen **Notenschlüssel**. | neu | Siehe Brainstorm. |
| 13 | 2026-11-24 | **Einstellungen-Button** (allgemeine Einstellungen). Dort u. a. **Notenschlüssel individuell anpassen**, Noten 1 bis 5 (sehr gut bis nicht genügend). | neu | Siehe Brainstorm. |
| 14 | 2026-11-24 | **Easter Egg:** Bei 100 Prozent kleines Fenster, das zum „besten Beamten des Tages“ gratuliert und fragt, ob die Person überhaupt Freizeit hat oder nur lernt. | neu | Siehe Brainstorm. |
| 15 | 2026-11-24 | **Prüfen:** (a) GitHub Pages für `lernapp`, (b) Alt-Repo bereinigt (PR #3). | erledigt (Prüfung) | (a) Veröffentlichung läuft: letzte Bereitstellung 2026-11-24 23:04 UTC, Status „success“ (Commit `2069b17`). (b) **Noch nicht erledigt:** `main` im Alt-Repo `foto-text-zu-word` enthält `lernapp/` weiterhin vollständig. Der dortige Merge von PR #3 entfernt den Ordner offenbar nicht, oder es ist ein früherer PR #3. Nutzer bitte in GitHub nachsehen (PR-Liste im Alt-Repo), ggf. neuen Aufräum-PR anfordern. |
| 16 | 2026-11-24 | **Historie** der Ergebnisse von Klausuren: gespeichert und einsehbar. | besprochen | Entschieden: gespeichert wird nur eine bewusst gestartete Klausur. | Siehe Brainstorm. |
| 17 | 2026-11-24 | **Umbenennen:** „Prüfungs-Stack“ wird zu **„Klausur“**. | besprochen | Entschieden: einheitlich umbenennen, also auch der Tab „Stacks“ wird „Klausuren“. Betrifft Beschriftungen in der App, README und Teilen-Text. Technisch (Stack-Link `#BDG:…`) bleibt alles gleich. |

## Brainstorm zu Wunsch 11 (noch nicht umgesetzt)
- Entschieden: dauerhaft strichliert, Pop-up auch vor der Antwort, auch Verweise auf andere Paragrafen. Bei Verweisen innerhalb des BDG zeigt das Pop-up die Überschrift und 1 bis 2 Sätze Kurzinhalt aus den vorhandenen Paragrafen-Daten (nur beschreibend, keine Wertung).
- **Inhalt:** Die Kurzbeschreibungen müssen einmal von Hand (oder aus RIS) erstellt werden, am besten als eigene Datei `daten/verweise.json` (Kürzel → Titel, 1 bis 2 Sätze, Link zum RIS). Erst ermitteln, welche Verweise in den 56 Fragen überhaupt vorkommen.
- **Technik:** Verweise im Fragentext markieren (z. B. `{{StGB §302}}`), beim Anzeigen automatisch in antippbare Elemente umwandeln. Pop-up lokal und offline, keine Fremdserver.
- **Stolperstein:** Aussagen sind selbst antippbar (Ankreuzen). Antippen des Verweises darf die Aussage nicht an- oder abwählen (Klick abfangen).
- **Frage:** Pop-up schon vor der Antwort erlauben? Das verrät evtl. Lösungshinweise; Alternative: Beschreibung nur allgemein halten (was regelt das Gesetz), nie bewerten.
- **Später nützlich:** Dieselbe Verweis-Liste für künftige Gesetze (StGB, SPG, VStG) wiederverwenden.

## Brainstorm zu Wunsch 12 bis 17 (noch nicht umgesetzt)
- **Notenschlüssel, Vorschlag (Frage an den Nutzer):** Üblich in Österreich: 1 ab 87,5 %, 2 ab 75 %, 3 ab 62,5 %, 4 ab 50 %, sonst 5. Passt das oder gilt ein anderer Schlüssel (z. B. 91/80/66/50)? Der Schlüssel wird in den Einstellungen (Wunsch 13) änderbar, vier Grenzwerte in Prozent.
- **Ergebnisanzeige:** „37 von 56 Punkten · 66 % · Note 3“. Maximalpunkte = 4 × Fragenzahl. Auch bei Zwischenständen die Maximalzahl nennen („Bisher 12 von 16“).
- **Einstellungen:** Zahnrad-Symbol oben rechts, öffnet Blatt. Inhalt zunächst nur Notenschlüssel mit Zurücksetzen. Prüfung der Eingabe: Grenzen müssen absteigend sein und zwischen 1 und 100 liegen. Speicherung lokal. Später möglich: Hell/Dunkel, Fortschritt zurücksetzen.
- **Note in der Historie (Wunsch 16):** Note zum Zeitpunkt der Klausur mit speichern, damit eine spätere Änderung des Schlüssels alte Ergebnisse nicht verfälscht. Alternativ neu berechnen, beides sinnvoll: Vorschlag fest speichern.
- **Historie:** Pro abgeschlossener Klausur ein Eintrag (Datum, Name, Paragrafen, Punkte, Maximum, Prozent, Note). Ansicht im Tab „Statistik“ als Liste, neueste zuerst, Verlauf pro Klausur. Frage: Zählt jeder Lerndurchlauf oder nur ein bewusst gestarteter Klausur-Durchlauf? Vorschlag: nur Durchläufe, die über eine gespeicherte Klausur gestartet wurden. Risiko: Daten liegen nur im Browser, gehen bei Löschen oder neuem Home-Bildschirm-Eintrag verloren; später Export/Import als Datei.
- **Easter Egg:** Nur bei exakt 100 % und nur am Ende eines Durchlaufs, ab mindestens 5 Fragen (sonst zu leicht). Kleines Fenster mit Schließen-Knopf, Text im Ton eines Augenzwinkerns, höchstens einmal pro Durchlauf. Nicht in der Historie sichtbar machen.
- **Umbenennen:** Auch „Stack“ allgemein im Tab? Vorschlag: Tab „Stacks“ bleibt zunächst, Abschnitt „Prüfungs-Stacks“ wird „Klausuren“. Einheitlichkeit prüfen (Tab-Name ebenfalls „Klausuren“?).
- **Reihenfolge-Vorschlag:** 17, 12, 13 (Basis), danach 16, 11, zuletzt 14.

## Umgesetzt
Wünsche 1 bis 8 am 2026-11-24 in einem Durchgang umgesetzt und getestet (Punktelogik bei allen 56 Fragen, Gruppen, Stacks, Teilen, QR, Link-Auswahl, Offline).

## Ideen für später (nicht beauftragt)
- StGB, SPG, VStG ergänzen.
- Wiederholungsintervalle (Spaced Repetition) statt „sicher = zuletzt 4 Punkte“.
- Strenger Prüfungsmodus (Zeitlimit, keine Erklärung während der Prüfung).
