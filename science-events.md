# Science Events

Events are actions the User does that are collected by Discord. More information
on the `science.md` file.

This gives a non-thorough list of Event objects.

If an event "contains properties" it is assumed that the Event object contains
an extra `properties` field pointing to a Properties object.

## Properties object

Fields are inconsistent and optional across events.

| field | type | description |
| --: | :-- | :-- |
| channel\_hidden | boolean | if the channel is muted (???) |
| channel\_id | snowflake | channel the user is in |
| channel\_member\_perms | permission bit set (integer) | the user permissions in the channel |
| channel\_size\_total | integer | ??? |
| channel\_type | integer, channel type | channel type (text, voice, etc) |
| client\_send\_timestamp | unix timestamp | assumed to be when client sent event |
| client\_track\_timestamp | unix timestamp | assumed to be when the event happened |
| client\_uuid | base64 of a uuid? | client identifier |

Fields specific to guild-related events:

| field | type | description |
| --: | :-- | :-- |
| guild\_id | snowflake | guild identifier |
| guild\_is\_vip | boolean | if the guild is a VIP guild |
| guild\_member\_num\_roles | integer | how many roles the user has in the guild |
| guild\_member\_perms | permission bit set (integer) | the user permissions in the guild |
| guild\_num\_channels | integer | amount of channels in the guild |
| guild\_num\_roles | integer | amount of roles in the guild |
| guild\_num\_text\_channels | integer | amount of text channels in the guild |
| guild\_num\_voice\_channels | integer | amount of voice channels in the guild |
| guild\_size\_total | integer | amount of members in the guild |

Fields specific to member lists / DM list:

| field | type | description |
| --: | :-- | :-- |
| num\_users\_visible | integer | amount of users the current user saw in the list |
| num\_users\_visible\_with\_mobile\_indicator | integer | self explanatory |

## `member_list_viewed`

Sent when the currently authenticated User sees a newly generated member list
in a guild. Contains properties.

## `ack_messages`

Sent when the current User acknowledged the messages in a channel. Contains
properties.

## `dm_list_viewed`

Sent when the current User views the Direct Messages they currently have.
Contains properties.

## `channel_opened`

Sent when the current User opens a channel. Can be a Guild Text Channel or a
DM channel. Contains properties.
