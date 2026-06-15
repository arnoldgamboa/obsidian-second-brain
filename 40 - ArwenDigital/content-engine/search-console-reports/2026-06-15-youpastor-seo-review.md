# YouPastor SEO/content operations review — 2026-06-15

## Scope and sources

Scope: YouPastor only. I excluded ArwenHQ, AI Employee, agency process/SaaS, client reporting, proposal/project-management, and ArwenHQ build-in-public angles except where the shared content engine itself was affected.

Sources checked:

- Pre-run script output: both `content_engine_snapshot.py` and `search_console_snapshot.py` initially reported `CalledProcessError(2)` from `/opt/data/home/.hermes/scripts/...`.
- Recovered local snapshot scripts from `/opt/data/scripts/`:
  - `content_engine_snapshot.py` succeeded at `2026-06-15T10:00:55`.
  - `search_console_snapshot.py` succeeded for `sc-domain:arnold.gamboa.ph`, using Arnold's personal token.
- Vault source files:
  - `/opt/data/My-Second-Brain/40 - ArwenDigital/content-engine/content-index.md`
  - `topic-clusters.md`, `publishing-calendar.md`, and `content-workflow.md` were absent/empty in the current content-engine folder.
- Bear Blog API:
  - `bear_list_posts`
  - `bear_get_post` for the active YouPastor draft and representative YouPastor posts.
- Public URL check:
  - `https://arnold.gamboa.ph/youpastor-ai-sermon-preparation-without-losing-your-pastoral-voice/` returned `403 Forbidden` from this environment, so public-resolution verification was not available.

## Search Console access/status

Search Console API access is available after recovery.

Recovered snapshot details:

- Site: `sc-domain:arnold.gamboa.ph`
- Date range: `2026-05-16` to `2026-06-13`
- Rows returned: 2 total
- YouPastor rows returned: 0

Returned rows were non-YouPastor and excluded from this review:

| Page | Query | Clicks | Impressions | CTR | Position |
|---|---:|---:|---:|---:|---:|
| `/why-i-wont-build-your-website-in-wordpress-and-what-i-recommend-instead/` | `wordpress site built badly` | 0 | 43 | 0% | 59.14 |
| `/why-im-building-an-open-source-alternative-to-basecamp/` | `entry point freelancer` | 0 | 1 | 0% | 14.0 |

## YouPastor-only GSC findings

### Low CTR opportunities

None yet. Search Console returned no YouPastor query/page rows for the last 28 days, so there is no meaningful YouPastor CTR signal to optimize from GSC yet.

### Striking-distance keywords, position 8–20

None yet for YouPastor. The only striking-distance row in the snapshot was non-YouPastor (`entry point freelancer`) and was excluded.

### Decaying posts

None deterministically measurable. There is no YouPastor previous-period baseline in the recovered GSC output, and several YouPastor posts are too new to treat lack of impressions as decay.

### New content ideas from GSC

No YouPastor-specific query data yet. Use index/Bear gaps and existing YouPastor positioning instead of Search Console-driven ideas this week.

Recommended YouPastor topic ideas from the current content set:

1. **“A Friday reset for bivocational pastors before Sunday”** — extend the scheduled X pack’s practical reset angle into a blog post.
2. **“What approval gates look like in a real sermon prep workflow”** — reduce duplication around “approval gates” by making one practical/how-it-works article.
3. **“How to turn one sermon into a church email, small group questions, and a devotional without losing pastoral tone”** — strong bridge between the pastoral-workflow thesis and concrete YouPastor product value.

## Index/Bear operations findings

### 1. Content index is incomplete for YouPastor

`content-index.md` currently lists only one YouPastor blog draft:

- `AI Sermon Preparation Without Losing Your Pastoral Voice` — status: `draft`; Bear draft ID: `cXxWKVWJpicDQYLCsJmG`; Bear published: `false verified via bear_get_post`; CTA: email capture placeholder.

Bear Blog has multiple YouPastor posts that are not represented in the local index, including:

- `How Pastors Can Use AI Without Outsourcing Their Calling` — `bear_get_post` reports `published: true`; slug `ai-without-outsourcing-pastoral-calling`; meta description present.
- `Pastors Do Not Need Autopilot AI. They Need Approval Gates.` — `bear_get_post` reports `published: true`; slug `pastors-need-approval-gates-not-autopilot-ai`; meta description present.
- `Bivocational Pastors Need More Than Sermon Prep AI` — `bear_get_post` reports `published: true`; slug `ai-for-bivocational-pastors`; meta description present.
- `The Sermon Is Not the Whole Pastoral Workflow` — `bear_get_post` reports `published: true`; slug `sermon-is-not-the-whole-pastoral-workflow`; meta description present.
- `Helpful AI Should Protect Pastoral Judgment` — `bear_get_post` reports `published: true`; slug `pastors-ai-pastoral-judgment`; meta description present.
- `The Hidden Weight Is Context Switching` — `bear_get_post` reports `published: true`; slug `pastors-ai-context-switching`; meta description present.
- `The AI Workspace Pastors Actually Need` — `bear_get_post` reports `published: true`; slug `ai-workspace-pastors-actually-need`; meta description present.
- `Why Generic Chatbots Are Not Enough for Sermon Preparation` — `bear_get_post` reports `published: true`; slug `generic-chatbots-sermon-preparation`; meta description present.
- `Prompt Fatigue Is Why Pastors Stop Using AI` — `bear_get_post` reports `published: true`; slug `prompt-fatigue-is-why-pastors-stop-using-ai`; meta description present.

