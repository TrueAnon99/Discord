# Integrations
Integrations are like connections but for guilds, being things like YouTube and Twitch.

## `INTEGRATION_UPDATE` Event
This event is fired to clients when an integration syncs.

| field | type | description |
| --: | :-- | :-- |
| user | user | User object of the integration owner |
| type | string | Integration type, either `"twitch"` or `"youtube"` |
| syncing | boolean | Whether the sync was manual <sup>needs confirmation</sup> |
| synced_at | timestamp | When the sync occurred |
| subscriber_count | int | Subscriber/Member count, depending on platform |
| role_id | snowflake | Role for the integration **Note:** This does not include tiered Twitch roles |
| revoked | boolean | Whether the integration is revoked or not. prerequisites unknown. |
| name | string | Channel name of the integration |
| id | snowflake | The integration's snowflake |
| expire_grace_period | int | Grace period for members expiration in days. Options are 1, 3, 7, 14, 30 |
| expire_behavior | int? | Behavior of what to do with member expiration. Options are 0 - Remove role, 1 - Kick. Could potentially be a bitflag. |
| enabled | boolean | Whether the integration is enabled |
| enable_emoticons | boolean | Whether emotes are copied to the guild and usable by integration members |
| account | object | External account info |
| guild_id | snowflake | Snowflake of the guild the event fired from |

### External account object

| field | type | description |
| --: | :-- | :-- |
| name | string | Display name from the external service |
| id | string | Interal ID from the external service |
