# Client-side Interactions

## OP 24 'Request Interactions'
Used by the client to retreive a list of interactions. Gateway responds with GUILD_APPLICATION_COMMANDS_UPDATE event.

| field | type | description |
| --: | :-- | :-- |
| `applications` | boolean   | false when using slash commands (documentation needed)
| `guild_id`     | snowflake | ID of guild to query interactions for
| `limit`        | integer   | How many interactions to return
| `nonce`        | string    | Nonce, used for the event returning the data
| `offset`       | integer   | 0-indexed offset for retrieving interactions

## `GUILD_APPLICATION_COMMANDS_UPDATE` event
Returns the data for OP 24

| field | type | description |
| --: | :-- | :-- |
| `application_commands` | list[ApplicationCommand] | list of application commands |
| `applications`         | list[Application]        | list of applications         |
| `guild_id`             | snowflake                | the same id used in OP 24    |
| `nonce`                | string                   | the same nonce used in OP 24 |
| `updated_at`           | unix timestamp           | when the interactions were updated. this is not relative to the discord epoch |

### Application
| field | type | description |
| --: | :-- | :-- |
| `bot`           | Bot       | partial user structure of the bot
| `command_count` | integer   | how many application commands does this application have
| `icon`          | string    | avatar hash of the application
| `id`            | snowflake | id of the application
| `name`          | string    | name of the application

#### Bot
| field           | type      | description
| --:             | :--       | :--
| `avatar`        | string    | avatar hash
| `bot`           | boolean   | always true
| `discriminator` | string    | discriminator of the bot
| `id`            | snowflake | id of the bot
| `public_flags`  | integer   | flags of the bot (check discord official docs)
| `username`      | string    | username of the bot

### ApplicationCommand
| field                | type                               | description
| --:                  | :--                                | :--
| `application_id`     | string                             | id of the app who owns this command
| `default_permission` | boolean                            | whether the command is enabled by default in this guild
| `description`        | string                             | description of this command (1-100 characters)
| `id`                 | snowflake                          | id of this command
| `name`               | string                             | name of this command (1-32 lowercase characters)
| `permissions`        | list[[ApplicationCommandPermission]](https://discord.com/developers/docs/interactions/slash-commands#applicationcommandpermissions)  | the permissions for the command in the guild
| `version`            | snowflake                          | ??? (documentation needed)

## POST `/interactions`
Use an interaction. Takes a InteractionBody and responds with 204. Also sends gateway events INTERACTION_CREATE and INTERACTION_SUCCESS/INTERACTION_FAILURE.

### InteractionBody
| field                | type                               | description
| --:                  | :--                                | :--
| `application_id`     | snowflake                          | id of application to use command for
| `channel_id`         | snowflake                          | id of the channel of the interaction
| `data`               | InteractionBodyData                | data of the interaction
| ?`guild_id`          | snowflake                          | if interaction was in a guild, its id
| `nonce`              | string                             | nonce for responding in interaction create and success events
| `type`               | integer                            | ??? (documentation needed) with slash commands, type = 2

## `INTERACTION_CREATE` event
Responds to /interactions.
data: InteractionResponseBody

## `INTERACTION_SUCCESS` event
Sent after INTERACTION_CREATE if the event was successful.
data: InteractionResponseBody

## `INTERACTION_FAILED` event
Sent after INTERACTION_CREATE if the event failed.
data: InteractionResponseBody

### InteractionResponseBody
| field   | type      | description
| --:     | :--       | :--
| `id`    | snowflake | maybe id of this event (???) (documentation needed)
| `nonce` | snowflake | nonce in POST /interactions
