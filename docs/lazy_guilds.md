# Lazy Guilds

**Note:** The lazy guild documentation described here does NOT represent the
added `guild_id` fields in some message/channel events. This documents
Unkown OP codes and mechanisms for optimization of the guild member list.

**Note:** This is not a complete document on how lazy guilds work, however, it
is lead to believe this is the most complete public document on the topic.

**Note for Server implementors:** The documentation describes behaviors that are
non-normative for the Discord API so that it becomes easier to reimplement.

The documentation is heavily based on [Litecord]'s [implementation of lazy
guilds](lazy-guild-impl).

[Litecord]: https://gitlab.com/litecord/litecord
[lazy-guild-impl]:https://gitlab.com/litecord/litecord/blob/master/litecord/pubsub/lazy_guild.py

## Known history

Lazy guilds were first implemented because of known stresses caused by the
Fortnite Discord guild. The existing tooling to handle big guilds were not
enough for something as big as Fortnite (e.g Guild Sync).

Limitations of the old member list methods (Guild Sync, Request Guild Members)
were already known to not scale well at large guilds. One of the first big
examples was the original Blobs guild. The course of events goes as this:
 - An at-everyone ping happened in the guild, causing a big spike in
   internal server traffic as the notification subsystem fans it out to users.
 - Users open the server. Many. This part is important, because the client
   subscribes to the guild via (what that time was) guild sync.
 - The large influx of subscriptions also caused large subscriptions to the
   member list, and considering Blobs has many members, there's a very high
   chance of the first 1K members in the guild going online or offline. You were
   able to see the online counts changing quickly.
 - If enough subscriptions were done, the Guild genserver powering the Blobs
   guild would crash, and so all users would find the infamous
   "unavailable guild" icon on their clients.

(Keep in mind the above "line of events" was not in any way confirmed by
Discord, and is a collection of "best guesses" by non-Discord-employees)

Lazy guilds were deployed on the guild and it was a success, now all the guilds
have that feature enabled.
The official client only uses Lazy Guild methods from now on.
It is unknown when *exactly* this was done. The other guild presence fetch
methods still exist and are functional for backwards-compatibility's sake are:
 - OP 8 Request Guild Members
 - OP 12 Guild Sync

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

Once a client requests a certain range, it is considered "subscribed"
to that range and will receive respective `GUILD_MEMBER_LIST_UPDATE`
events related to those ranges.

**ASSUMPTION:** `typing` field means the client wants to be subscribed to the
ranges the currently-typing members are on.

**ASSUMPTION:** Ranges can have any size, except negative.

### OP 14 Structure

| field | type | description |
| --: | :-- | :-- |
| guild\_id | snowflake | the guild id for the request |
| channels | map[snowflake -> list[list[int, int]]] | channel ranges |
| members | unknown | unknown |
| activities | boolean | unknown |
| typing | boolean | unknown, check assumptions |

## `GUILD_MEMBER_LIST_UPDATE` event

This is the main event related to all lazy guild related work. It is sent by
the Server to indicate updates to the member list, but only to the ranges
the client specified in its OP 14.

### List IDs

Member List IDs are defined by an algorithm that takes the current
permission overwrites for the given channel. This is made to prevent duplicity
of data in both the client and server (if channels have the same permission
overwrites, they bsaically have the same member lists).

The algorithm is as follows, in Python:

 - Assumes that `Permissions` parses a given permissions number
   into more readable fields, those are specified under Discord's API docs.

 - Assumes `mmh3` to be a function providing an implementation of
   MurMurHash version 3.

This was taken off [Litecord]'s implementation. Type hints are provided for
nicer understanding.

```python
def list_id(channel: Channel) -> str:
    # list of strings holding the hash input
    hash_in: List[str] = []

    # actor_id is a snowflake, representing either a user or a role
    # overwrite is Dict[str, int]
    for actor_id, overwrite in channel.channel_overwrites:
        allow = Permissions(overwrite['allow'])
        deny = Permissions(overwrite['deny'])

        if allow.read_messages:
            hash_in.append(f'allow:{actor_id}')
        elif deny.read_messages:
            hash_in.append(f'deny:{actor_id}')

    mm3_in = ','.join(hash_in)
    return str(mmh3(mm3_in))
```

