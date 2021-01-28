# Stickers

**Stickers** in Discord are just like stickers in Telegram; they're animated pictures that are displayed bigger than emojis. Stickers are currently (January 28 2021) only available for users from Brazil, Canada, and Japan "for the soft launch."[^1] We don't know if it's going to be able to add custom stickers, but you can *buy* **sticker packs** from the store.

## Sticker messages

Sticker messages are an extended version of regular messages, though they are not embedded. 
By specifying an empty `content` string and adding sticker IDs into the array of strings `sticker_ids`, you can send a sticker message.
It can also return these errors:
- `403 Forbidden {"message": "Cannot use this sticker", "code": 50081}`: It can mean that:
  - You haven't paid for this sticker pack
  - You have provided an invalid or malformed ID
  - Stickers are not available in your country

[^1]: https://support.discord.com/hc/en-us/articles/360056891113-Stickers-FAQ
