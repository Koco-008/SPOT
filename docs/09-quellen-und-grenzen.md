# 9 – Quellen, Annahmen und noch fehlende Nachweise

## Offizielle Hardwareunterlagen

- [Raspberry Pi 5](https://www.raspberrypi.com/products/raspberry-pi-5/) / [Raspberry Pi Dokumentation](https://www.raspberrypi.com/documentation/)
- [Raspberry Pi Camera Module 3](https://www.raspberrypi.com/products/camera-module-3/)
- [Raspberry Pi Active Cooler](https://www.raspberrypi.com/products/active-cooler/)
- [Raspberry Pi 27W USB-C Power Supply](https://www.raspberrypi.com/products/27w-power-supply/)
- [Teledyne FLIR: Lepton 3.5 / Modell 500-0771-01](https://oem.flir.com/products/lepton/?model=500-0771-01&segment=oem&vertical=microcam)
- [Teledyne FLIR: Breakout Board v2.0 / 250-0577-00](https://oem.flir.com/products/lepton-breakout-board-v2.0?model=250-0577-00)
- [FLIR: originaler Raspberry-Pi-Breakout-Anschlussplan](https://github.com/FLIR/Lepton/blob/main/docs/RaspberryPiGuide.md)
- [Waveshare: 5inch DSI LCD SKU 18396](https://www.waveshare.com/5inch-dsi-lcd.htm)
- [Waveshare: 5inch DSI LCD Wiki](https://www.waveshare.com/wiki/5inch_DSI_LCD)

## BMA-Software-Freeze

- [Signierter SPOT App v0.31.1 Stable-Release](https://github.com/Koco-008/SPOT-Releases/releases/tag/v0.31.1), ZIP-SHA256 `14c96dadd591bb9878607035eb71d52a607bc1f4cb0f6d6a01032bba249df6fc`
- [Signierter SPOT OS v0.1.7 Stable-Release](https://github.com/Koco-008/SPOT-OS-Releases/releases/tag/os-v0.1.7), ZIP-SHA256 `4d5b7bc6a41d88c440caa300f130c4fc0409605893e6a8167b7e8ac71181b8b0`
- [Lepton-Pi5-Treiber (öffentlich)](https://github.com/Koco-008/Lepton-Pi5), Treiberversion und Quelle werden durch den signierten OS-Installer festgelegt.

Der Original-Entwicklungsstand liegt im **privaten** GitHub-Repository `Koco-008/SPOT-App`. Die öffentlichen SPOT-App-/OS-Releases enthalten die zum Installieren und Prüfen erforderlichen Quellpakete; dieser Guide verweist **nicht** auf private Checkout-Pfade oder GitHub-Zugriffstokens. Die BMA-Freeze-Versionen werden unabhängig von künftigen Updates dokumentiert.

## Was nachweislich funktioniert

Der Ersteller hat auf dem ursprünglichen BMA-Raspberry-Pi den Stable-Stand **App 0.31.1 + OS 0.1.7** real installiert und die Wärmebildaufnahme und üblichen Funktionen erfolgreich getestet. Der offizielle Release-Workflow hat die signierten Pakete und öffentlichen Downloads geprüft.

## Was für eine Anfänger-Anleitung noch offen ist

1. **Erstinstallation vom frisch geflashten Image:** Noch kein unabhängiger Durchlauf auf einer fabrikneuen SD-Karte mit einem zweiten Pi dokumentiert. Treiberinstallation ist auf den freigegebenen Kernel eingeschränkt. Dies ist eine **wichtige**, nicht kosmetische Einschränkung.
2. **Gehäuse:** Noch kein aus dem tatsächlichen Prototypen verifiziertes CAD-/STL-Modell und keine vollständige mechanische Schrauben-/Distanzstückliste in dieser Anleitung.
3. **Fotos:** Noch fehlen eigene scharfe Fotos beider Seiten des Lepton-Breakouts mit lesbaren Pinmarkierungen, der eingebauten Flachbandkabel, des Gesamtaufbaus und der fertigen GUI.
4. **Stücklisten-Preis:** Preise und Lagerbestände der Bauteile schwanken. Vor Bestellung muss der aktuelle Preis beim ausgewählten Händler bestätigt werden; keine unverifizierten CHF-Gesamtsummen.
5. **Weitere Hardware-/Kernelrevisionen:** Nicht geprüft, selbst wenn Steckverbinder oder Namen kompatibel erscheinen.
6. **Stromversorgung:** Ein Akku-/Powerbankaufbau mit BMS ist nicht Bestandteil des freigegebenen BMA-Referenzaufbaus und nicht spezifiziert.
7. **Fehlerbehandlung:** Die Erstinstallation enthält einige administrative Eingriffe. Für komplette Anfänger wäre langfristig ein unabhängiger, reproduzierbarer SD-Image-Builder mit eigenem Hardwaretest sinnvoll – **nicht** als existierend ausgeben.

## Lizenzen und Sicherheitsgrenzen

Die eigenen Guide-Dateien stehen unter [MIT](../LICENSE). SPOT-App-/OS-Quellen besitzen eigene Lizenzdateien; fremde FLIR SDK-, Firmware-, Display- und Treiberbestandteile können davon abweichende Bedingungen besitzen. Beim Verteilen von Hardware und Treiber-Binaries sind die Original-Lizenzhinweise zu beachten.

Elektronikversuche nur an angemessen abgesicherten, spannungsarmen Prüflingen durchführen. Eine Wärmebildkamera ersetzt weder isolierte Messmittel noch eine professionelle Sicherheitsprüfung.
