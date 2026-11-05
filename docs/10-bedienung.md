# 10 – Die wichtigsten Funktionen von SPOT

SPOT ist für die thermische Fehlersuche auf **elektronischen Platinen** gedacht. Der Sensor zeigt Oberflächentemperaturen; schlecht leitende oder reflektierende Oberflächen können falsche Rückschlüsse erlauben. Heisse Stellen sind **Hinweise**, keine automatische Fehlerdiagnose.

## Liveansicht

- Wärmebild: vollständiger FLIR-Lepton-3.5-Bereich, wechselbare Farbdarstellung und Temperaturskala.
- Kamera 3: optische Zusatzansicht, z. B. im geteilten Bildschirm.
- Messungen: Punkttemperatur sowie automatisch markierter Hotspot/Coldspot.
- Emissionsgrad: Voreinstellungen, darunter FR4 (typisch 0,95 als Anwendungsannahme), und benutzerdefinierte Werte. Für belastbare Temperaturen die reale Oberfläche und den Einfluss reflektierter Strahlung beachten.

## Speichern

Eine Thermal-Einzelbildaufnahme schreibt ein gerendertes Wärmebild mit Skala/Markierungen/Logo und zusätzlich **unveränderte radiometrische Sensordaten**. Das PNG ist für die Ansicht gedacht, die radiometrischen Daten für spätere quantitative Analysen. Weitere Dateien wie RGB und Metadaten bleiben der Aufnahme zugeordnet.

## Analyse und Temperaturverlauf

In «Messungen» lassen sich Bilder und Verläufe öffnen, verwalten, exportieren und an einen PC übertragen. Analysen verwenden radiometrische Originaldaten, nicht nachträglich aus dem kolorierten PNG geschätzte Temperaturen. Eine Temperaturverlaufsmessung dokumentiert Werte über die Zeit mit kontrolliertem Start, Pause und Abschluss.

## Wartung und Updates

Im Menü «Software-Updates» getrennte signierte Versionen von SPOT App und SPOT OS prüfen. Regulär nur **Stable** auswählen. Die BMA-Zielfassung bleibt bewusst `0.31.1 / 0.1.7`; spätere Updates gehören nicht zur hier festgehaltenen BMA-Version.
