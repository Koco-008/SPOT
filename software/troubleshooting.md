# SPOT Troubleshooting

## Installation stops at the platform check

```bash
uname -m
uname -r
. /etc/os-release; echo "$PRETTY_NAME"
```

For the published SPOT OS 0.1.7 first-time installer, the Pi must be **aarch64**, **Debian 13 (Trixie)** and **kernel `6.18.50+rpt-rpi-2712`**. Start with the [dated Raspberry Pi OS image](installation.md#0-flash-raspberry-pi-os). A different kernel will not pass the Lepton driver check.

## Pi Camera Module 3 is missing

```bash
rpicam-hello --list-cameras
```

Check the ribbon cable and its connector orientation. The camera should be listed as an IMX708 device.

## Thermal image or Lepton driver is missing

```bash
sudo spot-os driver-status --user admin
sudo spot-os doctor
sudo journalctl -b -u lepton-streamer.service --no-pager -n 80
```

Check the Lepton breakout board, connector PCB alignment and the exact kernel. Use the reported driver status to identify the failure.

## SPOT interface does not start

Connect over SSH and run:

```bash
sudo spot-os check
sudo spot-os static-check
sudo spot-os doctor
```

Review the reported error before making any system changes.

## Release download or installation fails

From the main project directory:

```bash
cd ~/SPOT
python3 scripts/spot_releases.py verify --directory ~/spot-downloads
```

The verifier reports missing files, invalid signatures and mismatched checksums. If a download failed, remove its incomplete download directory and repeat the [installation instructions](installation.md).
