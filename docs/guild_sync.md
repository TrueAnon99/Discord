# Guild Sync

## OP 12 Guild Sync

This is an undocumented OP code used by some discord libraries to fetch
presence information on guilds. It *was* used by the official client, however,
nowadays, it uses lazy guilds. Look more over its
[own documentation](/lazy_guilds.html)

The data in the `d` field isn't a object with fields (as other OP codes do),
but it's a list of guild IDs.

It is presumed that the client will get a Guild Sync event for every given
guild ID, as long as the connected user has authorization for the guild.

## Guild Sync event

Sent as a response to the guild list given in OP 12 Guild Sync.

| field | type | description |
| --: | :-- | :-- |
| id | snowflake | the guild id |
| presences | List[Presence] | list of presence objects for the guild |
| members | List[Member] | list of member objects for the guild |
