# 7 – Erste Inbetriebnahme / Abnahmecheckliste

**SPOT BMA-Referenz:** App `0.31.1` Stable, OS `0.1.7` Stable. Die folgende Checkliste eignet sich für einen frisch nachgebauten SPOT und für die Dokumentation eines erfolgreichen Tests. Der ursprüngliche BMA-Prototyp wurde bereits auf diese Versionen geprüft; ein neuer Aufbau ist unabhängig zu testen.

## 1. Betriebssystem und Gerät

```bash
uname -r
sudo spot-os doctor
sudo systemctl is-active lepton-streamer.service
sudo systemctl is-active spot-os-session.service
```

Erwartet: freigegebener Kernel, beide Dienste aktiv, `doctor`: `ok`, `integrity_ok`, `runtime_ok` und `activation_ok` jeweils `true`. Falls das nicht so ist, zunächst [Fehlerhilfe](08-fehlerbehebung.md) verwenden.

## 2. Bedienoberfläche

- [ ] Vollständiger Strom-Aus-/Einschaltzyklus: SPOT startet ohne normale Desktopoberfläche direkt in die Kamera.
- [ ] Waveshare-Display: korrektes Bildformat 800×480, gut lesbar, Touch bedienbar.
- [ ] Kamera-Ansicht zeigt Wärmebild und – wenn gewählt – RGB-Bild.
- [ ] Die rechte Sidebar bleibt bedienbar; keine Überlappung mit Dialogen.
- [ ] Einstellungen öffnen und wieder zur Liveansicht wechseln.
- [ ] «Messungen» aus Einstellungen öffnen: Zurück geht in Einstellungen.
- [ ] «Messungen» nach abgeschlossener Temperaturverlaufsaufnahme öffnen: Zurück geht zur Liveansicht.

## 3. Radiometrische Messung

- [ ] Es erscheinen neue Wärmebilder (nicht nur ein altes eingefrorenes Bild).
- [ ] Temperaturen werden in °C angezeigt; **unterschiedliche** Oberflächen zeigen sinnvoll unterschiedliche Werte.
- [ ] Punktmessung aktivieren, verschieben und deaktivieren.
- [ ] Hotspot (Maximum) und Coldspot (Minimum) aktivieren; Marker und Werte prüfen.
- [ ] Emissionsgrad-Preset umschalten und prüfen, dass die Änderung vom Lepton bestätigt wird.
- [ ] Manuelles FFC auslösen: danach normale Wiedergabe.
- [ ] Mindestens eine stabil temperierte Referenz mit geeignetem Emissionsgrad prüfen. Die Kamera ist **kein zertifiziertes Thermometer**; Abweichungen dokumentieren, nicht heimlich korrigieren.

## 4. Aufnahmen und Daten

- [ ] Eine normale thermische Einzelbildaufnahme speichern.
- [ ] Ein Bild mit Punkt + Hotspot + Coldspot speichern.
- [ ] Das gespeicherte Thermal-Bild zeigt **alle vier Sensorbildränder** ohne schwarzen 10-Pixel-Rand rechts.
- [ ] Oben links befindet sich die ausgeklappte Temperaturskala; unten rechts das transparente SPOT-Logo.
- [ ] Radiometrische Datei ist mit dem Thermal-Bild verbunden und in der Analyse verwendbar.
- [ ] Separates RGB-Bild vorhanden, wenn für die Aufnahme vorgesehen.
- [ ] Gespeicherte Bilder in der Galerie ansehen, analysieren und exportieren.
- [ ] Einen Temperaturverlauf starten, kontrolliert stoppen und anschliessend öffnen.
- [ ] Übertragung auf den PC testen und Daten dort tatsächlich öffnen.

## 5. Software-Update-Funktion (nur prüfen, nichts unnötig installieren)

- [ ] **Einstellungen → Software-Updates → Nach Updates suchen** erreicht die öffentlichen Kanäle ohne GitHub-Login.
- [ ] App zeigt korrekt `0.31.1` als installiert.
- [ ] OS zeigt korrekt `0.1.7` als installiert.
- [ ] Bereits bestätigte alte Erfolgspopups erscheinen beim normalen Neustart nicht erneut.
- [ ] Kein Update auf eine ältere oder gleich alte Version anbieten lassen.

## 6. Abschlussnachweis

Notiere Datum, Hardware-Revisionen, OS-/App-Version, `uname -r`, `spot-os doctor`-Gesamtstatus und das Ergebnis jeder Checkliste. **Keine SSH-Logs mit WLAN-Passwort, privaten Schlüsseln oder persönlichen Daten öffentlich hochladen.**

Für den Fall eines unerwarteten Systemfehlers eine vollständige Kopie der funktionierenden SD-Karte auf einem getrennten Datenträger anfertigen. So lässt sich der Aufbau reproduzierbar sichern.
