# Remote Auth (Desktop)
Remote auth lets users effortlessly log into the desktop client using a QR code displayed on the logged-out desktop app by scanning it using a logged-in mobile app.

## Connecting to the auth gateway

Connecting is simple, just open a websocket connection to `wss://remote-auth-gateway.discord.gg/?v=1`. (The official client refers to this as `GLOBAL_ENV.REMOTE_AUTH_ENDPOINT`, but this will likely not change aside from an incremented version counter).

## Sending / Receiving Data

Data is packed using simple JSON of the following format:
```js
{
  "op": "something",
  ... // Packets are flat, relevant data is just another key on the packet
}
```
The following OP codes are valid:

| op | sender | description |
| --: | :-- | :-- |
| `hello` | server | Sent on connection open |
| `init` | client | Sent after `hello`, describes generated public key |
| `nonce_proof` | server | Sent after `init`, contains encrypted nonce |
| `nonce_proof` | client | Sent after `nonce_proof`, contains decrypted nonce as "proof" |
| `pending_remote_init` | server | Sent after a valid `nonce_proof` is submitted |
| `pending_finish` | server | Sent after QR code is scanned, contains encrypted user data |
| `finish` | server | Sent after login flow is completed, contains encrypted token |
| `heartbeat` | client | Sent every N ms, described in `hello` packet |
| `heartbeat_ack` | server | Sent after `heartbeat` packet, should close connection if a `heartbeat_ack` isn't received by the next `heartbeat` interval |

## OP `hello`

When the socket is first opened, the server sends an OP `hello` packet.

| field | type | description |
| --: | :-- | :-- |
| `timeout_ms` | int | Time in milliseconds until the server will close the websocket and invalidate the login QR code |
| `heartbeat_interval` | int | Time in milliseconds between when a client should send heartbeats |

## OP `heartbeat`

Sent by the client every `heartbeat_interval`ms

## OP `heartbeat_ack`

Sent by the server after every `heartbeat`, the client should close the connection if no `heartbeat_ack` is received after the next `heartbeat` packet is to be sent.

## OP `init`

After receiving a `hello` packet, a client should send the `init` packet with the public key it generated which future data will be encrypted with.

| field | type | description |
| --: | :-- | :-- |
| `encoded_public_key` | base64 | base64-encoded spki-encoded public key |

## OP `nonce_proof`

### (From Server)

After receiving an `init` packet from the client, the server sends a `nonce_proof` packet containing a nonce encrypted using the public key provided in the `init` packet.

| field | type | description |
| --: | :-- | :-- |
| `encrypted_nonce` | base64 | base64-encoded encrypted nonce |


### (From Client)

After the client receives a `nonce_proof` packet from the server, the client sends back a `nonce_proof` packet of its own containing a SHA-256 digest of the decrypted data encoded as base64-url.

| field | type | description |
| --: | :-- | :-- |
| `proof` | base64-url | base64-url-encoded SHA-256 digest of data decrypted from the `encrypted_nonce` parameter |

## OP `pending_remote_init`

When the server receives a correct `nonce_proof` packet from the client, it sends a `pending_remote_init` with a `fingerprint` which describes the actual login request.
Interestingly, `fingerprint` is the base64-url-encoded SHA-256 digest of the public key. The official client _does_ check this equality, but there's no reason a client needs to.
The client uses `https://discordapp.com/rp/` concatenated with the `fingerprint` parameter to create the QR code.
This approach is preferable to using random data alone because users can be directed to install the app if they scan it using a conventional QR code scanner app.

| field | type | description |
| --: | :-- | :-- |
| `fingerprint` | string | used by mobile to uniquely identify a login request |

## OP `pending_finish`

When the user scans the QR code using their device, the server sends a `pending_finish` packet containing encrypted user data.
This is used by the official client to show the username and avatar as a preview and to prompt the user to accept the scanned code.
The encrypted data is a utf-8-encoded string of the following format, seperated by `:`s:

| type | description |
| --: | :-- |
| snowflake | User ID |
| int | User Discriminator |
| hex | User avatar hash |
| string | Username |

For example: `196769986071625728:1212:d0900b8fe361c755549ab0beadb35075:Mary`

| field | type | description |
| --: | :-- | :-- |
| `encrypted_user_payload` | base64-url-encoded | Encrypted user data of the format described above |

## OP `finish`

When the user confirms the login on their device, the server sends a `finish` packet containing an encrypted token.
This event also marks the closing of the websocket.

| field | type | description |
| --: | :-- | :-- |
| `encrypted_token` | token | user's token |

## OP `cancel`

When the user cancels the login on their device, the server sends a `cancel` packet.
This event also marks the closing of the websocket.

This OP has no other fields.
