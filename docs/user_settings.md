# User Settings
Most settings of the client are stored here for syncing.

## `GET /users/@me/settings`
Retrieve settings

### Structure

| Field | Type | Description |
| --: | -- | :-- |
| afk_timeout | integer | How long from being idle from the client before you're marked as "AFK", this handles when you should get push notifications. |
| animate_emoji | boolean | Should animated emoji play without hovering over them |
| convert_emoticons | boolean | Should "old fashion" emoticons convert to emojis |
| default_guilds_restricted | boolean | "Allow direct messages from server members", true being off |
| detect_platform_accounts | boolean | Detect accounts from other services for connections |
| developer_mode | boolean | Allow copying of IDs from right click menus |
| disable_games_tab | boolean | Hides the activity tab |
| enable_tts_command | boolean | Enables /tts playback |
| explicit_content_filter | integer | Content filter level. 0 - off, 1 - friends excluded, 2 - scan everyone |
| friend_source_flags | object | Object defining who can add you as a friend. See [Friend Source Flags Structure](#friend_source_flags_structure). |
| gif_auto_play | boolean | Should GIFs play without hovering over them |
| guild_folders | array | Array of folder objects, see the page on [guild folders](/guild_folder.html) for more info. |
| guild_positions | array | Array of guild snowflakes, order matters |
| inline_attachment_media | boolean | Display images and video when uploaded directly |
| inline_embed_media | boolean | Display images and video when linked |
| locale | string | User defined locale |
| message_display_compact | boolean | Compact mode |
| render_embeds | boolean | Display embeds |
| render_reactions | boolean | Display reactions |
| restricted_guilds | array | Array of guild snowflakes of servers with "Allow direct messages from members" off |
| show_current_game | boolean | Shows playing status of detected/added games |
| status | string | Current status. Values: online, idle, dnd, invisible |
| theme | string | Client theme. Values: dark, light |
| timezone_offset | integer | Timezone offset. Arbitrary number, no way to change in client |
| custom\_status | CustomStatus | Set custom status. Structure defined in [Custom Status page](/custom_status.html) |

### Friend Source Flags Structure

All of these values are optional and only one will ever be set at a time, to set false, remove the key from the object

| Field | Type | Description |
| --: | -- | :-- |
| all | boolean | Anyone can add you |
| mutual_friends | boolean | Friends of friends can add you |
| mutual_guilds | boolean | Server members can add you |
