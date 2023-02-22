# Discord's new Mobile Indicator

The mobile indicator is a feature that recently landed on Stable versions of
Discord (January 16, 2019). It gives a phone icon next to a given user when
they supposedly are using their phone.

You can set yourself to idle/dnd/invisible to hide the mobile indicator.
It is also possible to patch the Android app.

## Detecting phone usage

The Gateway's `IDENTIFY` packet contains a `properties` field, containing
`os`, `browser` and `device` fields. Discord uses that information to know
when your phone client and only your phone client has connected to Discord,
from there they send the extended presence object.

The exact field that is checked is the `browser` field. 
If it's set to `Discord Android` on desktop, the mobile indicator is is 
triggered by the desktop client.  If it's set to `Discord Client` on mobile, 
the mobile indicator is not triggered by the mobile client.

The specific values for the `os`, `browser` and `device` fields can change from time to time.

At the time of writing, bots can spoof those fields and have the mobile
indicator set.

## Presence with mobile field

Presence objects come with a `mobile` field, which is a boolean telling if
the user being referenced by the presence is on mobile or not. It is not known
if the field is optional or not, for all intents and purposes, assume it *is.*
