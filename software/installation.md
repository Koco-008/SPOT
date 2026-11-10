# SPOT Installation

Flash **Raspberry Pi OS (64-bit, Debian 13 / Trixie)** onto a microSD card using [Raspberry Pi Imager](https://www.raspberrypi.com/software/). Create a user named `admin`, configure networking and enable SSH.

**Required kernel for this release:** `6.18.50+rpt-rpi-2712`. Check it after booting; newer Raspberry Pi OS images may ship with a different kernel. The SPOT OS 0.1.7 driver installer has not been qualified for other kernels.

These steps install **SPOT App 0.31.1** and **SPOT OS 0.1.7** on a new Raspberry Pi 5.

## 1. Connect and check the Pi

Connect via SSH (`ssh admin@<pi-address>`) and run:

```bash
uname -r
git clone https://github.com/Koco-008/SPOT.git ~/SPOT
cd ~/SPOT
bash scripts/check_pi.sh
```

The check must pass before continuing. The Raspberry Pi Camera 3, Lepton 3.5 and Waveshare DSI display should already be connected.

## 2. Install dependencies

```bash
sudo apt update
sudo apt install --no-install-recommends \
  git unzip python3 python3-pip python3-venv python3-cryptography \
  python3-picamera2 python3-numpy python3-smbus2 python3-opencv \
  python3-pyside6.qtcore python3-pyside6.qtgui \
  python3-pyside6.qtwidgets python3-pyside6.qtsvg \
  python3-pyside6.qtnetwork
```

## 3. Download and verify the releases

From `~/SPOT`:

```bash
python3 scripts/spot_releases.py fetch --directory ~/spot-downloads

python3 scripts/spot_releases.py extract --part app \
  --directory ~/spot-downloads --output ~/spot-app-0.31.1-verified

python3 scripts/spot_releases.py extract --part os \
  --directory ~/spot-downloads --output ~/spot-os-0.1.7-verified
```

The download tool verifies the official release signatures and checksums before extraction.

## 4. Install the SPOT App

Run the following **without `sudo`**:

```bash
cd ~/spot-app-0.31.1-verified
python3 tools/dependencies.py

bash tools/install.sh \
  --archive ~/spot-downloads/app/spot-0.31.1.zip \
  --sha256 14c96dadd591bb9878607035eb71d52a607bc1f4cb0f6d6a01032bba249df6fc \
  --version 0.31.1

python3 spot_update.py status
```

If the dependency check reports missing modules, run `python3 tools/dependencies.py --repair` and follow its output. If it selects a different Python interpreter, set `SPOT_PYTHON` to that interpreter before running the app installer.

## 5. Install SPOT OS and the Lepton driver

First verify the downloaded packages once more and copy the verified OS installer into a root-owned directory:

```bash
cd ~/SPOT
python3 scripts/spot_releases.py verify --directory ~/spot-downloads

sudo install -d -o root -g root -m 700 /root/spot-os-0.1.7
sudo cp -a ~/spot-os-0.1.7-verified/spot_os /root/spot-os-0.1.7/
sudo chown -R root:root /root/spot-os-0.1.7
sudo chmod -R go-w /root/spot-os-0.1.7

sudo --preserve-env=SSH_CONNECTION python3 -I \
  /root/spot-os-0.1.7/spot_os/setup_entry.py \
  setup --provision-lepton --user admin
```

**If the installer reports `reboot_required`:**

```bash
sudo reboot
```

Reconnect via SSH, then resume the installation:

```bash
sudo --preserve-env=SSH_CONNECTION python3 -I \
  /root/spot-os-0.1.7/spot_os/setup_entry.py \
  setup --provision-lepton --resume-lepton --user admin
```

Continue only after the setup reports successful completion.

## 6. Activate SPOT OS

```bash
sudo spot-os preflight --user admin
sudo spot-os check
sudo spot-os static-check

sudo spot-os provision-os-updates \
  --key-file /root/spot-os-0.1.7/spot_os/trust/spot-os-release.pub \
  --key-sha256 b142b246c22fd6f56f4207b86bbd5dcef09b122d228af81c0c51130d4309f907

sudo spot-os activate --user admin
sudo reboot
```

After the Pi reboots, SPOT should start automatically. Check the installation with:

```bash
sudo spot-os doctor
```

The final `doctor` result should report `ok: true`. Confirm that the live image, touch interface and temperature readings work on the device.

---
