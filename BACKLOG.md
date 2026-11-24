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
| 11 | 2026-11-24 | **Verweise auf andere Gesetze** in den Antwortmöglichkeiten (z. B. „§ 302 StGB“, „AVG“): Antippen öffnet ein Pop-up mit kurzer Beschreibung. Verweise mit dieser Funktion werden **strichliert unterstrichen**. | neu | Brainstorm offen (siehe unten). |

## Brainstorm zu Wunsch 11 (noch nicht umgesetzt)
- **Frage an den Nutzer:** „Strichliert unterstreichen, wenn die Funktion angewendet wird“ – gemeint ist vermutlich: jeder Verweis, der ein Pop-up hat, ist dauerhaft strichliert unterstrichen (zeigt, dass er antippbar ist). Oder erst nach dem Antippen?
- **Inhalt:** Die Kurzbeschreibungen müssen einmal von Hand (oder aus RIS) erstellt werden, am besten als eigene Datei `daten/verweise.json` (Kürzel → Titel, 1 bis 2 Sätze, Link zum RIS). Erst ermitteln, welche Verweise in den 56 Fragen überhaupt vorkommen.
- **Technik:** Verweise im Fragentext markieren (z. B. `{{StGB §302}}`), beim Anzeigen automatisch in antippbare Elemente umwandeln. Pop-up lokal und offline, keine Fremdserver.
- **Stolperstein:** Aussagen sind selbst antippbar (Ankreuzen). Antippen des Verweises darf die Aussage nicht an- oder abwählen (Klick abfangen).
- **Frage:** Pop-up schon vor der Antwort erlauben? Das verrät evtl. Lösungshinweise; Alternative: Beschreibung nur allgemein halten (was regelt das Gesetz), nie bewerten.
- **Später nützlich:** Dieselbe Verweis-Liste für künftige Gesetze (StGB, SPG, VStG) wiederverwenden.

## Umgesetzt
Wünsche 1 bis 8 am 2026-11-24 in einem Durchgang umgesetzt und getestet (Punktelogik bei allen 56 Fragen, Gruppen, Stacks, Teilen, QR, Link-Auswahl, Offline).

## Ideen für später (nicht beauftragt)
- StGB, SPG, VStG ergänzen.
- Wiederholungsintervalle (Spaced Repetition) statt „sicher = zuletzt 4 Punkte“.
- Strenger Prüfungsmodus (Zeitlimit, keine Erklärung während der Prüfung).
