# Häufige Fragen

**Kann ich mit einem beliebigen Raspberry Pi starten?** Nein. Die dokumentierte Hardwarebasis ist Raspberry Pi 5. Die Treiber-Ersteinrichtung ist zudem an eine exakt qualifizierte Debian-13-/Kernel-Kombination gebunden.

**Brauche ich GitHub-Zugang?** Nein, um die signierten öffentlichen App- und OS-Pakete zu erhalten. Die Softwarequellen stecken in den Release-ZIPs. Ein GitHub-Konto ist nur zum Melden von Problemen oder Entwickeln nötig.

**Wo ist der Quellcode?** Die offiziellen signierten ZIPs enthalten die für den jeweiligen Release benötigten editierbaren Quell-Dateien. Das ursprüngliche Entwicklungsgit ist privat; seine Historie ist für den Nachbau nicht erforderlich.

**Weshalb ist das OS nicht per normalem OTA auf einer leeren SD installierbar?** OTA setzt eine vorhandene kompatible SPOT-OS-Installation voraus. Der OS-0.1.7-Release akzeptiert OTA von OS 0.1.6. Eine Erstinstallation verwendet das separat geprüfte Setup im signierten Paket.

**Muss ich einen USB-Akku kaufen?** Nein. Der eingefrorene BMA-Referenzaufbau verwendet das offizielle Pi-5-Netzteil. Stromversorgung mit Akkus und eigenem BMS ist ein Zusatzprojekt.

**Wo bekomme ich ein Gehäuse?** Ein öffentlich verifiziertes Gehäuse-STL ist in diesem Guide noch nicht enthalten. Ein elektrisch sicherer offener Aufbau auf einer isolierenden Montageplatte funktioniert als Labormodell; für eine geschlossene portable Konstruktion ist die passende Mechanik separat nachzuweisen.

**Kann ich nach dem Nachbau alle Temperatursensorwerte als exakte Referenz verwenden?** Nein. Emissionsgrad, Oberflächenmaterial, Reflexionen, FFC und Aufnahmedistanz beeinflussen die Messung. Vergleichsmessungen mit bekannten Oberflächen sind erforderlich.

**Kann ich auch eine andere Waveshare-Displayrevision verwenden?** Nicht ohne Prüfung. Entscheidend sind 800×480, DSI-Kompatibilität mit Pi 5 und der Anschluss der konkreten Hardwareversion; `5inch DSI LCD (C)` mit 1024×600 ist nicht gleichwertig.
