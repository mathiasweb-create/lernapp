# -*- coding: utf-8 -*-
"""Fragen zum BDG 1979. Jede Frage: Fundstelle + 4 Aussagen (Text, richtig?, Korrektur bei falsch).
Alle Aussagen wurden gegen den RIS-Wortlaut formuliert. Fehlerhafte Fragen bitte in der App melden."""

T, F = True, False

FRAGEN = {
"4": [
 ("Abs. 1, 1b", [
  ("Bei Verwendungen gemäß § 42a ist die österreichische Staatsbürgerschaft ein allgemeines Ernennungserfordernis.", T),
  ("Bei sonstigen Verwendungen genügt statt der österreichischen Staatsbürgerschaft auch der unbeschränkte Zugang zum österreichischen Arbeitsmarkt.", T),
  ("Beim Eintritt in den Bundesdienst ist ein Lebensalter von mindestens 16 Jahren erforderlich.", F, "Erforderlich sind mindestens 18 Jahre (Abs. 1 Z 4)."),
  ("Das Erfordernis der vollen Handlungsfähigkeit kann auch im Einzelfall nie entfallen.", F, "Nach Abs. 1b kann es im Einzelfall entfallen, wenn die für die Verwendung erforderliche Handlungsfähigkeit vorliegt."),
 ]),
 ("Abs. 1a, 2, 3", [
  ("Die fachliche Eignung umfasst auch die Beherrschung der deutschen Sprache in Wort und Schrift.", T),
  ("Genügt für eine Verwendung die Beherrschung der deutschen Sprache in geringerem Umfang, ist sie in dem für diese Verwendung erforderlichen Ausmaß nachzuweisen.", T),
  ("Die Ernennungserfordernisse sind nur für die Ernennung, nicht aber für die Verleihung einer Planstelle zu erbringen.", F, "Sie sind auch für die Verleihung einer Planstelle gemäß § 2 Abs. 2 zu erbringen (Abs. 2)."),
  ("Von mehreren Bewerbern, die die Ernennungserfordernisse erfüllen, darf nur der ernannt werden, von dem aufgrund seiner persönlichen und fachlichen Eignung anzunehmen ist, dass er die Aufgaben in bestmöglicher Weise erfüllt.", T),
 ]),
 ("Abs. 1, 1b, 2", [
  ("Die besonderen Ernennungserfordernisse werden im Besonderen Teil und durch die Anlage 1 geregelt.", T),
  ("Die persönliche und fachliche Eignung bezieht sich auf die Aufgaben der vorgesehenen Verwendung.", T),
  ("Bei sonstigen Verwendungen sind stets die österreichische Staatsbürgerschaft und zusätzlich der unbeschränkte Arbeitsmarktzugang erforderlich.", F, "Es genügt eines von beiden („oder“, Abs. 1 Z 1 lit. b)."),
  ("Die volle Handlungsfähigkeit kann im Einzelfall entfallen, wenn die für die vorgesehene Verwendung erforderliche Handlungsfähigkeit vorliegt.", T),
 ]),
],
"10": [
 ("Abs. 1, 2", [
  ("Das Dienstverhältnis ist zunächst provisorisch.", T),
  ("Das provisorische Dienstverhältnis kann mit Bescheid gekündigt werden.", T),
  ("Die Kündigungsfrist beträgt während der ersten sechs Monate (Probezeit) zwei Kalendermonate.", F, "In der Probezeit beträgt sie 1 Kalendermonat."),
  ("Nach Vollendung des zweiten Dienstjahres beträgt die Kündigungsfrist drei Kalendermonate.", T),
 ]),
 ("Abs. 2, 3", [
  ("Während der Probezeit ist die Kündigung ohne Angabe von Gründen möglich.", T),
  ("Nach der Probezeit ist die Kündigung nur mit Angabe des Grundes möglich.", T),
  ("Die Kündigungsfrist hat mit Ablauf eines Kalendervierteljahres zu enden.", F, "Sie hat mit Ablauf eines Kalendermonates zu enden."),
  ("Die Bestimmungen über die Probezeit gelten nicht für den Beamten, der unmittelbar vor Beginn des Dienstverhältnisses mindestens ein Jahr in einem privatrechtlichen Dienstverhältnis zum Bund in gleichwertiger Verwendung zugebracht hat.", T),
 ]),
 ("Abs. 4, 5", [
  ("Bedarfsmangel ist ein Kündigungsgrund.", T),
  ("Unbefriedigender Arbeitserfolg ist ein Kündigungsgrund.", T),
  ("Wegen der Inanspruchnahme einer Pflegefreistellung nach § 76 darf nicht gekündigt werden.", T),
  ("Die in Abs. 4 genannten Kündigungsgründe sind abschließend aufgezählt.", F, "Die Kündigungsgründe sind „insbesondere“ genannt, also beispielhaft."),
 ]),
 ("Abs. 2, 3, 7", [
  ("Die Kündigungsfrist beträgt nach Ablauf der Probezeit drei Kalendermonate.", F, "Nach der Probezeit: 2 Kalendermonate; erst nach dem zweiten Dienstjahr 3."),
  ("Die Probezeit beträgt die ersten drei Monate des Dienstverhältnisses.", F, "Die Probezeit umfasst die ersten sechs Monate."),
  ("Die Kündigung während der Probezeit bedarf stets der Angabe eines Grundes.", F, "In der Probezeit ist die Kündigung ohne Angabe von Gründen möglich."),
  ("In den Fällen des Abs. 7 trägt die Beamtin oder der Beamte die Beweislast dafür, dass die Kündigung aus anderen Gründen erfolgt ist.", F, "Die Beweislast trägt der Dienstgeber."),
 ]),
],
"11": [
 ("Abs. 1", [
  ("Das Dienstverhältnis wird auf Antrag des Beamten definitiv, wenn er neben den Ernennungserfordernissen die Definitivstellungserfordernisse erfüllt und eine Dienstzeit von sechs Jahren im provisorischen Dienstverhältnis vollendet hat.", T),
  ("Der Eintritt der Definitivstellung ist mit Bescheid festzustellen.", T),
  ("Erforderlich ist eine Dienstzeit von vier Jahren im provisorischen Dienstverhältnis.", F, "Erforderlich sind sechs Jahre (vier Jahre betreffen nur den Dienstunfall nach Abs. 2)."),
  ("Die Definitivstellung tritt kraft Gesetzes ein, ein Antrag des Beamten ist nicht erforderlich.", F, "Die Definitivstellung erfolgt auf Antrag des Beamten."),
 ]),
 ("Abs. 2, 3, 4", [
  ("Die Definitivstellung wird durch eine Beeinträchtigung der persönlichen Eignung nicht gehindert, wenn diese aufgrund eines Dienstunfalles eingetreten ist, den der Beamte nach einer Dauer des provisorischen Dienstverhältnisses von vier Jahren erlitten hat.", T),
  ("In das provisorische Dienstverhältnis können bestimmte Vordienstzeiten eingerechnet werden, soweit sie zur Gänze als Vordienstzeiten auf das Besoldungsdienstalter angerechnet worden sind.", T),
  ("Zeiten einer nützlichen Berufstätigkeit nach § 12 Abs. 3 GehG können bis zum Höchstausmaß von drei Jahren eingerechnet werden.", F, "Das Höchstausmaß beträgt zwei Jahre (Abs. 3, Z 2 und 3)."),
  ("Bei der Einrechnung ist auf die bisherige Berufslaufbahn im Hinblick auf die vorgesehene Verwendung des Beamten Bedacht zu nehmen.", T),
 ]),
 ("Abs. 5", [
  ("Die Wirkung des Abs. 1 tritt während eines Disziplinarverfahrens und bis zu drei Monaten nach dessen rechtskräftigem Abschluss nicht ein.", T),
  ("Wird das Disziplinarverfahren eingestellt oder der Beamte freigesprochen, tritt die Wirkung des Abs. 1 rückwirkend ein.", T),
  ("Die Wirkung des Abs. 1 tritt bis zu sechs Monate nach rechtskräftigem Abschluss des Disziplinarverfahrens nicht ein.", F, "Es sind bis zu drei Monate."),
  ("Bei einem Schuldspruch ohne Strafe tritt die Wirkung des Abs. 1 jedenfalls automatisch rückwirkend ein.", F, "Es kann nur unter den Voraussetzungen der Z 1 bis 3 (geringe Schuld, keine/unbedeutende Folgen, keine dienstlichen Interessen entgegen) mit Bescheid festgestellt werden."),
 ]),
],
"20": [
 ("Abs. 1", [
  ("Das Dienstverhältnis wird unter anderem durch Austritt aufgelöst.", T),
  ("Das Dienstverhältnis wird unter anderem durch Kündigung des provisorischen Dienstverhältnisses aufgelöst.", T),
  ("Das Dienstverhältnis wird unter anderem durch Kündigung des definitiven Dienstverhältnisses aufgelöst.", F, "Das Gesetz nennt nur die Kündigung des provisorischen Dienstverhältnisses."),
  ("Das Dienstverhältnis wird durch Tod aufgelöst.", T),
 ]),
 ("Abs. 1 Z 3a, 4", [
  ("Eine rechtskräftige Verurteilung durch ein inländisches Gericht wegen eines ab dem 1. Jänner 2013 begangenen Vorsatzdelikts gemäß den §§ 92, 201 bis 217, 312 und 312a StGB löst das Dienstverhältnis auf.", T),
  ("Dasselbe gilt bei Verurteilung wegen jedes fahrlässig begangenen Delikts.", F, "Es muss ein Vorsatzdelikt der genannten Bestimmungen sein."),
  ("Der Amtsverlust gemäß § 27 Abs. 1 StGB löst das Dienstverhältnis auf.", T),
  ("Auch eine Verurteilung durch ein ausländisches Gericht löst das Dienstverhältnis nach Z 3a auf.", F, "Z 3a verlangt ein inländisches Gericht."),
 ]),
 ("Abs. 2", [
  ("Beim Beamten des Ruhestandes wird das Dienstverhältnis auch durch die Disziplinarstrafe des Verlustes aller aus dem Dienstverhältnis fließenden Rechte und Ansprüche aufgelöst.", T),
  ("Die Verurteilung wegen mit Vorsatz begangener strafbarer Handlungen kann zur Auflösung führen, wenn die verhängte Freiheitsstrafe ein Jahr übersteigt.", T),
  ("Die Auflösung tritt ein, wenn die nicht bedingt nachgesehene Freiheitsstrafe drei Monate übersteigt.", F, "Es sind sechs Monate."),
  ("Das Dienstverhältnis wird auch dann aufgelöst, wenn die Rechtsfolge bedingt nachgesehen wird.", F, "Es wird nicht aufgelöst, wenn die Rechtsfolge bedingt nachgesehen wird – es sei denn, die Nachsicht wird widerrufen."),
 ]),
 ("Abs. 3a, 3b", [
  ("Für die Dauer von sechs Monaten nach Auflösung des Dienstverhältnisses ist unter bestimmten Voraussetzungen die Tätigkeit für gewisse Rechtsträger untersagt.", T),
  ("Bei Zuwiderhandeln ist eine Konventionalstrafe in Höhe des Dreifachen des für den letzten Monat gebührenden Monatsbezuges zu leisten.", T),
  ("Der Anspruch auf Ersatz eines weiteren Schadens bleibt neben der Konventionalstrafe bestehen.", F, "Der Anspruch auf Erfüllung oder Ersatz eines weiteren Schadens ist ausgeschlossen."),
  ("Maßgeblich ist, ob die dienstlichen Entscheidungen im Zeitraum von 24 Monaten vor der Auflösung maßgeblichen Einfluss hatten.", F, "Der Zeitraum beträgt zwölf Monate."),
 ]),
 ("Abs. 4, 5", [
  ("Bei Auflösung nach Abs. 1 Z 1 bis 5 sind dem Bund die Ausbildungskosten zu ersetzen.", T),
  ("Der Ersatz der Ausbildungskosten reduziert sich pro vollendetem Monat des Dienstverhältnisses nach Beendigung der Ausbildung um ein Achtundvierzigstel.", T),
  ("Bei Pilotinnen und Piloten reduziert er sich pro Monat um ein Sechsundneunzigstel.", T),
  ("Der Anspruch auf Ersatz der Ausbildungskosten verjährt nach fünf Jahren ab der Auflösung.", F, "Er verjährt nach drei Jahren."),
 ]),
],
"38": [
 ("Abs. 1, 2", [
  ("Eine Versetzung liegt vor, wenn der Beamte einer anderen Dienststelle zur dauernden Dienstleistung zugewiesen wird.", T),
  ("Die Versetzung ist von Amts wegen zulässig, wenn ein wichtiges dienstliches Interesse daran besteht.", T),
  ("Während des provisorischen Dienstverhältnisses ist eine Versetzung auch ohne wichtiges dienstliches Interesse zulässig.", T),
  ("Eine Versetzung von Amts wegen ist stets nur mit Zustimmung des Beamten zulässig.", F, "Das Gesetz verlangt wichtiges dienstliches Interesse, keine Zustimmung."),
 ]),
 ("Abs. 3", [
  ("Ein wichtiges dienstliches Interesse liegt insbesondere bei Änderungen der Verwaltungsorganisation vor.", T),
  ("Ein wichtiges dienstliches Interesse liegt insbesondere bei der Auflassung von Arbeitsplätzen vor.", T),
  ("Ein wichtiges dienstliches Interesse liegt insbesondere vor, wenn der Beamte nach § 81 Abs. 1 Z 3 den zu erwartenden Arbeitserfolg nicht aufgewiesen hat.", T),
  ("Ein wichtiges dienstliches Interesse liegt immer vor, wenn über den Beamten rechtskräftig eine Disziplinarstrafe verhängt wurde – unabhängig von Art und Schwere der Dienstpflichtverletzung.", F, "Zusätzlich muss wegen Art und Schwere der Verletzung die Belassung in der Dienststelle nicht vertretbar erscheinen (Z 5)."),
 ]),
 ("Abs. 4, 5, 6", [
  ("Bei einer Versetzung an einen anderen Dienstort von Amts wegen sind die persönlichen, familiären und sozialen Verhältnisse des Beamten zu berücksichtigen.", T),
  ("Eine Versetzung in ein anderes Ressort bedarf bei sonstiger Nichtigkeit des Bescheids der Zustimmung der Leiterin oder des Leiters des anderen Ressorts.", T),
  ("Gegen die beabsichtigte Versetzung können binnen zwei Wochen nach Zustellung Einwendungen vorgebracht werden.", T),
  ("Werden innerhalb der Frist keine Einwendungen vorgebracht, gilt dies als Ablehnung der Versetzung.", F, "Es gilt als Zustimmung zur Versetzung."),
 ]),
 ("Abs. 7, 8", [
  ("Die Versetzung ist mit Bescheid zu verfügen.", T),
  ("Eine Beschwerde gegen diesen Bescheid hat keine aufschiebende Wirkung.", T),
  ("Der vom Beamten zuletzt innegehabte Arbeitsplatz darf bis zur Rechtskraft des Bescheides nicht auf Dauer besetzt werden.", T),
  ("Bei Versetzung an einen anderen Dienstort ist dem Beamten eine angemessene Übersiedlungsfrist zu gewähren.", T),
 ]),
],
"39": [
 ("Abs. 1, 2", [
  ("Eine Dienstzuteilung liegt vor, wenn der Beamte vorübergehend einer anderen Dienststelle zur Dienstleistung zugewiesen und mit Aufgaben eines in der Geschäftseinteilung vorgesehenen Arbeitsplatzes betraut wird.", T),
  ("Eine Dienstzuteilung ist nur aus dienstlichen Gründen zulässig.", T),
  ("Ohne schriftliche Zustimmung des Beamten darf sie höchstens für insgesamt 90 Tage in einem Kalenderjahr ausgesprochen werden.", T),
  ("Ohne schriftliche Zustimmung des Beamten darf sie höchstens für insgesamt 60 Tage in einem Kalenderjahr ausgesprochen werden.", F, "Es sind 90 Tage."),
 ]),
 ("Abs. 3, 4", [
  ("Über die Grenze hinaus ist die Dienstzuteilung ohne Zustimmung zulässig, wenn der Dienstbetrieb auf andere Weise nicht aufrechterhalten werden kann.", T),
  ("Über die Grenze hinaus ist sie ohne Zustimmung zulässig, wenn sie zum Zwecke einer Ausbildung erfolgt.", T),
  ("Über die Grenze hinaus ist sie ohne Zustimmung zulässig, wenn dem Beamten ein höherwertiger Arbeitsplatz zugewiesen wird.", F, "Dieser Fall ist nicht genannt; nur Dienstbetrieb und Ausbildung."),
  ("Bei einer Dienstzuteilung an einen anderen Dienstort ist außerdem auf die persönlichen, familiären und sozialen Verhältnisse Bedacht zu nehmen.", T),
 ]),
],
"43": [
 ("Abs. 1, 3", [
  ("Der Beamte hat seine dienstlichen Aufgaben unter Beachtung der geltenden Rechtsordnung treu, gewissenhaft, engagiert und unparteiisch zu besorgen.", T),
  ("Er hat sie mit den ihm zur Verfügung stehenden Mitteln aus eigenem zu besorgen.", T),
  ("Er hat Weisungen auch dann zu befolgen, wenn dies gegen die Rechtsordnung verstößt.", F, "Die Aufgaben sind unter Beachtung der geltenden Rechtsordnung zu besorgen."),
  ("Er hat die Parteien im Rahmen seiner dienstlichen Aufgaben zu unterstützen und zu informieren, soweit es mit den Interessen des Dienstes und dem Gebot der Unparteilichkeit vereinbar ist.", T),
 ]),
 ("Abs. 2, 4", [
  ("Das gesamte Verhalten ist darauf Bedacht zu nehmen, dass das Vertrauen der Allgemeinheit in die sachliche Wahrnehmung der dienstlichen Aufgaben erhalten bleibt.", T),
  ("Tatsächliche und vermeintliche Interessenkonflikte sind zu vermeiden, soweit dies zumutbar ist.", T),
  ("Ein Interessenkonflikt liegt nur vor, wenn die Aufgaben tatsächlich nicht unvoreingenommen wahrgenommen werden; ein bloßer Anschein genügt nicht.", F, "Auch der Anschein genügt (vermeintlicher Interessenkonflikt)."),
  ("Im Rahmen der dienstlichen Tätigkeit ist Diskriminierung aus Gründen des Geschlechts, der ethnischen Zugehörigkeit, der Religion, Weltanschauung, Behinderung, des Alters oder der sexuellen Orientierung verboten.", T),
 ]),
],
"43a": [
 ("§ 43a", [
  ("Vorgesetzte haben ihren Mitarbeiterinnen und Mitarbeitern mit Achtung zu begegnen.", T),
  ("Mitarbeiterinnen und Mitarbeiter haben ihren Vorgesetzten mit Achtung zu begegnen.", T),
  ("Beamtinnen und Beamte haben zu einem guten Funktionieren der dienstlichen Zusammenarbeit beizutragen.", T),
  ("Verboten sind nur Verhaltensweisen, die die menschliche Würde tatsächlich verletzen; eine bloße Absicht („bezwecken“) genügt nicht.", F, "Auch Verhaltensweisen, die dies bezwecken, oder sonst diskriminierende sind zu unterlassen."),
 ]),
 ("§ 43a", [
  ("Verhaltensweisen oder das Schaffen von Arbeitsbedingungen, die sonst diskriminierend sind, sind zu unterlassen.", T),
  ("Die Pflicht zum achtungsvollen Umgang besteht nur von Vorgesetzten gegenüber Mitarbeiterinnen und Mitarbeitern.", F, "Sie besteht in alle Richtungen: auch gegenüber Vorgesetzten und untereinander."),
  ("Die Pflicht gilt nur im Umgang mit Vorgesetzten, nicht gegenüber Kolleginnen und Kollegen.", F, "Sie gilt auch gegenüber Kolleginnen/Kollegen sowie Mitarbeiterinnen/Mitarbeitern."),
  ("Die Pflicht gilt im Umgang mit Vorgesetzten, Kolleginnen und Kollegen sowie Mitarbeiterinnen und Mitarbeitern.", T),
 ]),
],
"44": [
 ("Abs. 1, 2", [
  ("Der Beamte hat seine Vorgesetzten zu unterstützen und ihre Weisungen zu befolgen, soweit verfassungsgesetzlich nicht anderes bestimmt ist.", T),
  ("Vorgesetzter ist jeder Organwalter, der mit der Dienst- oder Fachaufsicht über den Beamten betraut ist.", T),
  ("Die Befolgung einer Weisung kann abgelehnt werden, wenn sie von einem unzuständigen Organ erteilt worden ist.", T),
  ("Die Befolgung kann abgelehnt werden, wenn sie gegen irgendeine Verwaltungsvorschrift verstoßen würde.", F, "Nur bei Verstoß gegen strafgesetzliche Vorschriften (oder unzuständigem Organ)."),
 ]),
 ("Abs. 1, 2", [
  ("Der Beamte kann die Befolgung einer Weisung ablehnen, wenn er sie für unzweckmäßig hält.", F, "Das Gesetz nennt nur unzuständiges Organ und Verstoß gegen strafgesetzliche Vorschriften."),
  ("Der Beamte kann die Befolgung ablehnen, wenn sie gegen strafgesetzliche Vorschriften verstoßen würde.", T),
  ("Vorgesetzter ist nur, wer Dienststellenleiter ist.", F, "Vorgesetzter ist jeder mit Dienst- oder Fachaufsicht betraute Organwalter."),
  ("Die Pflicht zur Befolgung besteht nur bei schriftlichen Weisungen.", F, "Eine Formvorschrift enthält § 44 nicht."),
 ]),
],
"46": [
 ("Abs. 1", [
  ("Der Beamte hat ausschließlich aus seiner amtlichen Tätigkeit bekannt gewordene Tatsachen geheim zu halten, soweit und solange dies erforderlich und verhältnismäßig ist.", T),
  ("Ein Geheimhaltungsgrund ist das Interesse der nationalen Sicherheit.", T),
  ("Ein Geheimhaltungsgrund ist die Vorbereitung einer Entscheidung.", T),
  ("Ein Geheimhaltungsgrund ist die Wahrung des Ansehens des Amtes.", F, "Dieser Grund steht nicht in der Aufzählung des Abs. 1."),
 ]),
 ("Abs. 2, 3, 4", [
  ("Die Pflicht zur Geheimhaltung besteht auch nach Beendigung des Dienstverhältnisses.", T),
  ("Lässt sich aus der Ladung erkennen, dass die Aussage der Geheimhaltung unterliegen könnte, hat der Beamte dies seiner Dienstbehörde zu melden, die über die Entbindung entscheidet.", T),
  ("Stellt sich die Geheimhaltungspflicht erst bei der Aussage heraus, hat der Beamte die Beantwortung weiterer Fragen zu verweigern.", T),
  ("In diesem Fall entscheidet die vernehmende Behörde selbst über die Entbindung von der Geheimhaltung.", F, "Sie hat die Entbindung zu beantragen; entscheiden muss die Dienstbehörde."),
 ]),
 ("Abs. 3, 5, 6", [
  ("Im Disziplinarverfahren ist weder die oder der Beschuldigte noch die Disziplinarbehörde noch die Disziplinaranwältin oder der Disziplinaranwalt zur Geheimhaltung verpflichtet.", T),
  ("Eine Meldung oder Hinweisgebung gemäß § 53a zweiter Satz unterliegt nicht der Pflicht zur Geheimhaltung.", T),
  ("Die Dienstbehörde kann die Entbindung unter der Voraussetzung aussprechen, dass die Öffentlichkeit von dem betroffenen Teil der Aussage ausgeschlossen wird.", T),
  ("Im Disziplinarverfahren ist die oder der Beschuldigte zur Geheimhaltung verpflichtet, die Disziplinarbehörde nicht.", F, "Weder Beschuldigte noch Behörde noch Disziplinaranwalt sind verpflichtet."),
 ]),
],
"49": [
 ("Abs. 1", [
  ("Der Beamte hat auf Anordnung über die im Dienstplan vorgeschriebenen Dienststunden hinaus Dienst zu versehen (Mehrdienstleistung).", T),
  ("Nicht angeordnete Mehrdienstleistungen sind gleichzuhalten, wenn der Beamte sie spätestens innerhalb einer Woche nach Erbringung schriftlich meldet (und die übrigen Voraussetzungen vorliegen).", T),
  ("Die schriftliche Meldung hat spätestens innerhalb eines Monats zu erfolgen.", F, "Die Frist beträgt eine Woche."),
  ("Nicht angeordnete Mehrdienstleistungen sind stets gleichgehalten, auch wenn die Notwendigkeit auf vom Beamten vermeidbare Umstände zurückgeht.", F, "Voraussetzung ist u. a., dass die Notwendigkeit nicht auf vermeidbare Umstände zurückgeht."),
 ]),
 ("Abs. 2, 3", [
  ("An Werktagen erbrachte Mehrdienstleistungen sind nach Möglichkeit im selben Kalendervierteljahr im Verhältnis 1 : 1 in Freizeit auszugleichen.", T),
  ("Mehrdienstleistungen an Sonn- und Feiertagen sind nicht durch Freizeit auszugleichen.", T),
  ("Werktags-Mehrdienstleistungen, die im Kalendervierteljahr nicht durch Freizeit ausgeglichen sind, gelten mit Ablauf des Kalendervierteljahres als Überstunden.", T),
  ("Mehrdienstleistungen außerhalb der Nachtzeit sind nach den Mehrdienstleistungen in der Nachtzeit auszugleichen.", F, "Sie sind vor jenen in der Nachtzeit auszugleichen."),
 ]),
 ("Abs. 4, 8", [
  ("Werktagsüberstunden sind je nach Anordnung im Verhältnis 1 : 1,5 in Freizeit auszugleichen.", T),
  ("Werktagsüberstunden können je nach Anordnung nach besoldungsrechtlichen Vorschriften abgegolten werden.", T),
  ("Werktagsüberstunden können im Verhältnis 1 : 1,5 in Freizeit ausgeglichen und zusätzlich abgegolten werden.", F, "Die Kombination lautet 1 : 1 in Freizeit und zusätzlich Abgeltung."),
  ("Ein Freizeitausgleich für Werktagsüberstunden ist bis zum Ende des sechsten auf das Kalendervierteljahr der Leistung folgenden Monats zulässig.", T),
 ]),
 ("Abs. 4, 6, 7, 9", [
  ("Die Nachtzeit im Sinne der Bestimmung ist 22.00 bis 6.00 Uhr.", T),
  ("Zeiten einer vom Beamten angestrebten Einarbeitung von Dienstzeit gelten jedenfalls nicht als Überstunden.", T),
  ("Zeitguthaben aus der gleitenden Dienstzeit gelten stets als Überstunden.", F, "Sie gelten nicht als Überstunden, soweit sie die Obergrenze des Gleitzeitdienstplans nicht übersteigen."),
  ("Dem Beamten ist bis zum Ende des auf das Kalendervierteljahr folgenden Kalendermonats mitzuteilen, welche Abgeltungsart auf welche Werktagsüberstunden angewendet wird.", T),
 ]),
],
"53": [
 ("Abs. 1, 1a, 1b", [
  ("Bei begründetem Verdacht einer von Amts wegen zu verfolgenden gerichtlich strafbaren Handlung, die den Wirkungsbereich der Dienststelle betrifft, ist dies unverzüglich dem Leiter der Dienststelle zu melden.", T),
  ("Keine Meldepflicht besteht, wenn die Meldung eine amtliche Tätigkeit beeinträchtigen würde, deren Wirksamkeit eines persönlichen Vertrauensverhältnisses bedarf.", T),
  ("Der Leiter der Dienststelle kann aus bestimmten Gründen abweichend eine Meldepflicht verfügen.", T),
  ("Die Meldung hat innerhalb einer Woche zu erfolgen.", F, "Die Meldung hat unverzüglich zu erfolgen."),
 ]),
 ("Abs. 2", [
  ("Eine Namensänderung ist der Dienstbehörde zu melden.", T),
  ("Eine Änderung des Wohnsitzes ist der Dienstbehörde zu melden.", T),
  ("Eine Standesveränderung ist der Dienstbehörde zu melden.", T),
  ("Eine Änderung der Konfession ist der Dienstbehörde zu melden.", F, "Dieser Fall ist in Abs. 2 nicht genannt."),
 ]),
 ("Abs. 1c, 1d, 2", [
  ("Ist eine Dienstverhinderung auf das Einwirken Dritter zurückzuführen, hat der Beamte dies unverzüglich der Dienstbehörde zu melden.", T),
  ("Auf Verlangen der Dienstbehörde hat er die für Ersatzansprüche erforderlichen Daten und Beweismittel bekanntzugeben.", T),
  ("Die Meldepflicht nach Abs. 1 gilt als erfüllt, wenn eine Meldung oder Hinweisgebung gemäß § 53a erfolgt ist.", T),
  ("Der Verlust einer für die Dienstausübung erforderlichen behördlichen Berechtigung (z. B. Lenkberechtigung) ist nicht zu melden.", F, "Er ist zu melden (Abs. 2 Z 5)."),
 ]),
],
"56": [
 ("Abs. 1, 2", [
  ("Nebenbeschäftigung ist jede Beschäftigung, die der Beamte außerhalb seines Dienstverhältnisses und einer allfälligen Nebentätigkeit ausübt.", T),
  ("Der Beamte darf keine Nebenbeschäftigung ausüben, die ihn an der Erfüllung seiner dienstlichen Aufgaben behindert.", T),
  ("Der Beamte darf keine Nebenbeschäftigung ausüben, die die Vermutung seiner Befangenheit hervorruft.", T),
  ("Nebenbeschäftigungen sind für Beamte generell verboten.", F, "Verboten sind nur Nebenbeschäftigungen nach Abs. 2."),
 ]),
 ("Abs. 3, 5", [
  ("Jede erwerbsmäßige Nebenbeschäftigung und jede Änderung ist der Dienstbehörde unverzüglich zu melden.", T),
  ("Eine Nebenbeschäftigung ist erwerbsmäßig, wenn sie die Schaffung von nennenswerten Einkünften in Geld- oder Güterform bezweckt.", T),
  ("Eine Tätigkeit im Vorstand oder Aufsichtsrat einer auf Gewinn gerichteten juristischen Person des privaten Rechts ist jedenfalls zu melden.", T),
  ("Erwerbsmäßig ist eine Nebenbeschäftigung nur, wenn sie tatsächlich Einkünfte erzielt; die bloße Absicht genügt nicht.", F, "Es genügt, dass sie die Schaffung nennenswerter Einkünfte bezweckt."),
 ]),
 ("Abs. 4, 6, 7", [
  ("Wer die Wochendienstzeit nach §§ 50a, 50b, 50e, 50f oder 50g herabgesetzt hat, darf eine erwerbsmäßige Nebenbeschäftigung nur mit Genehmigung der Dienstbehörde ausüben.", T),
  ("Dasselbe gilt für den Beamten im Karenzurlaub nach § 75c.", T),
  ("Eine unzulässige Nebenbeschäftigung ist von der Dienstbehörde unverzüglich mit schriftlicher Weisung zu untersagen.", T),
  ("Die Untersagung einer unzulässigen Nebenbeschäftigung erfolgt mit Bescheid.", F, "Sie erfolgt mit schriftlicher Weisung."),
 ]),
],
"65": [
 ("Abs. 1", [
  ("In jedem Kalenderjahr gebührt ein Erholungsurlaub im Ausmaß von 200 Stunden.", T),
  ("Das Urlaubsausmaß erhöht sich ab dem Kalenderjahr, in dem der 43. Geburtstag vor dem 1. Juli liegt, auf 240 Stunden.", T),
  ("Liegt der 43. Geburtstag nach dem 30. Juni, erhöht sich das Urlaubsausmaß ab dem darauf folgenden Kalenderjahr.", T),
  ("Das Urlaubsausmaß erhöht sich ab dem Kalenderjahr des 40. Geburtstags auf 240 Stunden.", F, "Maßgeblich ist der 43. Geburtstag."),
 ]),
 ("Abs. 2, 4", [
  ("Im Kalenderjahr der Begründung des Dienstverhältnisses beträgt das Urlaubsausmaß für jeden begonnenen Monat ein Zwölftel des jährlichen Ausmaßes.", T),
  ("Hat das Dienstverhältnis in diesem Kalenderjahr ununterbrochen sechs Monate gedauert, gebührt der volle Erholungsurlaub.", T),
  ("Teile von Stunden sind auf ganze Stunden abzurunden.", F, "Sie sind aufzurunden."),
  ("Bei einem verlängerten Dienstplan erhöht sich das Urlaubsausmaß entsprechend.", T),
 ]),
 ("Abs. 3", [
  ("Ging dem Dienstverhältnis unmittelbar ein Ausbildungs- oder Lehrverhältnis zum Bund voran, wird so vorgegangen, als hätte das Dienstverhältnis mit dem ersten Tag dieses Verhältnisses begonnen.", T),
  ("Der im vorangegangenen Ausbildungs- oder Lehrverhältnis verbrauchte Erholungsurlaub ist vom gesamten Urlaubsanspruch abzuziehen.", T),
  ("Der im vorangegangenen Ausbildungs- oder Lehrverhältnis verbrauchte Urlaub bleibt unberücksichtigt.", F, "Er ist abzuziehen."),
  ("Dies gilt auch für jedes unmittelbar vorangegangene Dienstverhältnis zu einem privaten Arbeitgeber.", F, "Abs. 3 betrifft nur Ausbildungs- oder Lehrverhältnisse zum Bund."),
 ]),
],
"76": [
 ("Abs. 1", [
  ("Anspruch auf Pflegefreistellung besteht bei notwendiger Pflege einer erkrankten oder verunglückten nahen Angehörigen.", T),
  ("Anspruch besteht auch bei notwendiger Pflege einer im gemeinsamen Haushalt lebenden erkrankten oder verunglückten Person.", T),
  ("Anspruch besteht bei Begleitung des erkrankten Kindes bei einem stationären Aufenthalt in einer Heil- und Pflegeanstalt, sofern das Kind das zehnte Lebensjahr noch nicht vollendet hat.", T),
  ("Die Altersgrenze für diese Begleitung bei stationärem Aufenthalt liegt beim zwölften Lebensjahr.", F, "Dort gilt das zehnte Lebensjahr (zwölftes Lebensjahr gilt in Abs. 4)."),
 ]),
 ("Abs. 2", [
  ("Als nahe Angehörige gelten der Ehegatte und Personen, die mit dem Beamten in gerader Linie verwandt sind.", T),
  ("Als nahe Angehörige gelten Geschwister.", T),
  ("Als nahe Angehörige gilt die Person, mit der der Beamte in Lebensgemeinschaft lebt.", T),
  ("Als nahe Angehörige gelten auch Onkel und Tanten.", F, "Sie sind in Abs. 2 nicht genannt."),
 ]),
 ("Abs. 3, 4", [
  ("Die Pflegefreistellung nach Abs. 1 darf im Kalenderjahr das Ausmaß der regelmäßigen Wochendienstzeit nicht übersteigen.", T),
  ("Darüber hinaus besteht Anspruch auf bis zu eine weitere Woche, wenn der Anspruch nach Abs. 1 verbraucht ist und das im gemeinsamen Haushalt lebende erkrankte Kind das zwölfte Lebensjahr noch nicht überschritten hat.", T),
  ("Die weitere Woche steht auch zu, wenn für das Kind erhöhte Familienbeihilfe gewährt wird.", T),
  ("Die weitere Woche steht zu, solange das Kind das 18. Lebensjahr noch nicht überschritten hat.", F, "Maßgeblich ist das zwölfte Lebensjahr (oder erhöhte Familienbeihilfe)."),
 ]),
 ("Abs. 7, 8, 9, 10", [
  ("Ist der Anspruch auf Pflegefreistellung erschöpft, kann zu einem in Abs. 4 genannten Zweck nicht verbrauchter Erholungsurlaub ohne vorherige kalendermäßige Festlegung nach § 68 angetreten werden.", T),
  ("Auch wer nicht mit dem erkrankten Kind im gemeinsamen Haushalt lebt, hat Anspruch nach Abs. 4 und 8.", T),
  ("Im vertraglichen Dienstverhältnis zum Bund bereits verbrauchte Pflegefreistellung ist anzurechnen.", T),
  ("Die Dauer einer Urlaubsunterbrechung gemäß § 71 Abs. 6 bleibt bei der Berechnung unberücksichtigt.", F, "Sie ist auf das Ausmaß nach Abs. 3 und 4 anzurechnen."),
 ]),
],
"94": [
 ("Abs. 1", [
  ("Nicht mehr bestraft werden darf, wenn nicht innerhalb von sechs Monaten ab Kenntnis der Disziplinarbehörde eine Disziplinarverfügung erlassen oder Anzeige an die Bundesdisziplinarbehörde erstattet wurde.", T),
  ("Nicht mehr bestraft werden darf, wenn nicht innerhalb von einem Jahr ab Kenntnis der Disziplinarbehörde ein Disziplinarverfahren vor der Bundesdisziplinarbehörde eingeleitet wurde.", T),
  ("Nicht mehr bestraft werden darf, wenn nicht innerhalb von drei Jahren ab Beendigung der Dienstpflichtverletzung eine Disziplinarverfügung erlassen oder ein Verfahren eingeleitet wurde.", T),
  ("Die dreijährige Frist läuft ab dem Zeitpunkt, zu dem die Disziplinarbehörde Kenntnis erlangt hat.", F, "Sie läuft ab Beendigung der Dienstpflichtverletzung."),
 ]),
 ("Abs. 1a, 4", [
  ("Drei Jahre nach Zustellung der Entscheidung, gegen den Beamten ein Disziplinarverfahren durchzuführen, darf keine Disziplinarstrafe mehr verhängt werden.", T),
  ("Hat der Sachverhalt zu einer strafgerichtlichen Verurteilung geführt und ist die strafrechtliche Verjährungsfrist länger, tritt sie an die Stelle der Frist des Abs. 1 Z 3.", T),
  ("Die strafrechtliche Verjährungsfrist tritt auch dann an die Stelle der Frist, wenn sie kürzer ist.", F, "Nur wenn sie länger ist."),
  ("Die Frist des Abs. 1a beträgt fünf Jahre.", F, "Sie beträgt drei Jahre."),
 ]),
 ("Abs. 2", [
  ("Die Fristen werden für die Dauer eines Verfahrens vor dem Verfassungsgerichtshof, Verwaltungsgerichtshof oder einem Verwaltungsgericht gehemmt (sofern der Sachverhalt Gegenstand ist).", T),
  ("Die Fristen werden für die Dauer eines Strafverfahrens nach der StPO gehemmt.", T),
  ("Die Fristen werden zwischen rechtskräftiger Beendigung oder Einstellung eines Strafverfahrens und dem Einlangen einer Mitteilung bei der Dienstbehörde gehemmt.", T),
  ("Ein Strafverfahren hemmt den Fristenlauf nicht.", F, "Es hemmt die Fristen (Abs. 2 Z 3)."),
 ]),
],
"112": [
 ("Abs. 1", [
  ("Die Dienstbehörde hat die vorläufige Suspendierung zu verfügen, wenn über den Beamten die Untersuchungshaft verhängt wird.", T),
  ("Sie hat sie zu verfügen, wenn eine rechtswirksame Anklage wegen eines in § 20 Abs. 1 Z 3a angeführten Delikts vorliegt und sich die Anklage auf die Tatbegehung ab dem 1. Jänner 2013 bezieht.", T),
  ("Sie hat sie zu verfügen, wenn durch die Belassung im Dienst das Ansehen des Amtes oder wesentliche Interessen des Dienstes gefährdet würden.", T),
  ("Sie hat sie bereits bei jeder Anzeige wegen einer Dienstpflichtverletzung zu verfügen.", F, "Das Gesetz nennt nur die Fälle der Z 1 bis 3."),
 ]),
 ("Abs. 2, 6", [
  ("Jede vorläufige Suspendierung ist unverzüglich der Bundesdisziplinarbehörde mitzuteilen, die innerhalb eines Monats zu entscheiden hat.", T),
  ("Die vorläufige Suspendierung endet spätestens mit rechtskräftiger Entscheidung der Bundesdisziplinarbehörde oder des Bundesverwaltungsgerichts über die Suspendierung.", T),
  ("Die Bundesdisziplinarbehörde hat innerhalb von drei Monaten zu entscheiden.", F, "Die Entscheidungsfrist beträgt einen Monat."),
  ("Die Suspendierung endet spätestens mit dem rechtskräftigen Abschluss des Disziplinarverfahrens.", T),
 ]),
 ("Abs. 4", [
  ("Jede Suspendierung, auch eine vorläufige, hat die Kürzung des Monatsbezuges auf zwei Drittel für die Dauer der Suspendierung zur Folge.", T),
  ("Für die Dauer der vorläufigen Suspendierung erfolgt eine Auszahlung ohne Kürzung.", T),
  ("Die Kürzung beträgt die Hälfte des Monatsbezuges.", F, "Sie beträgt zwei Drittel (der Beamte erhält zwei Drittel)."),
  ("Die Kürzung ist auf Antrag oder von Amts wegen zu vermindern oder aufzuheben, wenn das monatliche Gesamteinkommen der Beamtin oder des Beamten und der sorgepflichtigen Familienangehörigen den Mindestsatz nach § 26 Abs. 5 PG 1965 nicht erreicht.", T),
 ]),
 ("Abs. 3, 5, 7, 8", [
  ("Die Beschwerde gegen eine (vorläufige) Suspendierung hat keine aufschiebende Wirkung.", T),
  ("Wird die Bezugskürzung auf Antrag des Beamten vermindert oder aufgehoben, wird dies mit dem Tag der Antragstellung wirksam.", T),
  ("Nimmt der Beamte während der Suspendierung eine erwerbsmäßige Nebenbeschäftigung auf, erhöht sich die Kürzung um den Teil, um den die Einkünfte ein Drittel des Monatsbezugs übersteigen.", T),
  ("Der Disziplinaranwältin oder dem Disziplinaranwalt steht gegen eine Entscheidung der Bundesdisziplinarbehörde, keine Suspendierung zu verfügen, kein Beschwerderecht zu.", F, "Er hat das Recht der Beschwerde an das Bundesverwaltungsgericht (Abs. 3)."),
 ]),
],
"131": [
 ("§ 131", [
  ("Die Dienstbehörde kann ohne weiteres Verfahren schriftlich eine Disziplinarverfügung erlassen, wenn der Beamte vor dem Dienstvorgesetzten, dem Leiter der Dienststelle oder der Dienstbehörde eine Dienstpflichtverletzung gestanden hat.", T),
  ("Sie kann dies, wenn die Dienstpflichtverletzung aufgrund eindeutiger Aktenlage als erwiesen anzunehmen ist.", T),
  ("Sie kann dies, wenn der Beamte wegen desselben Sachverhalts rechtskräftig durch ein Strafgericht oder Verwaltungsgericht bestraft wurde.", T),
  ("Die Disziplinarverfügung kann auch mündlich erlassen werden.", F, "Sie ergeht schriftlich."),
 ]),
 ("§ 131", [
  ("Die Disziplinarverfügung setzt voraus, dass sie unter Bedachtnahme auf die für die Strafbemessung maßgebenden Gründe zur Ahndung ausreichend erscheint.", T),
  ("Die Disziplinarverfügung ist auch der Disziplinaranwältin oder dem Disziplinaranwalt zuzustellen.", T),
  ("In der Disziplinarverfügung darf nur der Verweis ausgesprochen oder eine Geldbuße bis zur Höhe eines Monatsbezuges verhängt werden.", T),
  ("In der Disziplinarverfügung darf eine Geldbuße bis zu zwei Monatsbezügen verhängt werden.", F, "Höchstens ein Monatsbezug."),
 ]),
],
}
