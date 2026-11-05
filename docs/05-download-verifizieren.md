# 5 – SPOT App und SPOT OS sicher herunterladen

**BMA-Freeze:** App `0.31.1` Stable und OS `0.1.7` Stable (05.11.2026). Der OS-Release `0.1.7` erlaubt als **OTA-Upgrade** nur OS `0.1.6`; bei der **Neuinstallation** wird stattdessen sein separat verifiziertes Installationspaket verwendet.

## Warum nicht einfach das GitHub-ZIP entpacken?

GitHub zeigt auch automatisch erstellte `Source code.zip` an. Diese sind **nicht** die signierten SPOT-Pakete. Lade ausschliesslich die ausdrücklich benannten Release-Dateien herunter. Das hier enthaltene Hilfsskript überprüft zusätzlich die zwei im Guide **unabhängig festgelegten Ed25519-Schlüssel** und die exakten SHA256-Werte des BMA-Endstands. Ein Schlüssel aus demselben ungeprüften Download würde die Herkunft **nicht** beweisen.

| Bestandteil | Veröffentlichter Release | Geprüfter ZIP-SHA256 |
| --- | --- | --- |
| App v0.31.1 | [App-Release](https://github.com/Koco-008/SPOT-Releases/releases/tag/v0.31.1) | `14c96dadd591bb9878607035eb71d52a607bc1f4cb0f6d6a01032bba249df6fc` |
| OS v0.1.7 | [OS-Release](https://github.com/Koco-008/SPOT-OS-Releases/releases/tag/os-v0.1.7) | `4d5b7bc6a41d88c440caa300f130c4fc0409605893e6a8167b7e8ac71181b8b0` |

**Öffentliche Schlüssel, ebenfalls als Datei in diesem Guide vorhanden:**

- App: `keys/spot-app.pub`, SHA256 `be3ddaf4363b0c9257a3a171b7cbac05789d05a27f6a9898b1869a9f76b20827`
- OS: `keys/spot-os.pub`, SHA256 `b142b246c22fd6f56f4207b86bbd5dcef09b122d228af81c0c51130d4309f907`

## Einfacher Weg: Prüftool (auf dem neuen Pi)

Dieser Abschnitt setzt voraus, dass der **Guide selbst aus einer vertrauenswürdigen Quelle** auf den Pi übertragen wurde. Bei unklarem Ursprung zuerst seinen Git-Commit gegen den offiziellen Projektlink abgleichen.

Im Hauptverzeichnis dieses Guides:

```bash
python3 scripts/spot_releases.py fetch --directory ~/spot-downloads
```

Das Skript lädt vier Dateien je Release herunter:

- App: `spot-0.31.1.zip`, `update.json`, `update.json.sig`, `SHA256SUMS.txt`
- OS: `spot-os-0.1.7.zip`, `os-update.json`, `os-update.json.sig`, `SHA256SUMS.txt`

Es prüft **beide** Ed25519-Signaturen, Dateigrössen, gepinnte SHA256-Werte, Manifestfelder, ZIP-Pfade und beim OS die internen Paketdatei-Hashes. **Es installiert nichts.**

Ausgabe sollte für jeden Bestandteil `"signature": "valid"` und den erwarteten BMA-Versionsstand enthalten. Bei **jedem Fehler abbrechen**; keine Prüfung abschalten und keine anderen ZIP-Dateien umbenennen.

Du kannst die Prüfung jederzeit wiederholen, ohne erneut herunterzuladen:

```bash
python3 scripts/spot_releases.py verify --directory ~/spot-downloads
```

Falls du bereits manuell die vier Release-Dateien heruntergeladen hast, lege sie in `~/spot-downloads/app/` und `~/spot-downloads/os/` ab und führe `verify` aus.

## App und OS in getrennte Verzeichnisse entpacken

```bash
python3 scripts/spot_releases.py extract --part app \
  --directory ~/spot-downloads --output ~/spot-app-0.31.1-verified
python3 scripts/spot_releases.py extract --part os \
  --directory ~/spot-downloads --output ~/spot-os-0.1.7-verified
```

Die beiden Zielordner müssen vorher **noch nicht existieren**. Das Prüftool verhindert bei der Extraktion Überschreiben, ZIP-Pfad-Traversal und symbolische Links.

Unter `~/spot-app-0.31.1-verified/` müssen u. a. `SPOT_v27.py`, `VERSION` und `tools/install.sh` liegen. Unter `~/spot-os-0.1.7-verified/spot_os/` müssen u. a. `PACKAGE.json`, `setup_entry.py`, `VERSION` liegen.

**Wichtig:** Das Prüftool braucht das System-Paket `python3-cryptography`. Unter Debian wird es mit `sudo apt install python3-cryptography` installiert. Es überträgt keine Zugangstokens und verwendet keine privaten GitHub-Repositories.

**Weiter:** [Erstinstallation auf dem Pi](06-installation.md).
