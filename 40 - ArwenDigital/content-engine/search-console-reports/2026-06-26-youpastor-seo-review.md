# 2026-06-26 YouPastor SEO/content operations review

Source snapshot generated: 2026-06-26T22:43:09  
Live checks run: 2026-06-26  
Blog: https://arnold.gamboa.ph/  
Scope: YouPastor only. ArwenHQ, AI Employee, agency/client-reporting, proposal/project-management, SaaS/process, and Build-in-Public-for-ArwenHQ angles excluded.

## Executive summary

Search Console is usable through Arnold's personal Google token when queried as `sc-domain:arnold.gamboa.ph`. The pre-run failed because it queried the URL-prefix property `https://arnold.gamboa.ph/`, where the token does not have sufficient permission. Re-querying the verified domain property returned data.

YouPastor has started to surface in Search Console, but only at very low volume: two YouPastor-related pages appeared in page-level data, with three total impressions and no clicks. Query-level data still returned only a non-YouPastor WordPress query, so there are no query-led title/meta changes to make yet.

The biggest operational risk this week is not rankings. It is publishing hygiene: two YouPastor posts that the snapshot/index still described as drafts are now live on Bear and publicly accessible, but both still contain `EMAIL_CAPTURE_URL_PLACEHOLDER` in the CTA.

## Search Console status

- Status: OK via domain property
- Working site property: `sc-domain:arnold.gamboa.ph`
- Pre-run failing property: `https://arnold.gamboa.ph/`
- Date range: 2026-05-27 to 2026-06-24
- Token path used for successful live check: `/Users/arnoldgamboa/.hermes/google_token_personal.json`
- Required scope present: `https://www.googleapis.com/auth/webmasters.readonly`

### Query-level findings

The page+query pull returned one row only, and it is not YouPastor-relevant:

| Page | Query | Clicks | Impressions | CTR | Avg position | Action |
|---|---:|---:|---:|---:|---:|---|
| `/why-i-wont-build-your-website-in-wordpress-and-what-i-recommend-instead/` | `wordpress site built badly` | 0 | 44 | 0% | 59.39 | Ignored — not YouPastor |

There are no YouPastor query-level low-CTR opportunities yet.

### YouPastor page-level findings

| Page | Clicks | Impressions | CTR | Avg position | Interpretation |
|---|---:|---:|---:|---:|---|
| `/sermon-is-not-the-whole-pastoral-workflow/` | 0 | 2 | 0% | 8.5 | Early striking-distance signal, but too few impressions for a title/meta rewrite. Keep monitoring. |
| `/ai-should-help-pastors-not-replace-them/` | 0 | 1 | 0% | 9.0 | Early striking-distance signal. This older YouPastor post is not currently listed in the content index; it should be reconciled/backfilled later. |

### Low CTR opportunities

None with enough YouPastor impressions to justify a CTR-focused rewrite. The two YouPastor page impressions are encouraging indexing signals, not statistically useful optimization signals.

### Striking-distance keywords / pages, position 8–20

No query-level YouPastor striking-distance keywords were exposed. Page-level striking-distance candidates:

1. **The Sermon Is Not the Whole Pastoral Workflow** — avg position 8.5, 2 impressions.
2. **AI should help pastors, not replace them** — avg position 9.0, 1 impression.

Recommended posture: monitor for another week before editing titles/meta. Do not refresh purely from three impressions.

### Decaying posts

No decay detected. Previous-period page-level data for YouPastor returned no rows, so the current appearance of two YouPastor pages is a new visibility signal, not a decline.

## YouPastor content-index review

### Verified published YouPastor posts in the snapshot/index

The snapshot/index already records these YouPastor posts as published and verified with public URLs, meta descriptions, and YouPastor CTA context:

1. **AI Sermon Preparation Without Losing Your Pastoral Voice**  
   https://arnold.gamboa.ph/youpastor-ai-sermon-preparation-without-losing-your-voice/

2. **What Approval Gates Look Like in a Real Sermon Prep Workflow**  
   https://arnold.gamboa.ph/youpastor-approval-gates-real-sermon-prep-workflow/

3. **How Pastors Can Use AI Without Outsourcing Their Calling**  
   https://arnold.gamboa.ph/ai-without-outsourcing-pastoral-calling/

4. **Pastors Do Not Need Autopilot AI. They Need Approval Gates.**  
   https://arnold.gamboa.ph/pastors-need-approval-gates-not-autopilot-ai/  
   Canonical approval-gates/autopilot target.

5. **Bivocational Pastors Need More Than Sermon Prep AI**  
   https://arnold.gamboa.ph/ai-for-bivocational-pastors/

6. **The Sermon Is Not the Whole Pastoral Workflow**  
   https://arnold.gamboa.ph/sermon-is-not-the-whole-pastoral-workflow/

7. **Helpful AI Should Protect Pastoral Judgment**  
   https://arnold.gamboa.ph/pastors-ai-pastoral-judgment/

8. **The Hidden Weight Is Context Switching**  
   https://arnold.gamboa.ph/pastors-ai-context-switching/

