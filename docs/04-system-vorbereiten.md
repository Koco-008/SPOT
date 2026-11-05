# 4 – Raspberry Pi und Betriebssystem vorbereiten

> **Dies ist die Einrichtung auf einem NEUEN Pi. Auf einem bereits funktionierenden SPOT diese Schritte nicht ausführen.**

Der BMA-Stand ist **Raspberry Pi 5 / 64-Bit Debian 13 (Trixie)** und ein für den Lepton-Treiber bestätigter Kernel. **Die vorliegende Erstinstallationsroutine ist auf `6.18.50+rpt-rpi-2712` eingeschränkt.** Ein aktuelles Raspberry-Pi-OS-Image kann abweichen. In diesem Fall **anhalten**, nicht auf Verdacht Firmware oder Kernel downgraden.

## A. Speicherkarte schreiben (am PC)

1. [Raspberry Pi Imager](https://www.raspberrypi.com/software/) installieren.
2. Eine leere microSD-Karte mit mindestens 32 GB einsetzen (Daten werden gelöscht).
3. Raspberry Pi 5 als Gerät und eine **64-Bit-Raspberry-Pi-OS-Version auf Debian 13/Trixie-Basis** wählen. Für die Erstinstallation ist eine Desktop-Variante hilfreich, damit Display/Touch ohne SPOT OS testbar sind. **Es zählt die nach dem Flashen tatsächlich installierte Version**, nicht die Bezeichnung in Imager.
4. In den Imager-Einstellungen einen Benutzer `admin` mit einem **eigenen sicheren Kennwort** erstellen, WLAN/Zeitzone setzen und SSH aktivieren (idealerweise per SSH-Schlüssel; Kennwörter nicht ins Repo kopieren).
5. Karte schreiben, sicher auswerfen, in den Pi stecken und anschliessend den bereits überprüften Hardwareaufbau mit Netzteil versorgen.
6. Die IP-Adresse des Pi aus dem Router auslesen. Bei funktionierender mDNS-Auflösung lautet die SSH-Verbindung beispielsweise `ssh admin@raspberrypi.local`; alternativ `ssh admin@<IP-ADRESSE>`.

## B. Basisbetrieb prüfen (am Pi via SSH)

**Jede Zeile einzeln ausführen und nur bei der erwarteten Ausgabe fortfahren.**

```bash
uname -m
uname -r
. /etc/os-release; echo "$PRETTY_NAME"
whoami
```

Erwartet: `aarch64`, **`6.18.50+rpt-rpi-2712`**, Debian 13 / Trixie und `admin`.

**Wenn `uname -r` anders lautet:** Die Software ist für diesen Kernel nicht als Erstinstallation freigegeben. Den Pi nicht mit nicht verifizierten Kernelpaketen verändern. Stattdessen ein zum freigegebenen Stand passendes und vertrauenswürdig archiviertes Original-Image suchen oder die Treiberkompatibilität unabhängig nachqualifizieren. Das Handbuch enthält ausdrücklich **kein** universelles SD-Image.

## C. Hardware einzeln prüfen

1. Das Waveshare-Display muss Bild und Touch-Eingaben auf dem normalen Raspberry-Pi-Desktop zeigen. Falls es schwarz bleibt, zuerst das Hersteller-Wiki und den **DSI1**-Anschluss prüfen.
2. Die Raspberry Pi Camera Module 3 sollte als Kamera erkannt werden:

```bash
rpicam-hello --list-cameras
```

Bei fehlendem Befehl zuerst die Raspberry-Pi-Kamerapakete überprüfen; **nicht** irgendein veraltetes Kamera-Overlay installieren. Erwartet ist ein Kameramodul mit IMX708-Sensor.

3. Für den Lepton muss die physische Verdrahtung bereits überprüft sein. SPI/I²C/VSYNC werden durch die spätere kontrollierte Treiberinstallation konfiguriert. Manuelle Tests dürfen die Kamera nicht gleichzeitig mit einem laufenden Treiberdienst ansprechen.

## D. Grundlegende Werkzeuge

Nur falls Pakete fehlen, die Debian-/Pi-Paketquellen zunächst aktualisieren, ohne ein Kernelupgrade zu erzwingen:

```bash
sudo apt update
sudo apt install --no-install-recommends git unzip python3 python3-cryptography python3-venv python3-pip
```

Ein `apt full-upgrade`, Kernelwechsel oder Firmwareupdate ist **kein** Schritt dieser Anleitung. Die SPOT-Installationsroutine prüft weitere Pakete und erstellt gegebenenfalls einen **zustimmungspflichtigen** Installationsplan.

## E. Prüfen, ob die Plattform zu SPOT passt

```bash
cat /proc/device-tree/model
free -h
df -h /
systemctl is-active ssh
```

Erwartet wird Raspberry Pi 5, ausreichend freier Speicher und ein erreichbarer SSH-Dienst. Bei Abweichungen nicht zur Treiberinstallation übergehen.

**Weiter:** [Signierte Pakete herunterladen und prüfen](05-download-verifizieren.md).
