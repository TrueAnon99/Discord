# Stickers

**Stickers** in Discord are just like stickers in Telegram; they're animated pictures that are displayed bigger than emojis. Stickers are currently (January 28 2021) only available for users from Brazil, Canada, and Japan "for the soft launch."[^1] We don't know if it's going to be able to add custom stickers, but you can *buy* **sticker packs** from the store.

## Sticker object

```json
{
  "id": string,
  "name": string, // based on the locale?
  "description": string, // same thing as `tags`?
  "pack_id": string,
  "asset": string, // id on the discord cdn
  "preview_asset": string, // another id on the discord cdn
  "format_type": integer,
  "tags": string
}
```

### Example

```json
{
  "id": "748293342357356564",
  "name": "Scared",
  "description": "wumpus, scared, woah, scary, scream, :o, spooked, 😨, 😱, :scared, :scream",
  "pack_id": "748286863302852648",
  "asset": "17e05030dcafa6604ee7479789652459",
  "preview_asset": "c5ca5d803b37604638c32e68cb629b1a",
  "format_type": 2,
  "tags": "wumpus, scared, woah, scary, scream, :o, spooked, 😨, 😱, :scared, :scream"
}
```

## Sticker pack object

```json
{
  "id": string,
  "stickers": [Sticker],
  "name": string, // based on the locale?
  "sku_id": string,
  "cover_sticker_id": string
}
```

### Example

```json
{
  "id": "755240383084232756",
  "stickers": [/* Many sticker objects */],
  "name": "Wumpus Nitro Elite",
  "sku_id": "755240383084232754",
  "cover_sticker_id": "755244316976218142"
}
```

## Extended sticker pack object

```json
{
  "user_id": string,
  "pack_id": string,
  "entitlement_id": string,
  "has_access": bool,
  "premium_type_required"?: integer, // nitro i guess
  "sticker_pack": StickerPack
}
```

### Example

```json
{
  "user_id": "270361773662535681", // see special thanks
  "pack_id": "755240383084232756",
  "entitlement_id": "789335049324462121",
  "has_access": false,
  "premium_type_required": 2,
  "sticker_pack": {
    "id": "755240383084232756",
    "stickers": [/* Many sticker objects */],
    "name": "Wumpus Nitro Elite",
    "sku_id": "755240383084232754",
    "cover_sticker_id": "755244316976218142"
  }
}
```

## `GET /api/users/@me/sticker-packs`

An **authorized** API endpoint without any parameters that returns the current sticker packs this user owns.

### Response

```json
[ExtendedStickerPack]
```

### Example response

```json
[
  {
    "user_id": "270361773662535681", // see special thanks
    "pack_id": "755240383084232756",
    "entitlement_id": "789335049324462121",
    "has_access": false,
    "premium_type_required": 2,
    "sticker_pack": {
      "id": "755240383084232756",
      "stickers": [/* Many sticker objects */],
      "name": "Wumpus Nitro Elite",
      "sku_id": "755240383084232754",
      "cover_sticker_id": "755244316976218142"
    }
  }
]
```

## Sticker messages

Sticker messages are an extended version of regular messages, though they are not embedded. 
By specifying an empty `content` string and adding sticker IDs into the array of strings `sticker_ids`, you can send a sticker message.
It can also return these errors:
- `403 Forbidden {"message": "Cannot use this sticker", "code": 50081}`: It can mean that:
  - You haven't paid for this sticker pack
  - You have provided an invalid or malformed ID
  - Stickers are not available in your country

## Special thanks
- To Brazilian **Kyatsuu**#5359 (270361773662535681) for following my instructions to reverse-engineer this.


[^1]: https://support.discord.com/hc/en-us/articles/360056891113-Stickers-FAQ
