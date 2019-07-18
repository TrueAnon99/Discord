# Guild Folders
Guild folders (also called server folders) let you sort your guilds.

## `PATCH /users/@me/settings`
Folder creation is stored and handled by user settings.

### Structure

| Field | Type | Description |
| --: | -- | :-- |
| guild_folders | array | Array of folder objects |

### Folder Object

| Field | Type | Description |
| --: | -- | :-- |
| id | snowflake | folder id |
| guild_ids | array of guild snowflakes | guilds in the folder |
| name | string | name of the folder |
