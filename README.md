# SPOT

SPOT ist eine Wärmebildkamera für die Analyse elektronischer Baugruppen. Das Projekt kombiniert einen Raspberry Pi 5, einen FLIR Lepton 3.5, eine Raspberry Pi Camera 3 und ein 5-Zoll-Touchdisplay.

## Nachbauen

| Bereich | Dokumentation |
| --- | --- |
| Komponenten | [Stückliste](BOM.csv) |
| Zusammenbau und Verdrahtung | [hardware/assembly.md](hardware/assembly.md) |
| Gehäuse / CAD | [hardware/cad/](hardware/cad/) |
| Leiterplatte / Fertigungsdaten | [hardware/pcb/](hardware/pcb/) |
| Fotos und Zeichnungen | [hardware/images/](hardware/images/) |
| Software installieren | [software/installation.md](software/installation.md) |
| Bedienung | [software/usage.md](software/usage.md) |
| Fehlerbehebung | [software/troubleshooting.md](software/troubleshooting.md) |

## Software und Quellen

- [SPOT App – Releases](https://github.com/Koco-008/SPOT-Releases/releases)
- [SPOT OS – Releases](https://github.com/Koco-008/SPOT-OS-Releases/releases)
- [SPOT OS – Quellcode](https://github.com/Koco-008/SPOT-OS)
- [Lepton-Pi5 – Treiber](https://github.com/Koco-008/Lepton-Pi5)

Unter `scripts/` liegen die bestehenden Werkzeuge für Plattformprüfung und Release-Verifikation. Die öffentlichen Signaturschlüssel liegen unter `keys/`.

## Dokumentationsstand

Die neue Struktur ist vorbereitet. Dateien mit dem Hinweis *Dokumentation folgt* sind noch nicht ausgearbeitet. Eine vollständige Erstinstallation auf einem neuen Raspberry Pi ist damit derzeit **nicht** als durchgehend dokumentiert oder unabhängig geprüft anzusehen.

## Lizenz

[MIT](LICENSE). Für externe Hardware und Software gelten deren jeweilige Lizenzen.
