# Science Events

Events are actions the User does that are collected by Discord. More information
on tracking and collection [here](/science.html).

This gives a non-thorough list of Event objects.

If an event "contains properties" it is assumed that the Event object contains
an extra `properties` field pointing to a Properties object.

Always assume `TrackingProperties` is included.

## Properties object

Fields are inconsistent and optional across events. Given *Property "objects"
are fields that may or may not be present in a Properties object.

### `TrackingProperties`

| field | type | description |
| --: | :-- | :-- |
| client\_send\_timestamp | unix timestamp | assumed to be when client sent event |
| client\_track\_timestamp | unix timestamp | assumed to be when the event happened |
| client\_uuid | base64 of a uuid? | client identifier |

### `ChannelProperties`

| field | type | description |
| --: | :-- | :-- |
| channel\_hidden | boolean | if the channel is muted (???) |
| channel\_id | snowflake | channel the user is in |
| channel\_member\_perms | permission bit set (integer) | the user permissions in the channel |
| channel\_size\_total | integer | ??? |
| channel\_type | integer, channel type | channel type (text, voice, etc) |

### `GuildProperties`

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

### `ListProperties`

| field | type | description |
| --: | :-- | :-- |
| num\_users\_visible | integer | amount of users the current user saw in the list |
| num\_users\_visible\_with\_mobile\_indicator | integer | self explanatory |

### `ActivityProperties`

| field | type | description |
| --: | :-- | :-- |
| game\_ids | list of snowflakes | game ids |
| load\_id | uuid as its formal representation (incl. hyphens) | ??? |
| num\_cards | integer | number of game cards in activity |
| num\_cards\_game\_news | integer | number of game cards showing game news |
| num\_cards\_game\_playable | integer | number of cards user can play |
| num\_cards\_visible | integer | number of cards user views when looking at activity |
| num\_game\_parties | integer | ??? |
| num\_game\_parties\_collapsed | integer | ??? |
| num\_game\_parties\_recently\_played | integer | ??? |
| num\_game\_parties\_rich\_presence | integer | ??? |
| num\_game\_parties\_solo | integer | ??? |
| num\_game\_parties\_voice | integer | ??? |
| num\_launcher\_applications | integer | ??? |
| num\_users\_subscribed | integer | ??? |

### `ActivityCloseProperties`

| field | type | description |
| --: | :-- | :-- |
| game\_ids\_viewed | list of snowflakes | game ids the user viewed while in activity |
| load\_id | uuid as its formal representation (incl. hyphens) | ??? |
| num\_cards\_total | integer | number of game cards in activity |
| num\_cards\_viewed | integer | number of cards user saw while in activity |
| num\_games\_total | integer | number of games seen in activity |
| seconds\_spent | integer | amount of seconds spent in activity view |
| store\_application\_ids\_viewed | list of snowflakes | application ids the user viewed |
| store\_sku\_ids\_viewed | list of snowflakes | skus the user viewed |

 - SKUs can be thought of as discord Store entries (Stock Keeping Unit).

### `WindowProperties`

| field | type | description |
| --: | :-- | :-- |
| window\_height | integer | client window height in pixels |
| window\_width | integer | client window width in pixels |

# Event types

## `member_list_viewed`

Sent when the currently authenticated User sees a newly generated member list
in a guild. Contains ChannelProperties, GuildProperties and ListProperties.

## `ack_messages`

Sent when the current User acknowledged the messages in a channel. Contains
ChannelProperties, optional GuildProperties.

## `dm_list_viewed`

Sent when the current User views the Direct Messages they currently have.
Contains ChannelProperties (for the current opened DM) and ListProperties.

## `channel_opened`

Sent when the current User opens a channel. Can be a Guild Text Channel or a
DM channel. Contains ChannelProperties.

## `af_loaded`

Related to client startup? Definitely related to the Activity view.
Contains ActivityProperties, WindowProperties.

## `af_exited`

Sent when the user leaves the Activity view. Contains ActivityCloseProperties.

## `open_popout`

Sent when the user opens any kind of popout (such as when adding a new member
to a group DM). Contains ChannelProperties, plus some fields:

| field | type | description |
| --: | :-- | :-- |
| is\_friend | boolean | if the dm you're on represents a friend dm |
| source | string | source of the popout, known value is `"DM"` |
| type | string | type of the popout, known value is `"Add Friends to DM"` |
