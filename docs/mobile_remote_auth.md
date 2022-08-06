# Remote Auth (Mobile)
Remote auth lets users effortlessly log into the desktop client using a QR code displayed on the logged-out desktop app by scanning it using a logged-in mobile app.

## Initializing
When a user scans a QR code, the mobile client does the following:
1. First, the client parses the URL and checks that it's valid
2. Next, the client extracts the "fingerprint" parameter from the url (the value after `/ra/`)
3. The client uses this "fingerprint" parameter to make a POST request to `/users/@me/remote-auth` with the following JSON-encoded body:

| field | type | description |
| --: | :-- | :-- |
| `fingerprint` | string | value from the QR code |

This request causes the [`pending_finish`](desktop_remote_auth.html#op-pending-finish) to be emitted to the desktop client, causing it to display the "confirm on your phone" message.

`remote-auth` responds with the following JSON-encoded body on success:

| field | type | description |
| --: | :-- | :-- |
| `handshake_token` | string | used to refer to this remote auth session |

The `handshake_token` is then used to refer to the QR code session between subsequent requests. 

From this point, one of two actions can be performed with the remote login session. A [cancel](#cancelling) or a [finish](#finishing)


## Cancelling
Cancelling a login request causes the [`cancel` OP](desktop_remote_auth.html#op-cancel) to be emitted to the desktop client.

Cancelling a request can be done with a POST to `/users/@me/remote-auth/cancel` with the following body:

| field | type | description |
| --: | :-- | :-- |
| `handshake_token` | string | token from POST to `/users/@me/remote-auth` |

This endpoint responds with a 204 on success.

## Finishing
Finishing a login request causes the [`finish` OP](desktop_remote_auth.html#op-finish) to be emitted to the desktop client.

Finishing a request can be done with a POST to `/users/@me/remote-auth/finish` with the following JSON-encoded body:

| field | type | description |
| --: | :-- | :-- |
| `handshake_token` | string | token from POST to `/users/@me/remote-auth` |
| `temporary_token` | boolean | whether or not the resulting token should be "temporary". currently, **must** be false or else you will receive a 500 |

This endpoint responds with a 204 on success.
