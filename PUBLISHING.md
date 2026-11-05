# Repository-Struktur und eingefrorener BMA-Stand

Dieses öffentliche Repository **[Koco-008/SPOT](https://github.com/Koco-008/SPOT)** dokumentiert das gesamte SPOT-Nachbauprojekt, nicht den privaten Entwicklungsverlauf.

| Repository | Inhalt | Für den Nachbau erforderlich? |
| --- | --- | --- |
| [`SPOT`](https://github.com/Koco-008/SPOT) | Diese Anleitung, Stückliste, Verdrahtung, Installationsprüfung | Ja |
| `SPOT-App` (privat) | App-Entwicklung, CI und signierte Veröffentlichungs-Workflows | Nein |
| [`SPOT-Releases`](https://github.com/Koco-008/SPOT-Releases/releases/tag/v0.31.1) | Offiziell signierte SPOT App 0.31.1, inklusive editierbarer Quelltexte | Ja |
| [`SPOT-OS-Releases`](https://github.com/Koco-008/SPOT-OS-Releases/releases/tag/os-v0.1.7) | Offiziell signiertes SPOT OS 0.1.7 | Ja |
| [`Lepton-Pi5`](https://github.com/Koco-008/Lepton-Pi5) | Öffentliche Treiberquelle, vom OS-Installer fest an eine geprüfte Revision gebunden | Automatisch durch das signierte Setup |

## Wichtig: keine zweite Release-Quelle

Die in `SPOT-App` historisch sichtbaren Releases enden vor dem zuletzt signierten Stable-Stand. Die offizielle App-Veröffentlichung erfolgt seit v0.28.6 in `SPOT-Releases`. Ein Release in der privaten App-Quellverwaltung sollte **nicht** als unabhängige, unbestätigte Downloadquelle dupliziert werden. Nur die im Guide festgelegten signierten ZIP-Assets gelten für die Neuinstallation.

## BMA-Freeze

- SPOT App **0.31.1 Stable**.
- SPOT OS **0.1.7 Stable**.
- Referenz-Hardware: Raspberry Pi 5, FLIR Lepton 3.5, Pi Camera 3, Waveshare 5inch DSI LCD 800×480.
- Die Software lief in dieser Kombination auf dem ursprünglichen BMA-Gerät.
- Künftige App-/OS-Änderungen gehören **nicht** rückwirkend zum BMA-Stand.

Die dokumentierte **Erstinstallation auf einer vollständig neuen SD-Karte** ist noch nicht unabhängig am zweiten Gerät nachgebaut worden. Sie ist in der Anleitung deshalb bewusst als prüfpflichtiger Installationsablauf gekennzeichnet.

## Was nicht öffentlich werden darf

Das ursprüngliche Projektarchiv enthält unter anderem ältere PCB-Projekte, Historien und BMA-Unterlagen. **Dieses Archiv nicht vollständig hochladen.** Dokumente und Bauteile nur nach Sichtung auf persönliche Angaben, Drittsoftware, Lizenzrechte und Versionsstand auswählen. Gehäuse-STEP-Modelle sind im Nutzerarchiv vorhanden, müssen aber vor einer öffentlichen Druckempfehlung noch gegen den realen Prototypen geprüft werden.

Eigene Guide-Dateien: MIT. Drittquellen behalten ihre eigenen Lizenzen.