Because the index does not have matching `bear_post_id` entries for these, I did not auto-add them in this run. The next deterministic cleanup should backfill these as published YouPastor entries only after public URL verification works.

### 2. Bear publication drift exists on at least one active draft

For `AI Sermon Preparation Without Losing Your Pastoral Voice` (`cXxWKVWJpicDQYLCsJmG`):

- `bear_list_posts` reports `published: true`.
- `bear_get_post` reports `published: false`.
- Public URL check from this environment returned `403 Forbidden` and did not confirm title/CTA content.

Per the Bear verification pitfall, this should remain treated as **not verified published**. The local index status of `draft` / `Bear published: false verified via bear_get_post` is still the safest state.

A similar Bear list/detail mismatch appears for `Pastors Need Approval Gates, Not AI Autopilot` (`STFDLLyZPbrCJNSuEztI`):

- `bear_list_posts` reports `published: true`.
- `bear_get_post` reports `published: false`.

This is especially important because there is also a newer, very similar post: `Pastors Do Not Need Autopilot AI. They Need Approval Gates.`

### 3. Potential duplicate/cannibalization cluster: approval gates/autopilot

The approval-gates angle has at least two very similar titles/slugs:

- `Pastors Need Approval Gates, Not AI Autopilot` — slug `pastors-need-approval-gates-not-ai-autopilot`; `bear_get_post` reports `published: false`.
- `Pastors Do Not Need Autopilot AI. They Need Approval Gates.` — slug `pastors-need-approval-gates-not-autopilot-ai`; `bear_get_post` reports `published: true`.

Recommendation: keep one canonical approval-gates article and use internal links from related posts. Do not publish/republish both without a distinct intent.

### 4. CTA consistency gap

Newer/stronger YouPastor posts use `https://youpastor.com` or an early-access/message CTA. The current local draft `AI Sermon Preparation Without Losing Your Pastoral Voice` still uses:

`https://example.com/youpastor-email-capture-placeholder`

This should be normalized before approval/publishing. The clean default is:

`If you want early access, join the list at [youpastor.com](https://youpastor.com).`

### 5. Meta descriptions are mostly present

Representative Bear detail checks show YouPastor posts generally have meta descriptions. The active local draft also has a meta description in frontmatter. No urgent meta-description cleanup was found for the checked YouPastor posts.

### 6. Social pipeline is active

`2026-06-12-youpastor-bivocational-pastors-x-pack.md` is marked `scheduled` with 8 X posts queued to Buffer for June 15–18. It is YouPastor-only and aligned with the “bivocational pastors / staying help / pastoral workflow” positioning.

## Deterministic content-index updates made

None.

Reason: updates were not deterministic enough under the current verification policy. `content-index.md` lacks matching `bear_post_id` records for most published YouPastor posts, and public URL verification returned `403 Forbidden` from this environment. I left the index unchanged rather than marking records published without full verification.

## Risks/cleanup needed

1. **Search Console pre-run path is wrong/stale.** The injected pre-run tried `/opt/data/home/.hermes/scripts/...`, but the working scripts are under `/opt/data/scripts/`. Cron wiring should be fixed so the pre-run succeeds without recovery.
2. **Public URL verification is blocked from this environment.** `arnold.gamboa.ph` returned `403 Forbidden` for the active YouPastor slug. This prevents the stricter Bear verification rule from completing.
3. **Content index is not the source of truth yet.** The index is missing many Bear-verified YouPastor posts, so future automation may undercount the published YouPastor footprint.
4. **Approval-gates duplication risk.** There are two near-duplicate approval-gates/autopilot posts with very similar slugs; canonicalization is needed before more internal linking/social repurposing.
5. **CTA placeholder risk.** The active sermon-prep draft still contains an `example.com` placeholder CTA and should not be published as-is.

## Next 3 recommended YouPastor actions

1. **Fix the active draft before approval:** replace the placeholder CTA in `AI Sermon Preparation Without Losing Your Pastoral Voice` with `https://youpastor.com`, then re-check Bear detail/public URL before marking published.
2. **Backfill the content index with verified YouPastor posts:** add the published YouPastor Bear posts to `content-index.md` only after public URL verification works; include title, slug, Bear ID, published date, meta-description status, CTA type, and internal-link targets.
3. **Create one practical follow-up article:** draft `What approval gates look like in a real sermon prep workflow` or `A Friday reset for bivocational pastors before Sunday` to move from philosophy into concrete pastor-facing utility.

## Report path

`/opt/data/My-Second-Brain/40 - ArwenDigital/content-engine/search-console-reports/2026-06-15-youpastor-seo-review.md`
