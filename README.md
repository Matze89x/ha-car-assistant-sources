# Car Assistant - sources

🇬🇧 English · [🇩🇪 Deutsch](README.de.md)

The package source of [Car Assistant](https://github.com/Matze89x/ha-car-assistant): the **integrations** and **plugins** you can install under *Add*. Car Assistant reads this repository only when you press *Update* under *Sources*; it only reads descriptions and never runs anything from here.

## Layout (the fixed rule)

```
integrations/
  index.json            all integrations: id, name, description, version
  <id>/plugin.json      one folder per integration, named like its id
plugins/
  index.json            all plugins
  <id>/plugin.json      one folder per plugin
```

`index.json`:

```json
{ "packages": [ { "id": "my-plugin", "name": "My plugin", "description": "Short text", "version": "1.0" } ] }
```

`plugin.json` is the description of one package (id, name, version, description, author, homepage, settings); see the format in the app's `docs/plugins.md`. The `version` in both files must be the same - a higher number than the installed one offers an **Update**.

## Cars (`vehicles/`)

`vehicles/index.json` lists car backups, `vehicles/<id>.zip` is one backup (made with *Vehicle data -> Back up this vehicle* in Car Assistant). They are offered under *Add vehicle* and restored like an uploaded backup. The two demo cars (`demo-diesel`, `demo-electric`) ask for the plugin `demo-connector`, which plays a made-up drive every 5 seconds (see its `simulation` part).

## Add your own package

1. Create `plugins/<id>/plugin.json` (or `integrations/<id>/…`) - `<id>`: lower-case letters, digits, `-`, `_`.
2. List it in the `index.json` next to it.
3. Run `python3 tools/check.py` - it must print `OK`.
4. Push. In Car Assistant: *Integrations / Plugins → Sources → Update*, then *Add* shows it.

## Use this source in Car Assistant

*Integrations → Sources → Add source*, the address of this repository. A private repository needs a read-only access token (stays on your server). Anyone can fork this repository and use their own copy the same way.

## License

GPL-3.0, see [LICENSE](LICENSE).
