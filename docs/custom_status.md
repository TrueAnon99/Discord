# Custom Statuses

Custom Statuses are the generalization of activites in Discord presences.

Users are able to set an emoji and any text, and it will be used, verbatim,
inside the presence.

## Changes

### Patch User Settings

The Patch User Settings route gets `custom_status`.

### CustomStatus structure

Called when the user wishes to update their **persistent** custom status.

The presence of a user regarding custom status is decided on 3 states:
 - On login, which loads the *persistent* custom status, and decides to invalidate it (if expired), or load it
 - From time to time the *persistent* custom status is checked for expiration
 - On OP 3 Status Update with an Activity of type 4

Clients SHOULD both update the user settings *always* and only send an
OP 3 Status Update *if necessary.*

Note persistent custom status updates don't propagate any gateway side-effects,
**for setting.** Expiration is likely to be accounted for in here.

| field | type | description |
| --: | :-- | :-- |
| text | string | Custom Status text |
| expires\_at | Optional[ISO8601 timestamp] | Timestamp in which the Custom Status expires. null for never expire |
| emoji\_name | string | Emoji name |
| emoji\_id | Optional[snowflake] | Emoji ID, null if unicode emoji |

### Type 4 Activity (CustomActivity)

| field | type | description |
| --: | :-- | :-- |
| state | string | Custom Status description |
| emoji | Optional[CustomStatusEmoji] | Custom Status emoji, if any |

#### CustomStatusEmoji

| field | type | description |
| --: | :-- | :-- |
| emoji_id | Optional[snowflake] | Emoji ID, null if emoji is unicode |
| emoji_name | string | Emoji name, unicode emoji goes here, as well as custom emoji |
| animated | boolean | If the Emoji is animated |
