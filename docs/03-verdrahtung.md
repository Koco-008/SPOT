# 3 – Verdrahtung Lepton 3.5 + Breakout v2.0 + Raspberry Pi 5

**ACHTUNG:** Bei Raspberry Pi bezeichnet `GPIO17` die **BCM-Nummer**, nicht den 17. Pin auf der Steckleiste. Die rechte Spalte enthält die **physische Pinposition**. Keine 5-V-Signale auf Lepton-Datenleitungen geben.

Pinbelegung gemäss [FLIR-Raspberry-Pi-Anleitung](https://github.com/FLIR/Lepton/blob/main/docs/RaspberryPiGuide.md) und [FLIR Breakout v2.0](https://oem.flir.com/products/lepton-breakout-board-v2.0?model=250-0577-00).

| Lepton-Breakout | Signal | Raspberry Pi 5 (BCM) | Physischer Pi-Pin |
| --- | --- | --- | ---: |
| J2 P8 | I²C SCL | GPIO3 | **5** |
| J2 P5 | I²C SDA | GPIO2 | **3** |
| J2 P12 | SPI MISO | GPIO9 | **21** |
| J2 P7 | SPI CLK | GPIO11 | **23** |
| J2 P10 | SPI CS / CE0 | GPIO8 | **24** |
| J2 P15 | VSYNC | GPIO17 | **11** |
| J3 P1 (quadratische Lötfläche) | GND | Masse | **6** |
| J3 P2 | VIN | **3,3 V** | **1** |

Der Hersteller erlaubt am **J3-VIN 3–5,5 V**. Für diesen Aufbau ist die Pi-3,3-V-Versorgung am physischen Pin 1 gewählt. **J3 und J2 nicht verwechseln**: Beim Breakout Rev R120 gibt es einen dokumentierten Fehler im alternativen J2-Versorgungspfad; die FLIR-Anleitung verwendet J3. J2-Pins für MOSI, Reset etc. werden hier nicht angeschlossen. Die Breakout-Jumper bleiben in Werksstellung.

## Weitere Verbindungen

- Waveshare 5inch DSI LCD: mit dem passenden **22→15-Pin-DSI-Kabel** zum Pi-5-**DSI1**.
- Pi Camera Module 3: mit dem passenden **22→15-Pin-Kamera-FFC** zum Camera/Display-Anschluss für CSI.
- Active Cooler: eigener Pi-5-Lüfterstecker, **nicht** auf GPIO umverdrahten.
- Strom: offizielles Raspberry-Pi-27-W-Netzteil an den **USB-C-Power-Anschluss** des Pi.

## Vor dem Einschalten

1. Netzteil bleibt abgezogen.
2. Durchgang zwischen Lepton-VIN und GND prüfen: kein Kurzschluss.
3. Jeden Stecker **Signal für Signal** mit Tabelle und Beschriftung abgleichen.
4. Flachbandkabel nur gemäss Hersteller-Verriegelung und Kontaktrichtung einsetzen.
5. Pi auf nichtleitender Unterlage oder Abstandshaltern befestigen.

Die Pinliste beschreibt die elektrische Zuordnung. Eine ausdrücklich fotografierte, an einem **neu aufgebauten SPOT** abgenommene Anschlussanleitung steht noch aus.
