# Lazy Guilds

**Note:** The lazy guild documentation described here does NOT equate to the
added `guild_id` fields in some message/channel events. This documents
Unkown OP codes and mechanisms for optimization of the guild member list.

## Known history

Lazy guilds were first implemented because of known stresses cause by the
Fortnite Discord guild. The existing tooling to handle big guilds were not
enough for something as big as Fortnite (e.g Guild Sync).

They were deployed on the guild and it was a success, now all the guilds have
that feature enabled. The official client only uses Lazy Guild methods from now
on. It is unknown when *exactly* this constraint was added.

## OP 14 "Lazy Request"

This OP Code is undocumented. "Lazy Request" is an unofficial name taken
by this documentation.

OP 14 is used by the client when wanting to load the member list of a guild.

When the client wants to load the member list, it describes its request
in detail. That is what the `channels` field is for. It explicitly says
which parts of the member list the client wants.

For example, in the official client, it preloads the first 100 members in
the list, then requesting more as time goes by, so the only range being
requested in its OP 14 is `[0, 99]`.

Once a client requests a certain range, it is assumed to be "subscribed"
to that range and will receive respective `GUILD_MEMBER_LIST_UPDATE`
events related to the ranges it is subscribed to.

### OP 14 Structure

| field | type | description |
| --: | :-- | :-- |
| guild\_id | snowflake | the guild id for the request |
| channels | map[snowflake -> list[list[int, int]]] | channel ranges |
| members | unknown | unknown |
| activities | boolean | unknown |
| typing | boolean | unknown |

## `GUILD_MEMBER_LIST_UPDATE` event

**TODO**
