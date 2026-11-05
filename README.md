# SPOT – Wärmebildkamera selbst bauen

**Vorbereitete öffentliche Bau- und Installationsanleitung zum eingefrorenen BMA-Projektstand.**

SPOT ist eine für die Fehlersuche an elektronischen Platinen entwickelte Wärmebildkamera auf Basis eines Raspberry Pi 5 und eines radiometrischen FLIR Lepton 3.5. Sie zeigt Temperaturen an, ermöglicht Punktmessungen sowie Min-/Max-Erkennung, speichert Wärmebilder mit unveränderten radiometrischen Rohdaten und besitzt eine Touchoberfläche.

> **BMA-Freeze (05.11.2026): SPOT App 0.31.1 Stable + SPOT OS 0.1.7 Stable.**
> Spätere Entwicklungen sind ausdrücklich **nicht** Bestandteil dieses dokumentierten BMA-Stands.

## Der Weg zu deinem eigenen SPOT

| Schritt | Anleitung | Status |
| --- | --- | --- |
| 1. Alles bestellen | [Einkaufsliste](docs/01-einkaufsliste.md) | Hersteller/Artikel eindeutig zugeordnet |
| 2. Hardware vorbereiten | [Zusammenbau](docs/02-zusammenbau.md) | FFC/Steckverbinder, Fotos noch ergänzen |
| 3. Lepton sicher anschliessen | [Verdrahtung](docs/03-verdrahtung.md) | FLIR-Pinbelegung und Pi-BCM-/Physikpins abgeglichen |
| 4. Raspberry Pi OS vorbereiten | [Vorbereitung](docs/04-system-vorbereiten.md) | Strikte Kernel-Kompatibilität beachten |
| 5. Signierte Pakete beziehen | [Download und Prüfung](docs/05-download-verifizieren.md) | Prüfsummen, Ed25519-Verifikation und verpackte Originalquellen |
| 6. Software auf neuem Pi installieren | [Erstinstallation](docs/06-installation.md) | **Noch nicht auf einer fabrikneuen SD-Karte von Dritten validiert** |
| 7. Aufnahme und Temperaturen testen | [Inbetriebnahme](docs/07-inbetriebnahme.md) | Prüfplan |
| Probleme beheben | [Fehlerhilfe](docs/08-fehlerbehebung.md) | Bekannte Fälle |

**[Kurzübersicht: Start in 15 kontrollierten Schritten](QUICKSTART.md)** · [Bedienung](docs/10-bedienung.md) · [FAQ](docs/11-faq.md) · [Projektstruktur](PUBLISHING.md)

## Das Handbuch auf den Raspberry Pi bringen

Dieses öffentliche GitHub-Repository kannst du ohne Anmeldung herunterladen (GitHub: **Code → Download ZIP**). Entpacke den Guide im Home-Verzeichnis des Pi unter `~/SPOT/`, oder verwende bei vorhandenem Git:

```bash
git clone https://github.com/Koco-008/SPOT.git ~/SPOT
cd ~/SPOT
bash scripts/check_pi.sh
```

**Wichtig:** Lade ausschliesslich diese öffentliche Anleitung herunter; das private Entwicklungsrepository `Koco-008/SPOT-App` ist für einen Nachbau nicht erforderlich.

## Was du brauchst

Raspberry Pi 5, offiziellen Active Cooler, 27-W-USB-C-Netzteil, microSD, **FLIR Lepton 3.5 (500-0771-01)**, **FLIR Breakout Board v2.0 (250-0577-00)**, Raspberry Pi Camera Module 3, Waveshare **5inch DSI LCD 800×480 (SKU 18396)**, passende Kamera-/Display-Flachbandkabel und Dupont-Verbindungskabel. Siehe die [verbindliche Einkaufsliste](docs/01-einkaufsliste.md) für Details.

## Signierte Software

- [App 0.31.1 – offizieller Stable-Release](https://github.com/Koco-008/SPOT-Releases/releases/tag/v0.31.1)
- [OS 0.1.7 – offizieller Stable-Release](https://github.com/Koco-008/SPOT-OS-Releases/releases/tag/os-v0.1.7)
- [SPOT-OS – vollständiger öffentlicher Quellcode](https://github.com/Koco-008/SPOT-OS) (kein signiertes Installationspaket)
- [Öffentliches Lepton-Pi5-Treiberprojekt](https://github.com/Koco-008/Lepton-Pi5)

Die Dateien liegen in den **expliziten ZIP-Assets**, nicht in den automatisch von GitHub erstellten `Source code (zip)`-Downloads. Die Releases sind getrennt mit Ed25519 signiert. [So prüfst du sie](docs/05-download-verifizieren.md).

## Wichtige Grenze der Erstinstallation

Das geprüfte Lepton-Provisioning ist für **Raspberry Pi 5, Debian 13/aarch64 und Kernel `6.18.50+rpt-rpi-2712`** zugelassen. Ein frisch heruntergeladenes Raspberry Pi OS kann inzwischen einen anderen Kernel mitbringen. Nicht blind zurück- oder hochrüsten. Das Hilfsskript verweigert einen unpassenden Kernel; stattdessen ist ein nachweislich kompatibles OS-Abbild beziehungsweise eine separat geprüfte Treiberfreigabe notwendig. Eine vollständig automatisierte Installation auf beliebig aktuellen Images wäre ein **separates Projekt nach der BMA**.

Es gibt **noch keinen validierten Ein-Klick-Installer oder ein geprüftes fertiges SD-Image**. Die detaillierte erste Einrichtung im Ordner `docs` ist ein reproduzierbarer Installationsplan, aber noch kein durch einen unbeteiligten Anfänger erfolgreich getesteter Durchlauf. Die Projektversion auf dem ursprünglichen BMA-Prototyp funktioniert; eine Neuinstallation ist ein eigener Nachweis.

Das ursprüngliche Entwicklungsrepository heisst seit der öffentlichen Projektaufteilung `SPOT-App` und bleibt privat. Seine GitHub-Releases-Seite ist **nicht** der aktuelle Downloadkanal. Die signierten App-Quellpakete werden offiziell über **`SPOT-Releases`** bereitgestellt.

## Sicherheit / Nutzungsgrenzen

- Vor dem Verdrahten das Netzteil abziehen. Kein 5-V-Pegel an die GPIO-Signalleitungen.
- Eine Kamera stellt **nicht jeden Platinenfehler** dar. Emissionsgrad und reflektierende Oberflächen beeinflussen Temperaturen.
- Keine offenen Hochspannungsplatinen berühren. Schutz- und Prüfregeln am Arbeitsplatz gelten weiterhin.
- Alle Softwaredownloads signaturprüfen. Keine GitHub-Tokens oder privaten Schlüssel auf dem Gerät hinterlegen.
- FLIR Lepton/Breakout sind Drittprodukte mit eigenen Herstellerbedingungen; die SPOT-MIT-Lizenz gilt nicht automatisch für fremde Hardware, Firmware oder Treiber.

## Lizenz und Nachweise

Dokumentation/Hilfsprogramme: [MIT-Lizenz](LICENSE). Externe Komponenten behalten ihre eigenen Lizenzen. [Quellen, Prüffakten und offene Punkte](docs/09-quellen-und-grenzen.md).

**Keine sensiblen Daten veröffentlichen:** keine WLAN-Namen/Passwörter, SSH-Schlüssel, lokale Logdateien, BMA-interne Dokumente oder private Git-Historie hochladen.
