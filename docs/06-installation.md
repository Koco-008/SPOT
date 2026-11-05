# 6 – Erste Installation auf einer neuen SD-Karte

> **Einrichtungsplan, noch keine unabhängig am fabrikneuen Pi abgeschlossene Ende-zu-Ende-Abnahme.** Die produktiven BMA-Versionen funktionieren auf dem ursprünglichen Gerät. Stoppe bei jeder unerwarteten Fehlermeldung. Auf einem bereits installierten SPOT sind diese Root-Einrichtungsschritte nicht anzuwenden.

**Vorbedingungen:** Einkauf, Verkabelung und Displaysystem geprüft; Debian 13 / aarch64 / Kernel `6.18.50+rpt-rpi-2712`; Pi-Benutzer `admin`; SSH-Rettungszugang; [beide ZIPs erfolgreich signaturverifiziert und entpackt](05-download-verifizieren.md).

## 6.1 Benötigte Python-/Pi-Abhängigkeiten bereitstellen

Die neue App benötigt Picamera2, NumPy, OpenCV, PySide6 inklusive QtSvg, SMBus2 und `cryptography`.

```bash
sudo apt update
sudo apt install --no-install-recommends \
  python3-picamera2 python3-numpy python3-smbus2 python3-cryptography \
  python3-pyside6.qtcore python3-pyside6.qtgui python3-pyside6.qtwidgets \
  python3-pyside6.qtsvg python3-pyside6.qtnetwork python3-opencv python3-venv
```

Die Verfügbarkeit und Namen einzelner Pakete sind von der aktuellen Debian-/Raspberry-Pi-Quelle abhängig. Wenn der Paketmanager etwas nicht findet, **nicht blind Pakete aus Fremdquellen installieren**.

Der offizielle App-Preflight liefert die fehlenden Abhängigkeiten:

```bash
cd ~/spot-app-0.31.1-verified
python3 tools/dependencies.py
```

Wenn er fehlende Pakete meldet, kann eine gezielte Reparatur geprüft werden:

```bash
python3 tools/dependencies.py --repair
```

Nur eine tatsächlich verstandene Paketliste mit `JA` bestätigen; der Installer lehnt unkontrollierte Upgrades/Entfernungen ab. Falls ein Virtualenv vorgeschlagen wird, **genau den ausgegebenen Interpreter** für die folgenden App-Installationsschritte wählen (`SPOT_PYTHON=...`).

## 6.2 Signierte App 0.31.1 lokal installieren

**Nicht mit `sudo` ausführen.** App und Update-Launcher gehören dem Benutzer `admin`.

```bash
cd ~/spot-app-0.31.1-verified
bash tools/install.sh \
  --archive ~/spot-downloads/app/spot-0.31.1.zip \
  --sha256 14c96dadd591bb9878607035eb71d52a607bc1f4cb0f6d6a01032bba249df6fc \
  --version 0.31.1
```

Die Installation sollte `~/.local/share/spot/` und den Launcher `~/.local/share/spot/bin/spot` erzeugen. Version überprüfen:

```bash
python3 spot_update.py status
```

Erwartet ist `0.31.1`. Wenn die App wegen des noch nicht eingerichteten Lepton-Treibers keine Kamera meldet, ist das zu diesem Zeitpunkt möglich. Dennoch **nicht** die Kameraprüfung oder Treiberfreigabe umgehen.

Bei Umgebungen mit `SPOT_PYTHON` den von `dependencies.py` geprüften Interpreter in **allen** App-Installationskommandos konsistent verwenden.

## 6.3 Verifiziertes SPOT-OS-Paket root-eigen bereitstellen

Der OS-Setup-Einstieg fordert ein **root-eigenes, unveränderliches** entpacktes Paket mit geschützten Elternverzeichnissen. Die Benutzerkopie ist bereits signatur- und hashgeprüft. Vor dem Root-Kopieren prüfen:

```bash
python3 ~/spot-app-0.31.1-verified/spot_update.py status
cd ~/SPOT
python3 scripts/spot_releases.py verify --directory ~/spot-downloads
```

Der zweite Befehl wird ausdrücklich aus dem Hauptordner dieses Build-Guides ausgeführt.

Nun den bereits verifizierten Paketbaum in ein neues geschütztes Root-Verzeichnis kopieren:

