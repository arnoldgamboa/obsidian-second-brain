# 2026-06-29 YouPastor SEO/content operations review

Source snapshot generated: 2026-06-29T10:00:24  
Live checks run: 2026-06-29 10:00 PST / Manila time  
Blog: https://arnold.gamboa.ph/  
Scope: YouPastor only. ArwenHQ, AI Employee, agency/client-reporting, proposal/project-management, SaaS/process, and Build-in-Public-for-ArwenHQ angles excluded.

## Executive summary

Search Console is available when queried through Arnold's personal token and the verified domain property `sc-domain:arnold.gamboa.ph`. The injected pre-run failed because it queried the URL-prefix property `https://arnold.gamboa.ph/`, where the account does not have sufficient permission. A live retry against the domain property succeeded.

YouPastor visibility is still extremely early: two YouPastor-related pages appeared at page level in the last 28 days, each with one impression and no clicks. Query-level data is still dominated by one non-YouPastor WordPress query, so there is not enough YouPastor query data for CTR rewrites yet.

The main operational issue remains publishing hygiene: two already-published YouPastor posts still contain public `EMAIL_CAPTURE_URL_PLACEHOLDER` links. I updated `content-index.md` for those two deterministic YouPastor status corrections only.

## Search Console status

- Status: OK via domain property
- Working site property: `sc-domain:arnold.gamboa.ph`
- Pre-run failing property: `https://arnold.gamboa.ph/`
- Date range: 2026-05-30 to 2026-06-27
- Previous comparison range: 2026-05-01 to 2026-05-29
- Token path used for successful live check: `/Users/arnoldgamboa/.hermes/google_token_personal.json`
- Required scope present: `https://www.googleapis.com/auth/webmasters.readonly`

### Available verified properties

The Search Console API lists Arnold as owner for:

- `sc-domain:arnold.gamboa.ph`
- `sc-domain:youpastor.com`
- `https://lifecity.ph/`
- `sc-domain:regubrief.com`
- `sc-domain:churchprompt.directory`

The weekly snapshot script should prefer `sc-domain:arnold.gamboa.ph` for this Bear Blog review.

## Search Console findings — YouPastor only

### Query-level findings

The page+query pull returned one row only, and it is not YouPastor-relevant:

| Page | Query | Clicks | Impressions | CTR | Avg position | Action |
|---|---:|---:|---:|---:|---:|---|
| `/why-i-wont-build-your-website-in-wordpress-and-what-i-recommend-instead/` | `wordpress site built badly` | 0 | 39 | 0% | 58.74 | Ignored — not YouPastor |

There are no YouPastor query-level low-CTR opportunities yet.

### YouPastor page-level findings

| Page | Clicks | Impressions | CTR | Avg position | Interpretation |
|---|---:|---:|---:|---:|---|
| `/sermon-is-not-the-whole-pastoral-workflow/` | 0 | 1 | 0% | 8.0 | Early striking-distance signal; too little volume for a rewrite. Keep monitoring. |
| `/ai-should-help-pastors-not-replace-them/` | 0 | 1 | 0% | 9.0 | Early striking-distance signal. This older YouPastor post is not in the current content index; backfill later if it remains relevant. |

### Low CTR opportunities

None with meaningful YouPastor impressions. Two single-impression page appearances are indexing signals, not optimization signals.

### Striking-distance pages / keywords, position 8–20

No query-level YouPastor striking-distance keywords were exposed. Page-level candidates:

1. **The Sermon Is Not the Whole Pastoral Workflow** — avg position 8.0, 1 impression.
2. **AI should help pastors, not replace them** — avg position 9.0, 1 impression.

Recommended posture: monitor for another week before editing titles/meta. Do not rewrite based on one impression each.

### Decaying posts

No YouPastor decay detected. `/sermon-is-not-the-whole-pastoral-workflow/` appeared in the previous period with 1 impression at avg position 9.0 and appears again this period with 1 impression at avg position 8.0. That is flat-to-slightly-better, not decay.

## YouPastor content-index review

### Active YouPastor approval queue

Pending Arnold review in `for-approval/`:

1. **AI Should Help Pastors Keep the Week, Not Just Finish Sunday**  
   Path: `for-approval/2026-06-29-youpastor-youpastor-ai-pastoral-rhythm.md`  
   Bear post ID: `WbKftxwrujCzZLhkkmDB`  
   Bear status: unpublished draft verified via Bear MCP.  
   SEO fit: strong continuation of the “sermon is not the whole workflow” cluster.  
   Next action: Arnold approve/edit/reject; replace email-capture placeholder before publish.

2. **Church Communication Should Not Start From Scratch Every Week**  
   Path: `for-approval/2026-06-26-youpastor-church-communication-not-from-scratch.md`  
   Bear post ID: `WAHbjbrMvktHAGFRcsGW`  
   Bear status: unpublished draft verified via Bear MCP.  
   SEO fit: strong support article for “AI church communication for pastors.”  
   Next action: Arnold approve/edit/reject.

