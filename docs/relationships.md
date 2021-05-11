# Relationships

## Relationship object

| field | type | description |
| --: | :-- | :-- |
| id | snowflake | user id the relationship is about |
| type | RelationshipType | relationship type |
| user | User | user object |

## RelationshipType enum

| value | description |
| --: | :-- |
| 1 | friend |
| 2 | block |
| 3 | incoming friend request |
| 4 | outgoing friend request |

## `GET /users/@me/relationships`

Get all relationships on the currently authenticated user. Returns a list
of Relationship objects.

## `POST /users/@me/relationships`

Create a relationship. If a User wants to create a friendship request, the
`type` in the relationship object MUST be a friendship type, NOT an incoming
or outgoing request.

## `PUT /users/@me/relationships/<peer_id>`

Another route to create a relationship. *for some reason.*

Input is only a JSON object with the `type` field (for a RelationshipType
value).

## `DELETE /users/@me/relationships/<peer_id>`

Remove a relationship targeted at a certain peer.
Returns empty response 204.

## `GET /users/<peer_id>/relationships`

Get mutual friends with a certain peer. Returns a list of user objects.

# `PATCH /users/users/@me/relationships/<peer_id>`
Used for setting a friend nickname.
Body data is a JSON object with the property (string) nickname.
The nickname could be removed by setting the nickname property to null.

## `RELATIONSHIP_ADD` event

Contains a Relationship object in the `d` field.

## `RELATIONSHIP_REMOVE` event

Contains a partial Relationship object in the `d` field. Partial Relationship
object contains `type` and `id` fields only.
