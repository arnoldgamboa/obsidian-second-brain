     1|---
     2|tags: [content-engine, google-search-console, seo, setup]
     3|date: 2026-05-16
     4|status: needs-setup
     5|---
     6|
     7|# Google Search Console Setup
     8|
     9|## Goal
    10|
    11|Use Search Console data as the feedback loop for Hermes SEO decisions.
    12|
    13|## Required setup
    14|
    15|1. Confirm https://arnold.gamboa.ph/ is verified in Google Search Console.
    16|2. Grant access to the Google account/token Hermes can use.
    17|3. Decide whether Hermes should use:
    18|   - Google Workspace CLI / existing Google auth flow, or
    19|   - Search Console API service account/OAuth setup.
    20|4. Create weekly job to pull:
    21|   - page URL
    22|   - query
    23|   - clicks
    24|   - impressions
    25|   - CTR
    26|   - average position
    27|
    28|## Weekly analysis rules
    29|
    30|Hermes should flag:
    31|
    32|- **CTR opportunity:** impressions >= 50 and CTR < 1.5%
    33|- **Striking distance:** average position between 8 and 20
    34|- **Refresh candidate:** published > 90 days and impressions declining
    35|- **New content idea:** recurring query that does not map cleanly to an existing post
    36|
    37|## Output destination
    38|
    39|Weekly reports should be saved to:
    40|
    41|`40 - ArwenDigital/content-engine/search-console-reports/`
    42|
    43|and summarized to Telegram.
    44|
    45|## Current status — 2026-05-16
    46|
    47|- `~/.hermes/google_token_personal.json` exists.
    48|- Current token does **not** include Search Console scope.
    49|- `~/.hermes/scripts/search_console_snapshot.py` was created and tested; it currently returns `invalid_scope` until Google OAuth is re-authorized with:
    50|  - `https://www.googleapis.com/auth/webmasters.readonly`
    51|
    52|## Next setup requirement
    53|
    54|Re-authorize Arnold's personal Google OAuth token with Search Console/Webmasters readonly scope, or create a dedicated Search Console OAuth token file and point `GSC_TOKEN_PATH` to it.
    55|
    56|

## Verification Check — 2026-05-16

- `arnold.gamboa.ph` TXT verification record is now visible in DNS.
- Root `gamboa.ph` still has an existing Google verification TXT record.
- `arnold.gamboa.ph` and `arnold-gamboa-dev.bearblog.dev` return HTTP 200 when fetched with a normal browser user agent; bare curl returns 403, likely bot/user-agent filtering.
- Bear Blog MCP is configured and read-only operations succeeded: blog settings and post list were retrieved.
- Search Console API automation is still blocked until the Personal Google OAuth token includes `https://www.googleapis.com/auth/webmasters.readonly`.
