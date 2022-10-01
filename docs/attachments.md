# Client Attachments

## Historical Context

**This section is SPECULATIVE.**

Discord wants to provide more benefits for Nitro users to drive Nitro adoption,
one of them being bumping the attachment size limit from 100MB to 500MB, however,
Cloudflare only allows for client requests sized 100MB in the Free plan.

Cloudflare can bump this limit to 500MB for Enterprise customers, but users are
able to upload up to 10 attachments in a single message, so the upper limit
would be 5GB. What to do then?

The answer: New API for asynchronous attachment uploads.

## How it currently works

From [the official docs](https://discord.com/developers/docs/reference#uploading-files),
you use multipart form data to attach your file and then reference it in another
part called `payload_json`. This is all part of a single request to `POST /messages`.

## How the new method works

*We do not know if Discord will open this API to bots. Use this at your own
caution.*

A new `POST /attachments` is created which creates an "attachment slot" (unofficial name) inside
Discord, that "slot" has a Google Cloud Storage bucket URL that the client
*directly* uploads to, then references it in `POST /messages`.

### `POST /attachments`

Receives a list of attachment slot requests.

| field | type | description |
| --: | :-- | :-- |
| files | List[AttachmentSlotRequest] | requests |

Returns a list of attachment slots.

| field | type | description |
| --: | :-- | :-- |
| attachments | List[AttachmentSlot] | slots |

#### AttachmentSlotRequest

| field | type | description |
| --: | :-- | :-- |
| filename | string | file name |
| file\_size | int | file size |
| id | string | slot id (random int by client, **ASSUMPTION:** this is scoped to either session or user id. **ASSUMPTION:** must be a number, as its casted on AttachmentSlot) |

Example:

```json
{
  "filename": "myfile.png",
  "file_size": 533389,
  "id": "3821"
}
```

#### AttachmentSlot

Contains a reserved attachment slot the client shall upload the actual file to.

| field | type | description |
| --: | :-- | :-- |
| id | int | slot id from the request |
| upload\_filename | string | filename of that slot |
| upload\_url | string | url for the client to directly upload the file to |

Example:

```json
{
  "id": 3821,
  "upload_url": "https://discord-attachments-uploads-prd.storage.googleapis.com/b757d035-4dcb-44c6-b66e-2815f5042ede/myfile.png?upload_id=OHQlQNB7Mx1J8teeUPE1V__KLj0OZZdPkMmGaA7o1qY'",
  "upload_filename": "b757d035-4dcb-44c6-b66e-2815f5042ede/myfile.png"
}
```

### referencing attachments in `POST /messages`

The [partial attachment object](https://discord.com/developers/docs/resources/channel#attachment-object)
gets a new field, `uploaded_filename`, which is the same value as the one
returned in the AttachmentSlot.

Example of message containing an attachment slot reference:

```json
{
  "content": "",
  "nonce": "123123123123123123",
  "channel_id": "123123123123123123",
  "type": 0,
  "sticker_ids": [],
  "attachments": [
    {
      "id": "0",
      "filename": "myfile.png",
      "uploaded_filename": "b757d035-4dcb-44c6-b66e-2815f5042ede/myfile.png"
    }
  ]
}
```
