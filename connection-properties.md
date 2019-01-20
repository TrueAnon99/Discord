# Connection Properties

The connection properties described here are beyond the `$os`, `$browser` and
`$device` properties. They're used by official clients to give more metadata
to Discord about the currently running device.

Fields for connection properties seem to be optional, except
for `os`, `browser` and `device`.

| field | type | description |
| --: | :-- | :-- |
| `browser` | string | browser string, `Discord Client` / `Discord Android`|
| `browser_user_agent` | string | the user agent for the device |
| `client_build_number` | integer | the client's build number |
| `client_event_source` | unknown | unknown |
| `client_version` | string | the client's version |
| `device` | string | device identifier |
| `device_id` | string | device identifier |
| `distro` | string | your distribution of linux |
| `os` | string | your operating system identifier |
| `os_arch` | string | your device architecture, e.g `"x86"` |
| `os_version` | string | your device os version, e.g `4.20-1-arch1-1-ARCH` |
| `release_channel` | string | the client's release channel, `stable`, `ptb`, `canary` |
| `window_manager` | string | contains your desktop environment and window manager |
