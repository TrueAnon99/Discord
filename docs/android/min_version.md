# Minimal version fetch

The Android client checks its own version against the minimal viable version
given by Discord. If the current version is lower than the minimal version, the
app will refuse to start and ask the user to update.

Assume the base url is `https://dl.discordapp.net` (used by official client).

## `GET /apps/android/versions.json`

Returns a JSON object with `discord_android_min_version` field.
