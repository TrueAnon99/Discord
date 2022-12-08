# User Settings
Most client settings are stored here for syncing.

## `GET /users/@me/settings`
Returns a [user settings](#user-settings-structure) object for the requester's account.

### User Settings Structure

| Field | Type | Description |
| -- | -- | -- |
| afk_timeout | integer | how many seconds being idle before the user is marked as "AFK"; this handles when push notifications are sent |
| allow_accessibility_detection | boolean | unknown |
| animate_emoji | boolean | play animated emoji without hovering over them |
| animate_stickers | integer | when stickers animate; `0`: always, `1`: on hover/focus, `2`: never |
| contact_sync_enabled | boolean | sync phone contacts with discord (seemingly unused, enabling contact sync does not change it) |
| convert_emoticons | boolean | convert "old fashioned" emoticons to emojis |
| custom_status | [custom status](/custom_status.html#customstatus-structure) object | custom status for the user |
| default_guilds_restricted | boolean | allow DMs from guild members by default on guild join |
| detect_platform_accounts | boolean | whether the client will detect accounts from other services for connections |
| developer_mode | boolean | show the option to copy ids in right click menus |
| disable_games_tab | boolean | hide the activity tab |
| enable_tts_command | boolean | enable /tts command and playback |
| explicit_content_filter | integer | content filter level; `0`: off, `1`: friends excluded, `2`: scan everyone |
| friend_discovery_flags | integer | [flags](#friend-discovery-flags) for how people can add the user via contact sync |
| friend_source_flags | [friend source flags](#friend-source-flags-structure) object | who can add the user as a friend |
| gif_auto_play | boolean | play GIFs without hovering over them |
| guild_folders | array of [guild folder](/guild_folders.html#folder-object) objects | guild folders set by the user |
| guild_positions | array | array of guild ids in order of position on the sidebar |
| inline_attachment_media | boolean | display images and video when uploaded directly |
| inline_embed_media | boolean | display images and video when linked |
| locale | string | user defined locale |
| message_display_compact | boolean | use compact mode |
| native_phone_integration_enabled | boolean | unknown |
| render_embeds | boolean | display embeds |
| render_reactions | boolean | display reactions |
| restricted_guilds | array | array of guild ids where the user has disallowed DMs from guild members |
| show_current_game | boolean | show playing status for detected/added games |
| status | string | current status; values: `online`, `idle`, `dnd`, `invisible` |
| stream_notifications_enabled | boolean | unknown |
| theme | string | client theme; values: `dark`, `light` |
| timezone_offset | integer | timezone offset in minutes (arbitrary number, no way to change in client) |
| view_nsfw_guilds | boolean | allow access to NSFW guilds from iOS devices |

### Friend Discovery Flags

| Value | Description |
| -- | -- |
| 0 | None |
| 1 << 0 | User can be added by phone number
| 1 << 1 | User can be added by email

### Friend Source Flags Structure

All of these fields are optional. To set false, either set the value to false or remove the field from the object.

| Field | Type | Description |
| -- | -- | -- |
| all | ?boolean | Anyone can add you |
| mutual_friends | ?boolean | Friends of friends can add you |
| mutual_guilds | ?boolean | Server members can add you |


## `GET /users/@me/settings-proto/:id`
Returns the user's settings in [protobuf](https://developers.google.com/protocol-buffers) format.
<details>
<summary><b>PreloadedUserSettings</b></summary>

```protobuf
syntax = "proto3";
package discord_protos.discord_users.v1;

message Version {
    uint32 client_version = 1;
    uint32 server_version = 2;
    uint32 data_version = 3;
}

enum InboxTab {
    UNSPECIFIED = 0;
    MENTIONS = 1;
    UNREADS = 2;
}

message InboxSettings {
    InboxTab current_tab = 1;
    bool viewed_tutorial = 2;
}

message ChannelSettings {
    bool collapsed_in_inbox = 1;
}

message GuildSettings {
    map<fixed64, ChannelSettings> channels = 1;
    uint32 hub_progress = 2;
    uint32 guild_onboarding_progress = 3;
}

message LastDismissedOutboundPromotionStartDate {
    string value = 1;
}

message PremiumTier0ModalDismissedAt {
    uint32 timestamp = 1;
}

message UserContentSettings {
    bytes dismissed_contents = 1;
    LastDismissedOutboundPromotionStartDate last_dismissed_outbound_promotion_start_date = 2;
    PremiumTier0ModalDismissedAt premium_tier_0_modal_dismissed_at = 3;
}

message VideoFilterBackgroundBlur {
    bool use_blur = 1;
}

message VideoFilterAsset {
    fixed64 id = 1;
    string asset_hash = 2;
}

message AlwaysPreviewVideo {
    bool value = 1;
}

message AfkTimeout {
    uint32 value = 1;
}

message StreamNotificationsEnabled {
    bool value = 1;
}

message NativePhoneIntegrationEnabled {
    bool value = 1;
}

message VoiceAndVideoSettings {
    VideoFilterBackgroundBlur blur = 1;
    uint32 preset_option = 2;
    VideoFilterAsset custom_asset = 3;
    AlwaysPreviewVideo always_preview_video = 5;
    AfkTimeout afk_timeout = 6;
    StreamNotificationsEnabled stream_notifications_enabled = 7;
    NativePhoneIntegrationEnabled native_phone_integration_enabled = 8;
}

message DiversitySurrogate {
    string value = 1;
}

message UseRichChatInput {
    bool value = 1;
}

message UseThreadSidebar {
    bool value = 1;
}

message RenderSpoilers {
    string value = 1;
}

message ViewImageDescriptions {
    bool value = 1;
}

message ShowCommandSuggestions {
    bool value = 1;
}

message InlineAttachmentMedia {
    bool value = 1;
}

message InlineEmbedMedia {
    bool value = 1;
}

message GifAutoPlay {
    bool value = 1;
}

message RenderEmbeds {
    bool value = 1;
}

message RenderReactions {
    bool value = 1;
}

message AnimateEmoji {
    bool value = 1;
}

message AnimateStickers {
    uint32 value = 1;
}

message EnableTtsCommand {
    bool value = 1;
}

message MessageDisplayCompact {
    bool value = 1;
}

message ExplicitContentFilter {
    uint32 value = 1;
}

message ViewNsfwGuilds {
    bool value = 1;
}

message ConvertEmoticons {
    bool value = 1;
}

message ExpressionSuggestionsEnabled {
    bool value = 1;
}

message ViewNsfwCommands {
    bool value = 1;
}

message TextAndImagesSettings {
    DiversitySurrogate diversity_surrogate = 1;
    UseRichChatInput use_rich_chat_input = 2;
    UseThreadSidebar use_thread_sidebar = 3;
    RenderSpoilers render_spoilers = 4;
    repeated string emoji_picker_collapsed_sections = 5 [packed = false];
    repeated string sticker_picker_collapsed_sections = 6 [packed = false];
    ViewImageDescriptions view_image_descriptions = 7;
    ShowCommandSuggestions show_command_suggestions = 8;
    InlineAttachmentMedia inline_attachment_media = 9;
    InlineEmbedMedia inline_embed_media = 10;
    GifAutoPlay gif_auto_play = 11;
    RenderEmbeds render_embeds = 12;
    RenderReactions render_reactions = 13;
    AnimateEmoji animate_emoji = 14;
    AnimateStickers animate_stickers = 15;
    EnableTtsCommand enable_tts_command = 16;
    MessageDisplayCompact message_display_compact = 17;
    ExplicitContentFilter explicit_content_filter = 19;
    ViewNsfwGuilds view_nsfw_guilds = 20;
    ConvertEmoticons convert_emoticons = 21;
    ExpressionSuggestionsEnabled expression_suggestions_enabled = 22;
    ViewNsfwCommands view_nsfw_commands = 23;
}

message ShowInAppNotifications {
    bool value = 1;
}

message NotifyFriendsOnGoLive {
    bool value = 1;
}

message NotificationSettings {
    ShowInAppNotifications show_in_app_notifications = 1;
    NotifyFriendsOnGoLive notify_friends_on_go_live = 2;
    fixed64 notification_center_acked_before_id = 3;
}

enum GuildActivityStatusRestrictionDefault {
    OFF = 0;
    ON_FOR_LARGE_GUILDS = 1;
}

message AllowActivityPartyPrivacyFriends {
    bool value = 1;
}

message AllowActivityPartyPrivacyVoiceChannel {
    bool value = 1;
}

message DetectPlatformAccounts {
    bool value = 1;
}

message Passwordless {
    bool value = 1;
}

message ContactSyncEnabled {
    bool value = 1;
}

message FriendSourceFlags {
    uint32 value = 1;
}

message FriendDiscoveryFlags {
    uint32 value = 1;
}

message PrivacySettings {
    AllowActivityPartyPrivacyFriends allow_activity_party_privacy_friends = 1;
    AllowActivityPartyPrivacyVoiceChannel allow_activity_party_privacy_voice_channel = 2;
    repeated fixed64 restricted_guild_ids = 3 [packed = true];
    bool default_guilds_restricted = 4;
    bool allow_accessibility_detection = 7;
    DetectPlatformAccounts detect_platform_accounts = 8;
    Passwordless passwordless = 9;
    ContactSyncEnabled contact_sync_enabled = 10;
    FriendSourceFlags friend_source_flags = 11;
    FriendDiscoveryFlags friend_discovery_flags = 12;
    repeated fixed64 activity_restricted_guild_ids = 13 [packed = true];
    GuildActivityStatusRestrictionDefault default_guilds_activity_restricted = 14;
    repeated fixed64 activity_joining_restricted_guild_ids = 15 [packed = true];
}

message RtcPanelShowVoiceStates {
    bool value = 1;
}

message DebugSettings {
    RtcPanelShowVoiceStates rtc_panel_show_voice_states = 1;
}

message InstallShortcutDesktop {
    bool value = 1;
}

message InstallShortcutStartMenu {
    bool value = 1;
}

message DisableGamesTab {
    bool value = 1;
}

message GameLibrarySettings {
    InstallShortcutDesktop install_shortcut_desktop = 1;
    InstallShortcutStartMenu install_shortcut_start_menu = 2;
    DisableGamesTab disable_games_tab = 3;
}

message Status {
    string status = 1;
}

message CustomStatus {
    string text = 1;
    fixed64 emoji_id = 2;
    string emoji_name = 3;
    fixed64 expires_at_ms = 4;
}

message ShowCurrentGame {
    bool value = 1;
}

message StatusSettings {
    Status status = 1;
    CustomStatus custom_status = 2;
    ShowCurrentGame show_current_game = 3;
}

message Locale {
    string locale_code = 1;
}

message TimezoneOffset {
    int32 offset = 1;
}

message LocalizationSettings {
    Locale locale = 1;
    TimezoneOffset timezone_offset = 2;
}

enum Theme {
    UNSET = 0;
    DARK = 1;
    LIGHT = 2;
}

message AppearanceSettings {
    Theme theme = 1;
    bool developer_mode = 2;
}

message PreloadedUserSettings {
    Version versions = 1;
    InboxSettings inbox = 2;
    GuildSettings guilds = 3;
    UserContentSettings user_content = 4;
    VoiceAndVideoSettings voice_and_video = 5;
    TextAndImagesSettings text_and_images = 6;
    NotificationSettings notifications = 7;
    PrivacySettings privacy = 8;
    DebugSettings debug = 9;
    GameLibrarySettings game_library = 10;
    StatusSettings status = 11;
    LocalizationSettings localization = 12;
    AppearanceSettings appearance = 13;
}
```

</details>

<details>
<summary><b>FrecencyUserSettings</b></summary>

```protobuf
syntax = "proto3";
package discord_protos.discord_users.v1;

enum GIFType {
    NONE = 0;
    IMAGE = 1;
    VIDEO = 2;
}

message FavoriteGIF {
    GIFType format = 1;
    string src = 2;
    uint32 width = 3;
    uint32 height = 4;
    uint32 order = 5;
}

message FavoriteGIFs {
    map<string, FavoriteGIF> gifs = 1;
    bool hide_tooltip = 2;
}

message FavoriteStickers {
    repeated fixed64 sticker_ids = 1 [packed = true];
}

message FrecencyItem {
    uint32 total_uses = 1;
    repeated uint64 recent_uses = 2 [packed = true];
    int32 frecency = 3;
    int32 score = 4;
}

message StickerFrecency {
    map<fixed64, FrecencyItem> stickers = 1;
}

message FavoriteEmojis {
    repeated string emojis = 1 [packed = false];
}

message EmojiFrecency {
    map<string, FrecencyItem> emojis = 1;
}

message ApplicationCommandFrecency {
    map<string, FrecencyItem> application_commands = 1;
}

message FrecencyUserSettings {
    Version versions = 1;
    FavoriteGIFs favorite_gifs = 2;
    FavoriteStickers favorite_stickers = 3;
    StickerFrecency sticker_frecency = 4;
    FavoriteEmojis favorite_emojis = 5;
    EmojiFrecency emoji_frecency = 6;
    ApplicationCommandFrecency application_command_frecency = 7;
}
```
</details>

### Settings ID
The `id` field can be one of:  
| Value | Name | Description |
| -- | -- | -- |
|1|PRELOADED_USER_SETTINGS|Appears to be the contents of regular /settings|
|2|FRECENCY_AND_FAVORITES_SETTINGS|Contains saved GIFs, as well as emoji and slash command [frecency](https://en.wikipedia.org/wiki/Frecency) data|
|3|TEST_SETTINGS|Blank on a regular user account. Unknown purpose|