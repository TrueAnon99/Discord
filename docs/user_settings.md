# User Settings
Most client settings are stored here for syncing.

## `GET /users/@me/settings`
Returns a [user settings](#user-settings-structure) object for the requester's account.

### User Settings Structure

| Field | Type | Description |
| -- | -- | -- |
| afk_timeout | integer | how many seconds being idle before the user is marked as "AFK"; this handles when push notifications are sent |
| allow_accessibility_detection | boolean | unknown |
| animate_emoji | boolean | play animated emoji without hovering over them |
| animate_stickers | integer | when stickers animate; `0`: always, `1`: on hover/focus, `2`: never |
| contact_sync_enabled | boolean | sync phone contacts with discord (seemingly unused, enabling contact sync does not change it) |
| convert_emoticons | boolean | convert "old fashioned" emoticons to emojis |
| custom_status | [custom status](/custom_status.html#customstatus-structure) object | custom status for the user |
| default_guilds_restricted | boolean | allow DMs from guild members by default on guild join |
| detect_platform_accounts | boolean | whether the client will detect accounts from other services for connections |
| developer_mode | boolean | show the option to copy ids in right click menus |
| disable_games_tab | boolean | hide the activity tab |
| enable_tts_command | boolean | enable /tts command and playback |
| explicit_content_filter | integer | content filter level; `0`: off, `1`: friends excluded, `2`: scan everyone |
| friend_discovery_flags | integer | [flags](#friend-discovery-flags) for how people can add the user via contact sync |
| friend_source_flags | [friend source flags](#friend-source-flags-structure) object | who can add the user as a friend |
| gif_auto_play | boolean | play GIFs without hovering over them |
| guild_folders | array of [guild folder](/guild_folders.html#folder-object) objects | guild folders set by the user |
| guild_positions | array | array of guild ids in order of position on the sidebar |
| inline_attachment_media | boolean | display images and video when uploaded directly |
| inline_embed_media | boolean | display images and video when linked |
| locale | string | user defined locale |
| message_display_compact | boolean | use compact mode |
| native_phone_integration_enabled | boolean | unknown |
| render_embeds | boolean | display embeds |
| render_reactions | boolean | display reactions |
| restricted_guilds | array | array of guild ids where the user has disallowed DMs from guild members |
| show_current_game | boolean | show playing status for detected/added games |
| status | string | current status; values: `online`, `idle`, `dnd`, `invisible` |
| stream_notifications_enabled | boolean | unknown |
| theme | string | client theme; values: `dark`, `light` |
| timezone_offset | integer | timezone offset in minutes (arbitrary number, no way to change in client) |
| view_nsfw_guilds | boolean | allow access to NSFW guilds from iOS devices |

### Friend Discovery Flags

| Value | Description |
| -- | -- |
| 0 | None |
| 1 << 0 | User can be added by phone number
| 1 << 1 | User can be added by email

### Friend Source Flags Structure

All of these fields are optional. To set false, either set the value to false or remove the field from the object.

| Field | Type | Description |
| -- | -- | -- |
| all | ?boolean | Anyone can add you |
| mutual_friends | ?boolean | Friends of friends can add you |
| mutual_guilds | ?boolean | Server members can add you |
