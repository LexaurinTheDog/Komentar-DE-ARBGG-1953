# Zweite Durchsicht des Arbeitsentwurfs

Prüfdatum: **19. Oktober 2026**. Ein frischer Bearbeitungsprozess hat das vorhandene Manuskript vollständig gegen seine Quellen gelesen und korrigiert. Das ist eine gesonderte zweite Durchsicht, **keine externe anwaltliche oder sonstige professionelle Freigabe**.

## Tatsächlich geprüfter Umfang

Alle **147 nummerierten Stellen** wurden einzeln mit ihrem amtlichen Wortlaut gelesen: 133 operative Vorschriften, 13 weggefallene Stellen und die ausdrückliche Leerstelle § 48a. Die Lektüre umfasste Voraussetzungen, Folgen, Absatzunterschiede, Verweisungen, Beispiele und Checklisten. Für jede Einheit hält [second-pass-unit-review.json](second-pass-unit-review.json) den konkreten Prüffokus und den Hash des korrigierten Kommentars fest. Die 19 Gliederungselemente sind keine zusätzlichen Vorschriften.

Das amtliche XML-ZIP und Inhaltsverzeichnis wurden erneut mit HTTP 200 abgerufen und als ZIP/XML beziehungsweise erwartetes HTML geprüft. Das entpackte XML stimmt bytegenau mit der verwendeten Fassung überein (SHA-256 `ee4064238832c74335dd689bd168babb81c323782f9af6ac211d142d28fa12e4`). [Abrufnachweise](sources/second-pass/verification.json) bewahren Zeitpunkt, URL, HTTP-Ergebnis und Hashes. Die Verkündungs-PDF wurde erneut vollständig in Text extrahiert; Artikel 7 ergänzt § 62 Absatz 3, Artikel 18 Absatz 1 setzt diese Änderung zum 1. Oktober 2026 in Kraft. Die Ausnahmen der folgenden Absätze betreffen andere Artikel. Damit ist für diesen Rechtsstand kein zusätzlicher operativer Änderungsbedarf gegenüber der vorhandenen kanonischen Quelle belegt. Das Baudatum wird nicht mit dem Inkrafttreten gleichgesetzt.

Beide zitierten BAG-Entscheidungen wurden vollständig gelesen: **10 AZB 18/22, Rn. 1–44**, und **5 AZB 23/20, Rn. 1–33**, jeweils mit Tenor und Verfahrenskontext. Die erneut abgerufenen amtlichen HTML-Volltexte wurden absatzweise mit den lokalen nationalen Volltexten verglichen; alle 77 nummerierten Gründe stimmen nach alphanumerischer Normalisierung überein ([Textvergleich](cases/second-pass-text-check.json)). Die [Aussagenprüfung](cases/second-pass-claim-support.json) dokumentiert die inhaltliche Belegzuordnung. Parteivorbringen und referierte Meinungen wurden von eigenen Gerichtsaussagen getrennt.

## Konkrete Befunde und Korrekturen

Zehn Einheiten wurden geändert; [second-pass-corrections.json](second-pass-corrections.json) erhält die genauen Vorher-/Nachher-Passagen.

- **§ 111 Absatz 2:** Ein Satz hatte die Reihenfolge sprachlich umgekehrt. Richtig ist die Ausschussverhandlung **vor** der Klage. Die Erläuterung sagt dies nun ausdrücklich; Anerkennungs- und Klagefrist bleiben getrennt.
- **§ 98 Absatz 6:** Die vorläufige Leistung war zu unbestimmt als bloß mögliche Folge beschrieben. Die Fassung erklärt nun die gebundene Anordnung auf Antrag, die beiden gesetzlichen Ausnahmen, den Vollstreckungstitel und das besondere Änderungsverfahren.
- **§ 24 Absatz 1 Nummer 4:** „Langjährige Vorbefassung“ konnte eine nicht vorhandene Mindestdauer suggerieren. Entscheidend ist eine einschlägige frühere Tätigkeit innerhalb des Zehnjahreszeitraums, nicht eine zehnjährige Tätigkeit.
- **§§ 89 und 94:** Die vorher nur verwiesenen Einlegungs- und Begründungsfristen sind nun konkret mit Beginn und Verlängerungsgrenzen erläutert. Bei § 94 wird die besondere Überleitung nach erfolgreicher Nichtzulassungsbeschwerde ausdrücklich abgegrenzt.
- **§ 105 Absatz 2:** Die mündliche Anhörung ist verbindlich formuliert; der Vertragsvorbehalt für Vertretungsregeln ist keine freie Ausnahme davon.
- **§§ 22 und 103:** Missverständliche Formulierungen zur natürlichen Richterperson beziehungsweise zum Verlust der Amtsfähigkeit wurden präzisiert.
- **§ 99:** Die Klärung der Tarifanwendbarkeit ist ausdrücklich von der Tariffähigkeitsfrage nach § 97 unterschieden.
- **§ 113:** Der historische Berichtsauftrag ist als gesetzliche Pflicht bezeichnet; der abgelaufene Termin bewirkt kein Außerkrafttreten.

Die beiden Fallkarten benötigen keine inhaltliche Berichtigung. 5 AZB 23/20 billigt die ursprüngliche Signatur gerade nicht; die Wiedereinsetzung beruht auf dem besonderen unterlassenen Hinweis. 10 AZB 18/22 betrifft den anwaltlichen Status des Verbandssyndikus und lässt sich nicht als damalige allgemeine Nutzungspflicht aller nichtanwaltlichen Verbandsvertreter lesen. Diese zeitlichen und sachlichen Grenzen sind bereits zutreffend dargestellt.

## Technische Prüfung und Grenzen

Der unveränderte zentrale Builder und der strikte Validator werden auf das korrigierte Manuskript angewendet. [validation-result.json](validation-result.json) enthält das tatsächliche strikte Ergebnis. [completeness-report.json](completeness-report.json) prüft alle amtlichen Kennungen, Reihenfolge, leere Stellen, Fußnoten und Normzeichen. [second-pass-validation.json](second-pass-validation.json) vergleicht zusätzlich das frisch abgerufene XML mit den Einheiten und dem tatsächlich erzeugten Buch sowie die Kommentarhashes mit dem Lektüreprotokoll. [audit-report.json](audit-report.json) und [prose-inspection.json](prose-inspection.json) ergänzen Abdeckungs-, Link- und Wiederholungskontrollen. Die Ergebnisentscheidung steht in [review-result.json](review-result.json).

Es gibt keine offenen sachlichen oder quellenbezogenen Blocker dieser Durchsicht. Die Rechtsprechungsarbeit bleibt auf die zwei genannten Entscheidungen begrenzt; für andere Vorschriften ist damit weder das Fehlen einschlägiger Rechtsprechung noch eine vollständige Rechtsprechungsaufarbeitung behauptet. Landesverordnungen, konkrete Gerichtsorganisation, Geschäftsverteilungspläne und sämtliche extern verwiesenen Gesetze wurden nicht umfassend neu recherchiert. Die Aktualitätskontrolle beruht auf amtlicher Konsolidierung und geprüfter jüngster Verkündung, nicht auf einer selbständigen historischen Nachkonsolidierung jedes Änderungsakts. Historische Übergangsverweisungen werden benannt; der Entwurf enthält keine vollständige Edition früherer Fassungen.

Mindestlänge, Textähnlichkeitswerte und Skripterfolg beweisen keine juristische Fehlerfreiheit. Es wurde nichts veröffentlicht, gepusht oder extern eingereicht.
