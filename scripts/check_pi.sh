#!/usr/bin/env bash
# Read-only quick check. This script NEVER changes packages, kernel, services or configuration.
set -u
printf 'SPOT BMA 0.31.1 / OS 0.1.7 -- read-only hardware preflight\n\n'
platform=$(uname -m)
kernel=$(uname -r)
. /etc/os-release
printf 'Architektur: %s\nKernel: %s\nBetriebssystem: %s\nBenutzer: %s\n' "$platform" "$kernel" "$PRETTY_NAME" "$(id -un)"
printf '\nPi-Modell: '
if [[ -r /proc/device-tree/model ]]; then tr -d '\0' < /proc/device-tree/model; else printf 'nicht lesbar'; fi
printf '\n\n'
valid=true
if [[ $platform != aarch64 ]]; then printf 'STOPP: Raspberry Pi OS muss aarch64 sein.\n'; valid=false; fi
if [[ $kernel != '6.18.50+rpt-rpi-2712' ]]; then printf 'STOPP: Der OS-0.1.7-Erstinstaller ist nicht für diesen Kernel qualifiziert.\n'; valid=false; fi
if [[ ${VERSION_ID:-} != 13 ]]; then printf 'STOPP: Debian 13/Trixie erforderlich.\n'; valid=false; fi
if [[ $(id -un) != admin ]]; then printf 'HINWEIS: Referenz-Setup verwendet Benutzer admin.\n'; fi
if [[ -r /proc/device-tree/model ]] && ! tr -d '\0' < /proc/device-tree/model | grep -q 'Raspberry Pi 5'; then printf 'STOPP: Kein Raspberry Pi 5 erkannt.\n'; valid=false; fi
printf '\nVerfügbarer Speicher:\n'; df -h / | tail -n 1
printf '\nSSH: '; systemctl is-active ssh 2>/dev/null || true
if command -v rpicam-hello >/dev/null 2>&1; then
  printf '\nKamera-Inventar:\n'; rpicam-hello --list-cameras 2>&1 | head -n 15
else
  printf '\nHinweis: rpicam-hello noch nicht verfügbar.\n'
fi
if [[ $valid == false ]]; then
  printf '\nERGEBNIS: Erstinstallation NICHT freigegeben. Keine Kernel-Experimente durchführen.\n'
  exit 2
fi
printf '\nERGEBNIS: Die Mindestplattform stimmt. Hardware-/Treiber-/Funktionsprüfung steht noch aus.\n'
