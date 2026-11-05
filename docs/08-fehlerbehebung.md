# 8 – Fehlerbehebung

Die folgenden Schritte sind nach Risiko geordnet. **Zunächst nur lesen/prüfen**, danach allenfalls gezielt eingreifen. Keine GPIO-Stecker bei laufendem System umstecken.

| Problem | Erste Prüfung | Nicht tun |
| --- | --- | --- |
| Raspberry Pi startet nicht | Originalnetzteil, SD-Sitz, Kabel, Displayrevision, kurzschlussfreie GPIO-Versorgung | Spannung am eingeschalteten Gerät umstecken |
| Pi warnt vor zu schwachem Netzteil | Original 27-W-/5,1-V-/5-A-Versorgung und Kabel prüfen | Die Warnung durch einen zufälligen Power-Parameter ignorieren |
| Display schwarz | DSI1, geeignetes 22↔15-FFC, Rev ≥2.2, `vcgencmd display_power` **nicht** als blindes Mittel nutzen | FFC im Betrieb drehen |
| RGB-Bild fehlt | Kamera erkannt? `rpicam-hello --list-cameras` | CSI/DSI-Kabel vertauschen |
| Lepton wird nicht erkannt | Verdrahtung aus Schritt 3 und `sudo spot-os driver-status --user admin` | Treiber beliebig ersetzen, SPI-Clock ohne Diagnose verändern |
| `unsupported_kernel` | `uname -r`: exakt qualifizierte Version? | Auf gut Glück Kernel upgraden/downgraden |
| Temperaturwerte fehlen | `sudo spot-os doctor`; CCI-Bestätigung/Frame-Frische | Rohbildpixel als Temperatur behandeln |
| FFC löst Problem nicht | `journalctl -b -u lepton-streamer.service -n 100 --no-pager` | FFC beliebig wiederholen |
| `Kein aktuell bestätigter radiometrischer Sensorframe ...` | App-Version `0.31.1` oder neuer? Lepton-Gesundheit prüfen | Sensorgenerationen manuell fälschen |
| Update erscheint nicht | Stable-Kanal, Internet, installierte Version, signiertes Release | Unsigniertes ZIP direkt ausführen |
| GUI bleibt beim Logo | `sudo spot-os doctor`, `sudo systemctl status spot-os-session.service` | Sperren, PID-Dateien oder Journale löschen |
| Aufnahme gespeichert, aber Datei fehlt | Speicherplatz `df -h`, Messungsverwaltung/Export | Während Schreibvorgang Strom abziehen |

## Lesbare Diagnosen per SSH

```bash
sudo spot-os doctor
sudo spot-os driver-status --user admin
sudo systemctl status lepton-streamer.service --no-pager -l
sudo systemctl status spot-os-session.service --no-pager -l
sudo journalctl -b -u lepton-streamer.service -n 100 --no-pager
sudo journalctl -b -u spot-os-session.service -n 100 --no-pager
sudo journalctl -b -u spot-os-update.service -n 100 --no-pager
uname -r
```

Beim Erstellen eines Supporttickets zuerst die Ausgabe kontrollieren und sensible Informationen anonymisieren. Insbesondere **keine** privaten Keys, Zugangstokens, WLAN-Daten, Host-Identitäten oder ganze Benutzerverzeichnisse veröffentlichen.

## Ein abgebrochenes Lepton-Setup

Die Provisionierung schreibt einen eigenen Zustand in `/var/lib/spot-os/lepton-provision.json`. Wenn `pending` oder `awaiting-reboot` gemeldet wird, ist ein explizit bestätigter Neustart mit anschliessendem `--resume-lepton` vorgesehen. Falls der Ablauf stattdessen fehlschlägt, nicht blind erneut ausführen: Erst Journal und DKMS-Status prüfen.

```bash
sudo dkms status
sudo cat /var/lib/spot-os/lepton-provision.json
```

Die eingebaute Rollback-Funktion ist nur nach dem dokumentierten Administrator-Preflight und bei gestoppten exklusiven Lepton-Prozessen vorgesehen. **Nicht** auf einem funktionierenden BMA-Gerät ausprobieren.

## App- und OS-Rollback

- App: Der signierte Launcher verwaltet eine vorherige Version und kann einen kontrollierten Rollback zulassen; **nicht** die aktuelle `current.json` von Hand ändern.
- OS: SPOT OS verwaltet eigene transaktionale Journale. Eine defekte Erstinstallation wird im Zweifel über ein **vorher erstelltes SD-Image** wiederhergestellt. Keine blind wiederholten Update- oder Aktivierungsbefehle.
- Fragen und Fehlerberichte: [GitHub Issues](https://github.com/Koco-008/SPOT/issues) (öffentliches Projekt-Repository).

## Wann Support statt Selbstversuch nötig ist

Wenn der Pi nicht bootet, der Lepton heiss wird, ein Verdrahtungskurzschluss vorliegt, `sudo spot-os doctor` nach erfolgreicher Einrichtung `ok=false` meldet oder der Treiber nicht gebaut werden kann: **Stromversorgung sicher trennen und keine weiteren Installationsbefehle ausführen**, bis die Ursache feststeht.
