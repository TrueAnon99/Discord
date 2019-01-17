# Lazy Guilds

**Note:** The lazy guild documentation described here does NOT represent the
added `guild_id` fields in some message/channel events. This documents
Unkown OP codes and mechanisms for optimization of the guild member list.

**Note:** This is not a complete document on how lazy guilds work, however, it
is lead to believe this is the most complete document on the topic.

**Note for Server implementors:** The documentation describes behaviors that are
non-normative for the Discord API so that it is easy to reimplement.

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

Once a client requests a certain range, it is considered "subscribed"
to that range and will receive respective `GUILD_MEMBER_LIST_UPDATE`
events related to those ranges.

**ASSUMPTION:** `typing` field means the client wants to be subscribed to the
ranges the currently-typing members are on.

**ASSUMPTION:** Ranges can have any size.

### OP 14 Structure

| field | type | description |
| --: | :-- | :-- |
| guild\_id | snowflake | the guild id for the request |
| channels | map[snowflake -> list[list[int, int]]] | channel ranges |
| members | unknown | unknown |
| activities | boolean | unknown |
| typing | boolean | unknown, see assumption about the nature of this field |

## `GUILD_MEMBER_LIST_UPDATE` event

This is the main event related to all lazy guild related work. It is sent by
the Server to indicate updates to the member list, but only to the ranges
the client specified in its OP 14.

### List IDs

Member List IDs are defined by an algorithm that takes the current
permission overwrites for the given channel. This is made to prevent duplicity
of data in both the client and server (if channels have the same permission
overwrites, they bsaically have the same member lists).

The algorithm is as follows, in pseudocode.

The pseudocode assumes `Permissions` to be parsing a given permissions number
into more readable fields, those are specified under Discord's API docs.

The pseudocode also assumes `mmh3` to be a function providing an implementation
of MurMurHash version 3.

```python
def list_id(channel) -> str:
    # list of strings holding the hash input
    hash_in = []

    for actor_id, overwrite in channel.channel_overwrites:
        allow, deny = (
            Permissions(overwrite['allow']),
            Permissions(overwrite['deny'])
        )

        if allow.read_messages:
            hash_in.append(f'allow:{actor_id}')
        elif deny.read_messages:
            hash_in.append(f'deny:{actor_id}')

    hash_in = ','.join(ovs_i)
    return str(mmh3(hash_in))
```

### Groups

Groups are a core concept of understanding lazy guilds. The maximum number of
groups is assumed to be the maximum number of roles a guild can have.

There are two default groups, and then a general rule for any group.

The default groups are the online members and the offline members.

After the default groups, all roles that have the `hoisted` property set to
true are considered groups.

#### Group object

| field | type | description |
| --: | :-- | :-- |
| id | snowflake OR "online" OR "offline" | group id |
| count | positive integer, includes 0 | the amount of members in that group |

### Event structure

| field | type | description |
| --: | :-- | :-- |
| id | string | the list being updated, output of the list\_id function |
| guild\_id | snowflake | the guild id being referenced |
| ops | list[Operator] | update operators |
| groups | list[Group] | group references |

### Operator

**TODO**
