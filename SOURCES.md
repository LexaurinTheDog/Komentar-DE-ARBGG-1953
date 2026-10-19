# Quellen, Fassungsvergleich und Nachweise

## Amtlicher Gesetzestext

Prüfdatum ist der 19. Oktober 2026. Maßgeblich ist die an diesem Tag gesicherte [Gesamt-XML im amtlichen ZIP](https://www.gesetze-im-internet.de/arbgg/xml.zip), Dokument BJNR012670953. [ZIP](sources/arbgg.zip), [XML](sources/arbgg.xml), [amtliches Inhaltsverzeichnis](sources/index.html), [amtliche HTML-Gesamtausgabe](sources/gesamt.html) und [abgeleiteter kanonischer Lesetext](sources/arbgg-canonical.md) liegen bei. Antworten und Prüfsummen sind in [verification.json](sources/verification.json) protokolliert. Die beiden versuchten direkten XML-Adressen lieferten 404; verwendet wurde ausschließlich das erfolgreich geladene und als ZIP sowie XML validierte amtliche Paket.

Amtliche Standangabe: Neufassung vom 2. Juli 1979; zuletzt geändert durch Artikel 7 des Gesetzes vom 20. Mai 2026 (BGBl. 2026 I Nr. 152). Der technische XML-Build trägt 20261008215505. Die Wirksamkeit der jüngsten Änderung ergibt sich zusätzlich aus [Artikel 7 und Artikel 18 der Verkündung](https://www.recht.bund.de/bgbl/1/2026/152/regelungstext.pdf?__blob=publicationFile): [gesicherte PDF](sources/bgbl-2026-I-152.pdf), [Textauszug der vollständigen Verkündung](sources/bgbl-2026-I-152.txt). Das PDF wurde anhand seines tatsächlichen PDF-Headers geprüft. Artikel 7 ergänzt § 62 Absatz 3, Artikel 18 Absatz 1 setzt diese Änderung zum 1. Oktober 2026 in Kraft; die Ausnahmen der Absätze 2 bis 4 betreffen andere Artikel.

Die ergänzende Recherche nach späteren Änderungen ist in [Versionssuche](sources/research/search-version.json) und [Aktualitätssuche](sources/research/search-latest.json) erhalten. Sie ergab keinen belegten späteren ArbGG-Änderungsstand; entscheidend bleibt die gesicherte aktuelle amtliche Konsolidierung zusammen mit der verifizierten Verkündung, nicht der Suchmaschinenausschnitt. Eine lückenlose selbständige historische Nachkonsolidierung sämtlicher Bundesgesetzblätter wird nicht behauptet.

## Original und Vergleich

Das [unveränderte Intake](sources/intake-original.md) wurde aus der zugewiesenen Originaldatei kopiert. Sein SHA-256 lautet `60eac96643ad176e813abafb9c5f4f8ab87036235b23a7ca85728d3f5a91dac5`. Die [maschinelle Vergleichskarte](sources/change-map.json) erhält Rohunterschiede und die [ergänzende Einordnung](sources/version-assessment.json) trennt redaktionelle Hinweise, leere Körper und operative Texte.

Das Intake vom 1. Oktober enthielt den neuen § 62 Absatz 3 bereits textlich; sein Kopf vermerkte noch eine nicht abschließend bearbeitete Änderung. Der aktuelle Kopf nennt diese Änderung als letzten Stand. Die weiteren maschinellen Unterschiede betreffen die sichtbare Wiedergabe leerer Wegfallstellen und die Trennung amtlicher Fußnoten vom Normkörper. Es wurden keine früheren und späteren operativen Fassungen aneinandergehängt.

## Vollständigkeit und Extraktion

Das Skript [Parser](_parse.py) verarbeitet ausschließlich die erhaltene XML-Datei. Der [unabhängige Zusatzprüfer](_audit.py) zählt die offiziellen Kennungen getrennt aus XML und Inhaltsverzeichnis und vergleicht sie mit units.jsonl. Zusätzlich vergleicht er sämtliche Nicht-Leerraumzeichen des Normkörpers und der Fußnoten gegen das XML. So wird nicht bloß geprüft, ob ein aus demselben Parser erzeugter Lesetext in sich konsistent ist.

Der [Vollständigkeitsbericht](completeness-report.json) weist 147 nummerierte Stellen, 19 Gliederungselemente, einen Gesetzeskopf, sämtliche Wegfallstellen und § 48a aus. Die Gliederungen und allgemeinen amtlichen Hinweise sind in [structure.json](sources/structure.json) erhalten. Es gibt keinen operativen Anhangdatensatz; der Hinweis auf nicht mehr anzuwendende Einigungsvertrags-Maßgaben wird ausdrücklich bewahrt. Die im amtlichen XML vorhandenen Wortzusammenziehungen, etwa in § 58 Absatz 4, bleiben im Gesetzeszitat unverändert.

## Ergänzend geprüfte Verweisungen

Amtliche Einzeltexte zu [§ 752a ZPO](https://www.gesetze-im-internet.de/zpo/__752a.html), [§ 753a ZPO](https://www.gesetze-im-internet.de/zpo/__753a.html), [§ 43 EGGVG](https://www.gesetze-im-internet.de/gvgeg/__43.html) und [§ 5 UrhG](https://www.gesetze-im-internet.de/urhg/__5.html) sind mit Rohantworten und abgeleiteten Texten im Quellenordner gesichert. Der Abruf ist in verification.json dokumentiert. Diese punktuellen Kontrollen sind kein Vollkommentar aller extern verwiesenen Gesetze und kein Nachweis sämtlicher Landesumsetzungsvorschriften.

## Rechtsprechung

Zwei Entscheidungen wurden vollständig im lokalen nationalen RII-Bestand gelesen und mit unmittelbar abgerufenen BAG-Volltexten abgeglichen:

- BAG, 23. Mai 2023 – 10 AZB 18/22: [Fallkarte](cases/bag-10-azb-18-22.md), insbesondere Rn. 9–23, 35–43.
- BAG, 14. September 2020 – 5 AZB 23/20: [Fallkarte](cases/bag-5-azb-23-20.md), insbesondere Rn. 8–20 und 26–32.

[Suchprotokoll](cases/search-log.json) und [Abruf-/Hashnachweise](cases/verification.json) dokumentieren Auswahl und Grenzen. Die Fallkarten behandeln die zeitlichen Abweichungen des damaligen Rechts, die eigenen Aussagen des Gerichts und die begrenzte heutige Übertragung. Nur Suchtreffer ohne Volltextlektüre wurden nicht als Autoritäten eingebaut. Für die übrigen Vorschriften wurde keine zusätzliche Entscheidung in dieser Fassung ausgewertet; daraus wird nicht auf das Fehlen einschlägiger Rechtsprechung geschlossen.

## Lizenz und Reproduzierbarkeit

Die Apache-2.0-Lizenz betrifft die ursprüngliche Kommentierung und Redaktion, Copyright © 2026 Vojtěch Říha. Amtliche Gesetzes- und Entscheidungstexte sind gesonderte Quellen. Private Kommentare, nichtamtliche Anmerkungen und kommerzielle Leitsätze wurden nicht übernommen. Die in amtlichen Volltexten enthaltenen Literaturhinweise sind keine Behauptung einer eigenen Auswertung jener Werke.

[Quellenmanifest](source-manifest.json), [Zusatzprüfung](audit-report.json) und [Prüfbericht](REVIEW.md) gehören zum Entwurf. Die zweite Durchsicht ist in REVIEW.md und [second-pass-unit-review.json](second-pass-unit-review.json) dokumentiert. Der erneute Abruf von amtlichem XML und Inhaltsverzeichnis sowie beider BAG-Volltexte ist unter [sources/second-pass/verification.json](sources/second-pass/verification.json) erhalten. Das XML ist unverändert; sämtliche 77 Randnummern der beiden lokalen Entscheidungstexte stimmen nach alphanumerischer Normalisierung mit dem erneut abgerufenen amtlichen HTML überein ([Nachweis](cases/second-pass-text-check.json)). Die Aussagen wurden zusätzlich inhaltlich gelesen und den Fallkarten zugeordnet ([Aussagenprüfung](cases/second-pass-claim-support.json)). Mindestlänge und Skripterfolg sind keine juristische Qualitätsbescheinigung. Eine externe Freigabe oder Veröffentlichung ist nicht erfolgt.