AI Employee items in `for-approval/` were intentionally ignored.

### Deterministic status corrections made today

Live Bear checks showed two YouPastor posts that `content-index.md` still listed as drafts are already published:

| Post | Bear post ID | Public URL | Verification | Remaining issue |
|---|---|---|---|---|
| **Your Church Context Belongs in the Workflow, Not Every AI Prompt** | `LxwIIrANwaFECxnkrqPo` | https://arnold.gamboa.ph/youpastor-church-context-belongs-in-workflow/ | Bear `published=true`; meta description present | CTA still contains `EMAIL_CAPTURE_URL_PLACEHOLDER` |
| **Start With Your Sermon Notes, Not a Blank AI Prompt** | `vpRgjWFUuuAjuPDFRvzi` | https://arnold.gamboa.ph/youpastor-sermon-notes-before-ai-prompts/ | Bear `published=true`; meta description present | CTA still links to `EMAIL_CAPTURE_URL_PLACEHOLDER` |

I updated `content-index.md` for these two entries only, because the status change was deterministic from Bear MCP. No other YouPastor status updates were made.

### Duplicates / canonicalization

- Canonical approval-gates/autopilot target remains: **Pastors Do Not Need Autopilot AI. They Need Approval Gates.** (`pastors-need-approval-gates-not-autopilot-ai`, Bear post ID `cawFjjbqBIqDXXvLKZAP`).
- Non-canonical duplicate-risk post remains: **Pastors Need Approval Gates, Not AI Autopilot** (`pastors-need-approval-gates-not-ai-autopilot`, Bear post ID `STFDLLyZPbrCJNSuEztI`). Keep it unpublished unless rewritten for a distinct search intent such as an “AI sermon review checklist.”
- The new pastoral rhythm and church communication drafts are distinct enough to keep: one is about carrying the whole ministry week; the other is specifically about communication workflows.

### CTA and metadata checks

- Published YouPastor posts in the index generally have meta descriptions present.
- Two live YouPastor posts still expose placeholder CTA links:
  - `youpastor-church-context-belongs-in-workflow`
  - `youpastor-sermon-notes-before-ai-prompts`
- Current unpublished drafts use placeholder/soft CTA language; keep them unpublished until Arnold approves and the CTA is made non-broken.

## Risks

1. **Public placeholder CTA risk**  
   The two published posts with `EMAIL_CAPTURE_URL_PLACEHOLDER` links are the highest-priority fix because they affect real visitors now.

2. **Search Console property mismatch**  
   The automation should query `sc-domain:arnold.gamboa.ph`, not `https://arnold.gamboa.ph/`, or weekly snapshots will keep reporting false GSC permission failures.

3. **Thin query visibility**  
   YouPastor pages are indexed/visible at low volume, but query-level data is too sparse to support title/meta experiments.

4. **Approval queue mixing**  
   The active `for-approval/` queue includes both YouPastor and AI Employee items even though AI Employee is paused. This report ignores paused content, but the queue still creates review noise for Arnold.

## Recommended YouPastor topics for next week

1. **AI church communication for pastors**  
   Best next publish candidate if Arnold approves it: `Church Communication Should Not Start From Scratch Every Week`. It naturally supports the published “Sermon Is Not the Whole Pastoral Workflow” article.

2. **How pastors should review AI-generated sermon drafts**  
   Practical approval-gates checklist article. This extends the canonical approval-gates cluster without duplicating the core post.

3. **How bivocational pastors can reduce ministry context switching**  
   Use Arnold’s lived experience: workday fatigue, family pressure, Sunday still coming, and the need for practical help beyond sermon writing.

## Recommended next actions

1. **Fix live placeholder CTAs now**  
   Replace `EMAIL_CAPTURE_URL_PLACEHOLDER` on:
   - https://arnold.gamboa.ph/youpastor-church-context-belongs-in-workflow/
   - https://arnold.gamboa.ph/youpastor-sermon-notes-before-ai-prompts/

   If the email capture URL is still unavailable, use a non-broken interim CTA: `https://youpastor.com` or plain text inviting pastors to message Arnold.

2. **Approve or edit the two YouPastor drafts in `for-approval/`**  
   Prioritize:
   - `2026-06-26-youpastor-church-communication-not-from-scratch.md`
   - `2026-06-29-youpastor-youpastor-ai-pastoral-rhythm.md`

3. **Keep monitoring, do not rewrite from GSC yet**  
   Watch `/sermon-is-not-the-whole-pastoral-workflow/` and `/ai-should-help-pastors-not-replace-them/` next week. Wait for more impressions before changing titles or meta descriptions.

## Content-index update decision

Updated `content-index.md` only for obvious YouPastor status corrections:

- `youpastor-church-context-belongs-in-workflow`: draft → published, with Bear `published=true`; CTA placeholder warning recorded.
- `youpastor-sermon-notes-before-ai-prompts`: draft → published, with Bear `published=true`; CTA placeholder warning recorded.

No AI Employee entries were edited. No YouPastor recommendations were marked complete unless verified.
