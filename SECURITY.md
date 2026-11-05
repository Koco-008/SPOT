# Sicherheit beim SPOT-BMA-Nachbau

Dieser Guide veröffentlicht **nur öffentliche Ed25519-Schlüssel**. Die Signierschlüssel bleiben bei den offiziellen Herausgebern. Für die Installation sind keine GitHub-Zugangstokens nötig.

- Führe keine Root-Skripte aus, bevor die zugehörigen veröffentlichten Dateien mit dem unabhängigen Public-Key und dem SHA256-Wert des eingefrorenen BMA-Releases geprüft wurden.
- Niemals private GitHub-, WLAN-, SSH- oder API-Tokens in Issues, Bildern oder Logs veröffentlichen.
- Kein `curl | bash` und keine unkontrollierten Kernel-/Treiber-Upgrades.
- Verdrahtung nur spannungsfrei; der Pi-GPIO verträgt **keine 5-V-Signale**.
- Fehlersuche an Hochspannungsplatinen ist nicht Gegenstand dieses Aufbaus.
- Unsichere oder veraltete Betriebsumgebungen nicht durch Abschalten von Prüfschranken „kompatibel“ machen.

Sicherheitsprobleme nach Erstellung des Repositories bitte **nicht** als öffentlichen Issue mit Exploitdetails posten, sondern über GitHub **Report a vulnerability** melden, sofern vom Betreiber eingerichtet.
