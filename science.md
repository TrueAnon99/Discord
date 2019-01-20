# Tracking via `/api/track` and `/api/science`

`/api/track` is the same as `/api/science`, both do work and accept the
same input. The reasoning for `/api/science` to appear is that adblocking
software was denying requests for `/api/track` because of the obivous name.

They seem to be the main way Discord collects user information. At the time of
writing, the client sends user data through those routes, **including when the
user explicitly denied such "collection".** The reasoning behind this behavior
is that the Privacy & Safety settings only cite *use* of the given data, **NOT**
collection of the data to start with.

![privacy & safety settings](https://catgirl.estrogen.fun/i/eq5w3chk.png)

Discord argues that they need to collect the data in the case the User
allows the usage of the data later on. Which in the author's opinion is complete
bullshit. Have a good day.

You can only delete all tracking data via deleting or disabling your account.

## `POST /api/science`

Called by the official clients to give user data to Discord.
The routes can be called at, theoretically, any point in time, but the *usual*
behavior is when you change channels, servers, enter/exit settings, acknowledge
messages, etc.

The request contains special CORS configurations to accept specific headers,
such as `X-Fingerprint` and `X-Super-Properties`.

The `X-Fingerprint` header specifies a device fingerprint, it is an opaque
string given by the `POST /api/v6/auth/fingerprint` route (request does not
contain body). It is assumed fingerprint generation happens on first client
start, or first client login.

The `X-Super-Properties` header encodes a base64 representation of a JSON
object.

### Super Properties object

| field | type | description |
| --: | :-- | :-- |
| os | string | operating system |
| browser | string | browser string, e.g `Chrome` |
| browser\_user\_agent | string | **full** browser user agent string |
| browser\_version | string | complete browser version |
| os\_version | string | operating system version, if available |
| referrer | string | ??? |
| referring\_domain | string | ??? |
| referring\_domain\_current | string | ??? |
| release\_channel | string | the client's release channel, `stable`, `ptb`, `canary` |
| client\_build\_number | integer | the client's build number |
| client\_event\_source | Nullable[?] | ??? |

Following fields are targeted towards mobile clients.

| field | type | description |
| --: | :-- | :-- |
| device | string | device information (model and manufacturer) |
| device\_id | string | device identifier |
| os\_sdk\_version | string | Android [API level] |

[api level]: https://en.wikipedia.org/wiki/Android_version_history

### Request body

The body encodes a JSON object:

| field | type | description |
| --: | :-- | :-- |
| token | string | analytics token. unknown if this ties up to your auth token |
| events | list of Event | events made by the user |

#### Event object

**Note:** Needs more work. There are a LOT of event types that its infeasible
to add them all. We SHOULD however, add the most known ones, such as
`channel_opened`.

**Note:** The only REQUIRED field is `type`. The rest of the fields are
present/not present based on that type.

| field | type | description |
| --: | :-- | :-- |
| type | string | event type |