### Groups

Groups are a core concept of understanding lazy guilds. The maximum number of
groups is assumed to be the maximum number of roles a guild can have.

There are two default groups, and then a general rule for any group:
 - The default groups are the online members and the offline members.
 - After the default groups, all roles that have the `hoisted` property set
   are considered groups.

Groups are ordered by the same order roles are, with the online and offline
coming in last, respectively.

#### Group object

| field | type | description |
| --: | :-- | :-- |
| id | snowflake OR "online" OR "offline" | group id |
| count | unsigned number | the amount of members in that group |

### Event structure

| field | type | description |
| --: | :-- | :-- |
| id | string | the list being updated, output of the list\_id function |
| guild\_id | snowflake | the guild id being referenced |
| ops | list[Operator] | update operators |
| groups | list[Group] | group references |

### Operator

Operator objects represent operations a client MUST act upon to achieve
a synchronized member list with the server. The client MUST process each
operator based on the given order by the `GUILD_MEMBER_LIST_UPDATE` event.

 - `range` is present if `op` is any of: `"SYNC"`, `"INVALIDATE"`
 - `items` is present if `op` is equal to `"SYNC"`
 - `index` is present if `op` is any of: `"INSERT"`, `"DELETE"`, `"UPDATE"`
 - `item` is present if `op` is any of: `"INSERT"`, `"UPDATE"`

| field | type | description |
| --: | :-- | :-- |
| op | OperatorType | operator type for the list |
| range | list[int, int] | range being operated upon |
| items | list[SyncItem] | the list of items related to the range given |
| index | positive integer, includes 0 | the item being acted upon |
| item | SyncItem | new item for the index |

#### SyncItem

It can be a Group object, or a member object with a `presence` field attached.

## Implementation Notes

*This section is non-normative. This is also aimed at server implementors
wanting to implement Lazy Guilds. Clients only bother with the
`GUILD_MEMBER_LIST_UPDATE` events*

For `SYNC` events, server implementors can assume the `index`
is an index in a list composed of, for every group in the list, by:
 - a group object
 - members in that group

With the given list, make slices out of the list based on the requested
ranges by the client. This approach is known to work, but it is not known
if the list generation method is the same used by Discord. Proceed with care.

For guidelines on when to update the list, here follows an informal list
of state changes to a list. For a member:
 - A member moves from offline group to any other group (presence change).
 - A member moves from any group to the offline group (presence change).
 - A member moves from any group to any other group (role changes).
 - A member moves from a group G to the same G, while changing their position
    in the group (nickname changes).
 - A member moves from a group G to the same G, while not changing their
    position in the group ("simple" presence changes).

The fifth state change is the simplest to handle, it can be caused by a
member going from *online* to *idle* while maintaining their roles. The others
are more complex and cane grouped into two categories: simple presence update
and complex presence update.

The "presence update" sentence is not always tied to a presence, it represents
an update to member state, and while that includes roles, it also includes
the member's nickname and current presence (status is enough). Complex presence
updates always involve a member going from an old group to a new group. Simple
presence updates only involve an update of the state at the same group.

When implementing complex presence updates, server implementors are recommended
to use a single `SYNC` operator (given the correct information, e.g ranges)
instead of calculating the correct order / appearance of `INSERT` / `UPDATE`
/ `DELETE` operators.

When implementing this server-side, it is valid behavior to send a `SYNC`
operator to the client (given the correct range) instead of calculating
the correct `INSERT` / `UPDATE` / `DELETE` operators.

The simplifying behavior is caused by unstability in the `index` property, It
is currently unknown the governing rules about the property, esp. when it
starts, or ends, or what enters the index or what doesn't, etc.

There are other related state changes to the list that are *related* to members
but not related to the actual member state (or are, but aren't tied to a
single member):
 - A role being created with hoisted property set to true (a new group).
 - A role having its position updated (group changes position).
 - A role having its hoisted property set to false (removal of a group).
 - A new member joining (creation of a member in a group, most probably
   auto-inserting them into the online group).
 - A member leaving (be it via a kick or a ban, they all have the same
   meaning to the member list).
 - A member updating its user information (such as avatar or username).
