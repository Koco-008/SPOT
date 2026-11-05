# 2 – Mechanischer Aufbau

**Alle Verbindungen nur bei abgezogenem Netzteil herstellen.** Platinen antistatisch anfassen und auf nichtleitender Unterlage arbeiten.

1. Pi, Display und Kameras auspacken, Typnummern und Flachbandkabel kontrollieren.
2. Die beiden kleinen Pi-5-FFC-Anschlüsse kontrollieren. Für das Waveshare-Display ist **DSI1** vorgesehen, für die Pi Camera 3 der andere für Kamera geeignete Anschluss. Positionen und Kontaktorientierung anhand offizieller Herstellerzeichnungen kontrollieren. Die bauähnlichen Anschlüsse sind **nicht beliebig vertauschbar**.
3. Zuerst die FFC-Kabel vorsichtig in die kleinen Raspberry-Pi-Steckverbinder einführen und verriegeln. Offizielle Raspberry-Pi-Anleitung: [Kamera verbinden](https://www.raspberrypi.com/documentation/accessories/camera-software.html). Waveshare-Anleitung: [Display mit Pi 5](https://www.waveshare.com/wiki/5inch_DSI_LCD).
4. Den originalen Pi-5-Active-Cooler gemäss Hersteller montieren (Wärmeleitpads bereits angebracht). Kamera-FFC-Kabel sind danach schwieriger erreichbar.
5. Waveshare DSI-Kabel an das Display anschliessen, Verriegelung und Kontaktseite anhand der **genauen Displayrevision** kontrollieren. Keine Gewalt.
6. Lepton 3.5 ohne verkantete Kontakte vorsichtig ins Breakout v2.0 einsetzen. Herstellermarkierungen beachten. Werkseitige Jumper J5–J9 **nicht entfernen**.
7. Breakout über die [acht Leitungen aus dem Verdrahtungsplan](03-verdrahtung.md) verbinden. Zunächst jede Leitung unabhängig durchmessen und gegen Kurzschluss kontrollieren.
8. Komponenten mechanisch befestigen. Keine leitenden Schrauben/Abstandshalter an freie Lötstellen setzen. Kabel knickfrei führen, Active-Cooler-Luftstrom offen halten.
9. Vor dem ersten Einschalten anhand [Verdrahtung](03-verdrahtung.md) noch einmal **alle GPIO-Nummern als physische Pin-Nummern** kontrollieren. Erst danach Strom anschliessen.

## Gehäuse

Es gibt derzeit **keine als universell nachbaubar bestätigte STL-/CAD-Datei** in diesem öffentlichen Handbuch. Eine separate Gehäuseanleitung ist vor einem Anfänger-Release notwendig. Für den ersten Test ist ein isolierender Tischaufbau mit sicher befestigten Platinen geeigneter als ein ungeprüftes Gehäuse.

## Was noch als Foto dokumentiert werden muss

- Pi 5 mit eingestecktem CSI-/DSI-Kabel vor Kühler-Montage
- Lepton 3.5 im Breakout v2.0 und sichtbarer J2/J3-Pinmarkierung
- Vollständige GPIO-Verkabelung ohne verdeckte Pins
- Front-/Rückseite des Waveshare-Displays und genaue Revision
- Mechanisch fixierter Aufbau ohne leitfähige Kontaktstellen
