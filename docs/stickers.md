# Stickers

**Stickers** in Discord are just like stickers in Telegram; they're animated pictures that are displayed bigger than emojis. Stickers are currently (January 28 2021) only available for users from Brazil, Canada, and Japan "for the soft launch."[^1] We don't know if it's going to be able to add custom stickers, but you can *buy* **sticker packs** from the store.

## Animation formats

Discord uses 2 formats of stickers right now (even though there's 3rd one):
- **PNG**: Unused
- **APNG**: Used for some stickers that usually look worse than **Lottie** stickers.
- **Lottie**: Used for clean animation in some stickers. Lottie animations are rendered in Discord using [Discord's rlottie](https://github.com/discord/rlottie), a fork of [Telegram's rlottie](https://github.com/TelegramMessenger/rlottie).

## Sticker object

| field         | type    | description |
| --:           | :--     | :-- |
| id            | string  | unique ID of this sticker |
| name          | string  | display name of this sticker (might be localized on the client?) |
| description   | string  | display description of this sticker (in the store?) (might be localized on the client?). same thing as `tags` for older packs |
| pack_id       | string  | the ID of the pack this sticker belongs to |
| asset         | string  | asset ID on the CDN |
| preview_asset | string? | asset ID of preview (in the store?) |
| format_type   | integer | format of the asset. 1 for png, 2 for apng, 3 for lottie |
| tags          | string  | search tags for this sticker |

### Examples

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
```json
{
  "asset": "e71c2fc3e471f663dd78189d7b01b52d",
  "description": "Wumpus crying into his helmet",
  "format_type": 3,
  "id": "755242820368859196",
  "name": "Crying",
  "pack_id": "755240383084232756",
  "preview_asset": null,
  "tags": "wumpus, cry, crying, sad, upset, feelsbadman, :<, :(, :[, 😥, 😢, 😭, ):, tear, :sad, :tear, :cry"
}
```

## Sticker pack object

| field            | type          | description |
| --:              | :--           | :-- |
| id               | string        | unique ID of this pack |
| stickers         | list[Sticker] | the stickers that this pack provides |
| name             | string        | display name of this pack (might be localized on the client?) |
| sku_id           | string        | just SKU ID |
| cover_sticker_id | string        | id of the "example sticker" in this pack |

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

## <a name="per-user-sticker-pack"></a> Per-user sticker pack object

| field                  | type        | description |
| --:                    | :--         | :-- |
| user_id                | string      | id of this user |
| pack_id                | string      | id of the sticker pack |
| entitlement_id         | string      | unknown purpose |
| has_access             | boolean     | is this user an owner of the pack |
| premium_type_required? | integer     | nitro level required to have the pack (0 for none, 1 for classic, 2 for full) |
| sticker_pack           | StickerPack | composition > inheritence |

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

An array of per-user [sticker pack objects](#per-user-sticker-pack).

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

Sticker messages are an extended version of regular messages, though stickers are not embedded. 
By specifying an empty `content` string and adding sticker IDs into the array of strings `sticker_ids`, you can send a sticker message.

### Errors
- `403 Forbidden {"message": "Cannot use this sticker", "code": 50081}`: It can mean that:
  - You haven't paid for this sticker pack
  - You have provided an invalid or malformed ID
  - Stickers are not available in your country

### Example payload

```json
{
  "content": "",
  "nonce": "804415164441952256",
  "sticker_ids": ["748293342357356564"],
  "tts": false
}
```

## Special thanks
- To Brazilian **Kyatsuu**#5359 (270361773662535681) for following my instructions to reverse-engineer this.


[^1]: https://support.discord.com/hc/en-us/articles/360056891113-Stickers-FAQ
