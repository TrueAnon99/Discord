# Discord's new Mobile Indicator

The mobile indicator is a feature that recently landed on Stable versions of
Discord (January 16, 2019). It gives a phone icon next to a given user when
they supposedly are using their phone.

## Discoverying phone usage

The Gateway's `IDENTIFY` packet contains a `properties` field, containing
`$os`, `$browser` and `$device` fields. Discord uses that information to know
when your phone client and only your phone client has connected to Discord,
from there they send the extended presence object.

The specific values for the `$os`, `$browser` and `$device` fields are unknown,
and can change from time to time.

At the time of writing, bots can spoof those fields and have the mobile
indicator set.

## Presence with mobile field

Presence objects come with a `mobile` field, which is a boolean telling if
the user being referenced by the presence is on mobile or not. It is not known
if the field is optional or not, for all intents and purposes, assume it *is.*