9. **The AI Workspace Pastors Actually Need**  
   https://arnold.gamboa.ph/ai-workspace-pastors-actually-need/

10. **Why Generic Chatbots Are Not Enough for Sermon Preparation**  
    https://arnold.gamboa.ph/generic-chatbots-sermon-preparation/

11. **Prompt Fatigue Is Why Pastors Stop Using AI**  
    https://arnold.gamboa.ph/prompt-fatigue-is-why-pastors-stop-using-ai/

### Deterministic status corrections made today

Live Bear/public checks showed two YouPastor posts that the snapshot still listed as unpublished drafts are now published:

| Post | Bear post ID | Public URL | Verification | Remaining issue |
|---|---|---|---|---|
| **Your Church Context Belongs in the Workflow, Not Every AI Prompt** | `LxwIIrANwaFECxnkrqPo` | https://arnold.gamboa.ph/youpastor-church-context-belongs-in-workflow/ | Bear `published=true`; public HTTP 200; title present; meta description present | CTA still links to `EMAIL_CAPTURE_URL_PLACEHOLDER` |
| **Start With Your Sermon Notes, Not a Blank AI Prompt** | `vpRgjWFUuuAjuPDFRvzi` | https://arnold.gamboa.ph/youpastor-sermon-notes-before-ai-prompts/ | Bear `published=true`; public HTTP 200; title present; meta description present | CTA still links to `EMAIL_CAPTURE_URL_PLACEHOLDER` |

I updated `content-index.md` for these two YouPastor entries only, because the status change was deterministic from Bear MCP plus public URL verification.

### Duplicates / canonicalization

- Canonical approval-gates/autopilot target remains: **Pastors Do Not Need Autopilot AI. They Need Approval Gates.**
- Non-canonical duplicate-risk post remains: **Pastors Need Approval Gates, Not AI Autopilot** (`pastors-need-approval-gates-not-ai-autopilot`, Bear post ID `STFDLLyZPbrCJNSuEztI`). Live `bear_get_post` reports `published=false`; keep it unpublished unless rewritten for a separate search intent.
- Good distinct angle to use if rewritten: “how pastors review AI-generated sermon drafts” or “AI sermon approval checklist.”

### CTA and metadata checks

- Published YouPastor posts in the index have meta descriptions present.
- The two newly verified live posts have meta descriptions present, but both expose `EMAIL_CAPTURE_URL_PLACEHOLDER` publicly.
- Existing normalized YouPastor CTA on older posts remains `https://youpastor.com` where already fixed.

## Risks

1. **Live placeholder CTA risk**  
   Two public YouPastor posts currently show placeholder CTA links. This is the highest-priority fix because it affects visitors now.

2. **Search Console property mismatch**  
   The automation should query `sc-domain:arnold.gamboa.ph`, not `https://arnold.gamboa.ph/`, or weekly snapshots will falsely report a permission failure.

3. **Index drift**  
   Bear/public status moved ahead of the local content index for two YouPastor posts. I corrected the index entries that were deterministic today, but this suggests the content engine should reconcile Bear statuses during weekly review.

4. **Thin query visibility**  
   YouPastor is starting to appear in page-level Search Console data, but query-level data is still too sparse for query-led optimization.

## Recommended YouPastor topics for next week

1. **AI church communication for pastors**  
   Use the church communication angle to support “The Sermon Is Not the Whole Pastoral Workflow.” Focus on carrying approved sermon context into email, devotional, and follow-up drafts without autopilot.

2. **How pastors should review AI-generated sermon drafts**  
   Practical checklist article that extends the approval-gates cluster without duplicating the canonical article.

3. **How bivocational pastors can reduce ministry context switching**  
   Deepen the bivocational/context-switching cluster with Arnold’s lived experience: after-work prep, family pressure, Sunday deadlines, and practical support instead of hype.

## Recommended next actions

1. **Fix the two live placeholder CTAs**  
   Replace `EMAIL_CAPTURE_URL_PLACEHOLDER` on:
   - `youpastor-church-context-belongs-in-workflow`
   - `youpastor-sermon-notes-before-ai-prompts`

   If no email capture URL exists yet, use a non-placeholder YouPastor CTA pointing to `https://youpastor.com` or plain text inviting pastors to message Arnold.

2. **Update the Search Console snapshot script/property**  
   Use `sc-domain:arnold.gamboa.ph` for Search Console pulls. The domain property works with Arnold’s personal token; the URL-prefix property does not.

3. **Monitor, do not rewrite, the two early GSC pages**  
   Watch `/sermon-is-not-the-whole-pastoral-workflow/` and `/ai-should-help-pastors-not-replace-them/` next week. If impressions grow and CTR remains low, then test title/meta changes.

## Content-index update decision

Updated `content-index.md` only for obvious YouPastor status changes:

- `youpastor-church-context-belongs-in-workflow`: draft → published, with public URL verification and placeholder CTA warning.
- `youpastor-sermon-notes-before-ai-prompts`: draft → published, with public URL verification and placeholder CTA warning.

No other YouPastor status updates were made.
