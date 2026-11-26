# Car Assistant – Quellen

**Drive · Log · Go**

[🇬🇧 English](README.md) · 🇩🇪 Deutsch

Die Paketquelle von [Car Assistant](https://github.com/Matze89x/ha-car-assistant): die **Integrationen** und **Plugins**, die du unter *Hinzufügen* installieren kannst. Car Assistant liest dieses Repository nur, wenn du unter *Quellen* auf *Aktualisieren* tippst; gelesen werden nur Beschreibungen, ausgeführt wird nie etwas von hier.

## Was hier drin ist
- **Integrationen** (kein Programm, nur eine Beschreibung, die die App zeichnet): *Kraftstoff-Additiv* – ein Additiv-Plan, der mit jeder Tankung weiterrückt, mit Erinnerung und Verlauf; *Coding* – die Codierung der Steuergeräte, Werkswert neben aktuell, geänderte Bytes markiert.
- **Plugins** (Verbindungen nach außen): *Demo connector* spielt eine erfundene Fahrt ab; *Home Assistant* bringt Entitäten aus deinem Home Assistant – eine Wallbox, einen Tracker, die Integration deines Autos – in ein Fahrzeug, für jedes Fahrzeug einzeln, live (braucht Car Assistant ab 0.5.37).
- **Autos**: die beiden Demo-Autos kommen mit erfundenen Daten in jedem Modul – auch Ausstattung in allen zwölf Bereichen mit jedem Status, Luftdruck (normal und voll beladen), einer eigenen Hinterachse, Widgets (*Aufmerksamkeit*, *Fahrzeugdaten* und *Standort* als ganze Zeile) und einem eigenen Icon.

## Aufbau (die feste Regel)

```
integrations/
  index.json            alle Integrationen: id, name, description, version
  <id>/plugin.json      ein Ordner je Integration, benannt wie ihre id
plugins/
  index.json            alle Plugins
  <id>/plugin.json      ein Ordner je Plugin
```

`index.json`:

```json
{ "packages": [ { "id": "mein-plugin", "name": "Mein Plugin", "description": "Kurzer Text", "version": "1.0" } ] }
```

`plugin.json` ist die Beschreibung eines Pakets (id, name, version, description, author, homepage, settings); das Format steht in der `docs/plugins.de.md` der App. Die `version` muss in beiden Dateien gleich sein – eine höhere Zahl als die installierte bietet ein **Update** an.

## Autos (`vehicles/`)

`vehicles/index.json` listet Fahrzeug-Sicherungen, `vehicles/<id>.zip` ist eine Sicherung (gemacht mit *Fahrzeugdaten → Dieses Fahrzeug sichern* in Car Assistant). Sie werden unter *Fahrzeug hinzufügen* angeboten und wie eine hochgeladene Sicherung wiederhergestellt. Die zwei Demo-Autos (`demo-diesel`, `demo-electric`) verlangen das Plugin `demo-connector`, das alle 5 Sekunden eine erfundene Fahrt abspielt (siehe seinen Teil `simulation`).

## Eigenes Paket hinzufügen

1. `plugins/<id>/plugin.json` anlegen (oder `integrations/<id>/…`) – `<id>`: Kleinbuchstaben, Ziffern, `-`, `_`.
2. In der `index.json` daneben eintragen.
3. `python3 tools/check.py` ausführen – es muss `OK` ausgeben.
4. Pushen. In Car Assistant: *Integrationen / Plugins → Quellen → Aktualisieren*, dann erscheint es unter *Hinzufügen*.

## Diese Quelle in Car Assistant nutzen

*Integrationen → Quellen → Quelle hinzufügen*, die Adresse dieses Repositorys. Ein privates Repository braucht ein Zugriffs-Token mit Leserecht (bleibt auf deinem Server). Jeder kann dieses Repository forken und seine eigene Kopie genauso nutzen.

## Lizenz

GPL-3.0, siehe [LICENSE](LICENSE).