```bash
sudo install -d -o root -g root -m 700 /root/spot-os-0.1.7-bma
sudo cp -a ~/spot-os-0.1.7-verified/spot_os /root/spot-os-0.1.7-bma/
sudo chown -R root:root /root/spot-os-0.1.7-bma
sudo chmod -R go-w /root/spot-os-0.1.7-bma
```

Bevor du `setup` startest, `PACKAGE.json` im Root-Baum mit isoliertem Python prüfen. Der Einstieg führt diese Prüfung nochmals automatisch durch. Keine modifizierten oder fremden Dateien hinzufügen.

## 6.4 Lepton-Treiber und SPOT OS erstmals einrichten

Die folgenden Befehle verändern Systemkonfiguration und werden **nur auf einem neu installierten Gerät** verwendet. **Nicht** auf dem funktionierenden BMA-Pi ausführen. Die tatsächliche Erstinstallationslogik steckt im signierten offiziellen OS-0.1.7-Paket, nicht in diesem Guide.

Über eine bestehende SSH-Sitzung:

```bash
sudo --preserve-env=SSH_CONNECTION python3 -I \
  /root/spot-os-0.1.7-bma/spot_os/setup_entry.py \
  setup --provision-lepton --user admin
```

Dieser Vorgang führt eine kontrollierte Lepton-Provisionierung aus. Er benötigt passende Kernel-Header und lädt ausschliesslich die im signierten Paket festgelegte Treiberquelle. Paketinstallationen und Root-Änderungen können stattfinden. Der Installationsvorgang kann als `pending` / `reboot_required` enden. **Das ist kein bereits bestätigter Erfolg.**

**Nur wenn das Programm explizit einen Reboot verlangt**, einmal:

```bash
sudo reboot
```

Nach erneutem SSH-Login die Fortsetzung durchführen:

```bash
sudo --preserve-env=SSH_CONNECTION python3 -I \
  /root/spot-os-0.1.7-bma/spot_os/setup_entry.py \
  setup --provision-lepton --resume-lepton --user admin
```

Bei `unsupported_kernel`, fehlenden passenden Kernel-Headern, falschem Format, fehlendem Lepton oder unerwarteten APT-/DKMS-Änderungen **abbrechen und Fehler protokollieren**. Kein `--force`, keine willkürlichen `modprobe`-/`systemctl`-Neustarts, keine manipulierten Journale.

## 6.5 OS aktivieren und Update-Vertrauen einrichten

Erst wenn `setup` die vollständige Installation bestätigt hat:

```bash
sudo spot-os preflight --user admin
sudo spot-os check
sudo spot-os static-check
```

Der **öffentliche OS-Vertrauensschlüssel** kann aus dem verifizierten OS-Paket bereitgestellt werden:

```bash
sudo spot-os provision-os-updates \
  --key-file /root/spot-os-0.1.7-bma/spot_os/trust/spot-os-release.pub \
  --key-sha256 b142b246c22fd6f56f4207b86bbd5dcef09b122d228af81c0c51130d4309f907
```

Danach erst die dedizierte SPOT-Oberfläche aktivieren:

```bash
sudo spot-os activate --user admin
sudo spot-os doctor
```

Für eine gültige Abnahme muss `doctor` nach einem vollständigen, kontrollierten Neustart unter anderem `integrity_ok=true`, `runtime_ok=true`, `activation_ok=true`, `ok=true` liefern; die Livekamera muss sichtbar und bedienbar sein.

### Nicht tun

- Keine `curl | bash`-Installation aus ungeprüften Quellen.
- Nicht das private Entwicklungsrepository auf den Pi klonen oder dafür einen GitHub-Token einrichten.
- Kein Downgrade auf einen ungeprüften Kernel und kein unkontrolliertes `apt full-upgrade`.
- Nicht sofort das OS-0.1.7-Update als OTA von einem leeren Raspberry Pi ausführen. Der Release erlaubt das OTA ausdrücklich nur von **OS 0.1.6**, die Erstinstallation verwendet den Paket-Einstieg.
- Keine echten Messungen als erfolgreich deklarieren, bevor Livebilder, Werte und Speicherfunktion geprüft sind.

**Weiter:** [Inbetriebnahme und Ersttest](07-inbetriebnahme.md).
