# SPOT BMA – Schnellübersicht

**Dieser Guide ist keine Abkürzung an den Sicherheits- und Hardwareprüfungen vorbei.** Alle Befehle gelten nur für einen neuen Aufbau. Bei einem unpassenden Kernel oder einem fehlgeschlagenen Signaturtest nicht fortfahren.

1. [Hardware vollständig bestellen](docs/01-einkaufsliste.md) und auf identische Typnummern achten.
2. [Pi, Kameras und Display sicher mechanisch montieren](docs/02-zusammenbau.md).
3. [Acht Lepton-Verbindungen](docs/03-verdrahtung.md) bei getrennter Stromversorgung sorgfältig überprüfen.
4. [Raspberry Pi OS 64-bit Debian 13](docs/04-system-vorbereiten.md) auf microSD schreiben; SSH, Benutzer `admin` aktivieren.
5. `uname -r` prüfen: Nur `6.18.50+rpt-rpi-2712` ist für dieses BMA-Treiber-Setup freigegeben.
6. Dieses GitHub-Guide-Repository auf den Pi klonen oder das ZIP unter `~/SPOT/` entpacken.
7. Im Guide-Verzeichnis `bash scripts/check_pi.sh` ausführen; **STOPP** bei nicht bestandener Prüfung.
8. `sudo apt install python3-cryptography` (falls noch nicht vorhanden).
9. Im Guide-Verzeichnis `python3 scripts/spot_releases.py fetch --directory ~/spot-downloads` ausführen; **zwei gültige Ed25519-Nachweise** abwarten.
10. [App und OS sicher entpacken](docs/05-download-verifizieren.md).
11. [App-Abhängigkeiten prüfen und App 0.31.1 installieren](docs/06-installation.md#61-benötigte-python-pi-abhängigkeiten-bereitstellen).
12. [OS 0.1.7 samt Lepton neu installieren](docs/06-installation.md#63-verifiziertes-spot-os-paket-root-eigen-bereitstellen) – dieser Teil umfasst administrative Änderungen und ggf. einen bewussten Neustart.
13. OS aktivieren und mit `sudo spot-os doctor` kontrollieren.
14. [Aufnahme-, Mess- und Exportfunktionen am Gerät prüfen](docs/07-inbetriebnahme.md).
15. Eine Sicherung der nachweislich funktionierenden SD-Karte erstellen.

**Noch keine „One-Click“-Installation:** Die Erstinstallationsroutine wurde noch nicht unabhängig mit einem fabrikneuen Pi auf diese exakte Dokumentationsversion abgenommen. Sie ist zudem bewusst kernelgebunden. Der originale BMA-Prototyp mit App 0.31.1 und OS 0.1.7 funktioniert.
