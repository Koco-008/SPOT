# 1 – Einkaufsliste

Die Angaben beziehen sich auf den **BMA-Referenzaufbau**. Identische Produktnamen können abweichende Revisionen haben. Kontrolliere **Typnummer, Anschluss und Auflösung vor dem Kauf**.

| Menge | Teil | Exakte Auswahl / Hinweis | Hersteller/Bezugsquelle |
| ---: | --- | --- | --- |
| 1 | Raspberry Pi 5 | 64-Bit Pi 5, 8 GB empfohlen; auch andere RAM-Varianten nicht automatisch geprüft | [Raspberry Pi](https://www.raspberrypi.com/products/raspberry-pi-5/) |
| 1 | Raspberry Pi Active Cooler | Offizieller Pi-5-Kühler; keine mechanische Kollision mit FFC/GPIO | [Hersteller](https://www.raspberrypi.com/products/active-cooler/) |
| 1 | Raspberry Pi USB-C-Netzteil 27 W | Offiziell, **5,1 V / 5 A**. Kein beliebiges schwaches Handy-Ladegerät | [Hersteller](https://www.raspberrypi.com/products/27w-power-supply/) |
| 1 | microSD-Karte | 32–64 GB, Markenkartentyp empfohlen; plus USB-SD-Leser am PC falls nötig | [Raspberry Pi Imager](https://www.raspberrypi.com/software/) |
| 1 | FLIR Lepton **3.5** | **500-0771-01**, 160×120 **radiometrisch**; **nicht** Lepton FS1 oder 3.0 | [FLIR](https://oem.flir.com/products/lepton/?model=500-0771-01&segment=oem&vertical=microcam) |
| 1 | FLIR Lepton Breakout v2.0 | **250-0577-00**, VSYNC-Pin, 3–5,5 V am VIN | [FLIR](https://oem.flir.com/products/lepton-breakout-board-v2.0?model=250-0577-00) |
| 1 | Raspberry Pi Camera Module 3 | Standardobjektiv, 15-polige Kameraseite | [Hersteller](https://www.raspberrypi.com/products/camera-module-3/) |
| 1 | Kameraflachbandkabel | **Standard–Mini (15 zu 22 Pin)** für Pi 5, ausreichend lang | [Raspberry Pi Kameradokumentation](https://www.raspberrypi.com/documentation/accessories/camera-software.html) |
| 1 | Waveshare 5inch DSI LCD | **SKU 18396 / 800×480 / kapazitiver Touch**, möglichst Rev 2.2 oder neuer | [Waveshare](https://www.waveshare.com/5inch-dsi-lcd.htm) |
| 1 | DSI-Flachbandkabel | **22 zu 15 Pin, DSI-Cable-12cm** für Pi 5; laut Waveshare beim SKU-18396-Lieferumfang enthalten, nachprüfen | [Waveshare Wiki](https://www.waveshare.com/wiki/5inch_DSI_LCD) |
| 1 | Dupont-Kabelsatz | Mindestens **8 Verbindungen**, Steckerart je nach Breakout-Header und Pi-GPIO (typisch Female–Female bei bestückten Stiftleisten), 10–20 cm | Elektronikfachhandel |
| 1 | Befestigung | M2.5-Abstandshalter, Schrauben, ggf. Distanzstücke; genaue Länge abhängig vom Aufbau | Elektronikfachhandel |
| 1 | Gehäuse / Montageplatte | Optionaler kundenspezifischer 3D-Druck; vorerst **kein verifiziertes universelles STL** | [Offene Punkte](09-quellen-und-grenzen.md) |
| 1 | Computer mit Internet | Für Raspberry Pi Imager, Downloads und SSH | – |
| 1 | Digitalmultimeter mit Durchgangsprüfung | Vor dem Einschalten die Stromversorgungs- und Signalverbindungen kontrollieren | Elektronikfachhandel |
| 1 | Kleiner Schraubendreher | Für Montage und M2.5-Befestigung | Elektronikfachhandel |
| 1 | Isolierende stabile Montageplatte | Für sicheren Tischaufbau ohne festes Gehäuse | Elektronikfachhandel |

**Nicht enthalten:** Powerbank, Akku, BMS, Spannungswandler oder Netzunabhängigkeit. Der BMA-Referenzstand wird über das USB-C-Netzteil betrieben. Einen Akkubau ohne geprüften Schaltplan nicht nachrüsten.

**Bearbeitbare Bestellung:** [BOM.csv](../BOM.csv) – dort können Händler, aktuelle Preise und allfällige Versandkosten ergänzt werden.

## Bestell-Checkliste

- [ ] Lepton **3.5 radiometrisch**, nicht die ähnlich bezeichnete nicht radiometrische Variante
- [ ] Breakout **v2.0 mit VSYNC** (Hersteller-Nr. 250-0577-00)
- [ ] Waveshare **800×480**, nicht 1024×600 oder Hochformat 720×1280
- [ ] Pi-5-Kamera **15↔22-Pin**-Kabel vorhanden
- [ ] Display **22↔15-Pin DSI**-Kabel vorhanden
- [ ] Genügend Female–Female-Leitungen vorhanden
- [ ] Original-Pi-5-Netzteil **5,1 V / 5 A**

## Preise

Preis und Verfügbarkeit hängen vom Land, Datum, Versandkosten und Steuern ab. Deshalb sind hier **keine unzuverlässigen fixen Frankenbeträge** eingetragen. Herstellerseiten enthalten Modelle und verweisen auf autorisierte Händler. Bestelle keine ähnlich benannten Ersatzprodukte ohne Kompatibilitätsprüfung.
