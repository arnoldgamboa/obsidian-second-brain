---
brain_schema: 1
title: "2026-07-06 YouPastor SEO/content operations review"
type: report
status: active
created: 2026-07-06
updated: 2026-07-06
area: ArwenDigital
tags: []
aliases: []
---

# 2026-07-06 YouPastor SEO/content operations review

Source of truth: scheduled content-engine snapshot generated `2026-07-06T10:00:15` plus Search Console snapshot generated `2026-07-06` for `sc-domain:arnold.gamboa.ph` covering `2026-06-06` through `2026-07-04`.

Scope: YouPastor-only. ArwenHQ, AI Employee, agency process/SaaS, client reporting, proposal/project-management, and Build-in-Public-for-ArwenHQ angles are intentionally excluded.

## Executive summary

The YouPastor content base is in a healthy draft/published split, but Search Console is not yet surfacing YouPastor query data in the last 28-day snapshot. That means this week should focus less on reacting to GSC keywords and more on tightening publication readiness: replace placeholder email-capture CTAs, approve/publish the strongest existing drafts, and keep internal links pointed at the canonical approval-gates/autopilot article.

## Search Console status

- API status: `ok`.
- Property: `sc-domain:arnold.gamboa.ph`.
- Date range: `2026-06-06` to `2026-07-04`.
- Rows returned in snapshot: one row, for a non-YouPastor WordPress article:
  - Page: `https://arnold.gamboa.ph/why-i-wont-build-your-website-in-wordpress-and-what-i-recommend-instead/`
  - Query: `wordpress site built badly`
  - Clicks: 0
  - Impressions: 26
  - Average position: 61.35

### YouPastor-only GSC findings

No YouPastor page/query rows appeared in the latest 28-day Search Console snapshot. Therefore:

- Low-CTR YouPastor opportunities: none visible yet.
- Striking-distance YouPastor keywords, positions 8–20: none visible yet.
- Decaying YouPastor posts: not enough YouPastor GSC history in this snapshot to identify decay.
- New content ideas from GSC: none directly supported by YouPastor query data this week.

Interpretation: this is likely an indexing/age/data-volume issue rather than a content failure. The YouPastor posts are new enough that the next useful action is to keep publishing consistently and verify indexability/metadata rather than overfit to non-YouPastor query data.

## YouPastor content inventory from content index

### Published and verified YouPastor posts

These are already marked published and publicly verified in the content index:

- `https://arnold.gamboa.ph/youpastor-ai-sermon-preparation-without-losing-your-voice/`
- `https://arnold.gamboa.ph/youpastor-approval-gates-real-sermon-prep-workflow/`
- `https://arnold.gamboa.ph/ai-without-outsourcing-pastoral-calling/`
- `https://arnold.gamboa.ph/pastors-need-approval-gates-not-autopilot-ai/`
- `https://arnold.gamboa.ph/ai-for-bivocational-pastors/`
- `https://arnold.gamboa.ph/sermon-is-not-the-whole-pastoral-workflow/`
- `https://arnold.gamboa.ph/pastors-ai-pastoral-judgment/`
- `https://arnold.gamboa.ph/pastors-ai-context-switching/`
- `https://arnold.gamboa.ph/ai-workspace-pastors-actually-need/`
- `https://arnold.gamboa.ph/generic-chatbots-sermon-preparation/`
- `https://arnold.gamboa.ph/prompt-fatigue-is-why-pastors-stop-using-ai/`

Operational note: keep monitoring these after Search Console starts returning YouPastor rows. The current snapshot gives no page/query evidence to prioritize one refresh over another.

### YouPastor drafts waiting on approval/CTA

Current YouPastor drafts in the index:

1. `drafts/2026-07-06-youpastor-review-ai-before-sermon-desk`
   - Title: **What Pastors Should Review Before AI Leaves the Sermon Desk**
   - Status: draft
   - Bear post ID: `hwpEZqonhuVLrBHFNCqc`
   - Bear published: false verified via `bear_get_post`
   - Public URL: 404 as expected for draft
   - CTA: `email_capture_placeholder`
   - Next action: Arnold review/approval and replace `EMAIL_CAPTURE_URL_PLACEHOLDER` before publish.

2. `drafts/2026-06-29-youpastor-friday-reset-for-pastors-before-sunday`
   - Title: **The Friday Reset Pastors Need Before Sunday**
   - Status: draft
   - Bear post ID: `wRtWKTjTHdrNYabNoIxp`
   - Bear published: false created via `bear_create_post`
   - CTA: `email_capture_placeholder`
   - Next action: Arnold review/approval and email capture URL before publish.

3. `drafts/2026-06-22-youpastor-church-context-belongs-in-workflow`
   - Title: **Your Church Context Belongs in the Workflow, Not Every AI Prompt**
   - Status: draft
   - Bear post ID: `LxwIIrANwaFECxnkrqPo`
   - Bear published: false verified via `bear_get_post`
   - CTA: `email_capture_placeholder`
   - Next action: Arnold review/approval and replace `EMAIL_CAPTURE_URL_PLACEHOLDER` before publish.

4. `drafts/2026-06-22-youpastor-sermon-notes-before-ai-prompts`
   - Title: **Start With Your Sermon Notes, Not a Blank AI Prompt**
   - Status: draft
   - Bear post ID: `vpRgjWFUuuAjuPDFRvzi`
   - Bear published: false verified via `bear_get_post`
   - CTA: `email_capture_placeholder`
   - Next action: Arnold review/approval and replace `EMAIL_CAPTURE_URL_PLACEHOLDER` before publish.

## Risks and blockers

1. **Placeholder CTAs are blocking YouPastor publishing.**
   - Multiple YouPastor drafts still depend on `EMAIL_CAPTURE_URL_PLACEHOLDER` or `email_capture_placeholder`.
   - Do not publish these until the email capture URL is available or the CTA is intentionally changed to `https://youpastor.com`.

2. **Search Console has no YouPastor query rows yet.**
   - This limits data-driven refresh decisions.
   - Keep the review index-based until YouPastor URLs accumulate impressions.

3. **Canonicalization needs continued discipline.**
   - Canonical approval-gates/autopilot target: **Pastors Do Not Need Autopilot AI. They Need Approval Gates.**
   - Slug: `pastors-need-approval-gates-not-autopilot-ai`
   - Bear post ID: `cawFjjbqBIqDXXvLKZAP`
   - Non-canonical duplicate risk remains unpublished: `pastors-need-approval-gates-not-ai-autopilot`, Bear post ID `STFDLLyZPbrCJNSuEztI`.
   - Do not republish the duplicate unless it is rewritten for a distinct search intent.

4. **Buffer X queue limit is blocking remaining YouPastor social posts.**
   - The `2026-07-03` YouPastor bivocational pastors X pack is only partially scheduled: 6/8 scheduled.
   - Remaining posts are blocked by Buffer scheduled-post limit: 10/10.
   - This is social distribution, not core SEO, but it affects post amplification.

## Duplicate and cannibalization review

- Approval-gates/autopilot cluster has a clearly designated canonical post. Keep using it as the internal-link destination.
- The unpublished duplicate risk should remain unpublished unless rewritten.
- No other obvious YouPastor duplicate problem is visible from the snapshot.

## CTA and metadata review

### CTA issues

- Published YouPastor posts appear to have YouPastor CTA context and public verification.
- Draft YouPastor posts are blocked by placeholder CTAs.
- Recommended default if no email capture page exists this week: normalize draft CTAs to `https://youpastor.com` rather than leaving placeholders.

### Meta description issues

- Backfilled published YouPastor posts show `meta description: present` in the index.
- Draft metadata cannot be fully verified from the snapshot alone.
- Before approving any draft, verify the Bear draft has a non-empty meta description and does not repeat the title as an H1 in the body.

## Recommended YouPastor topics for next week

Because Search Console did not return YouPastor query opportunities, these are index-led topics based on the current published/draft clusters:

1. **A pastor's AI review checklist before Sunday**
   - Publish or refine: **What Pastors Should Review Before AI Leaves the Sermon Desk**.
   - Search intent: practical review checklist for pastors using AI in sermon preparation.
   - Internal links: pastoral judgment, approval gates, sermon prep workflow.

2. **Friday reset workflow for pastors**
   - Publish or refine: **The Friday Reset Pastors Need Before Sunday**.
   - Search intent: pastors preparing for Sunday, especially bivocational/small-church pastors.
   - Internal links: bivocational pastors, context switching, sermon is not whole workflow.

3. **Church context as workflow memory, not repeated prompt-writing**
   - Publish or refine: **Your Church Context Belongs in the Workflow, Not Every AI Prompt**.
   - Search intent: pastors tired of re-explaining church context to generic AI tools.
   - Internal links: generic chatbots, prompt fatigue, AI workspace pastors need.

4. **Start from sermon notes instead of blank prompts**
   - Publish or refine: **Start With Your Sermon Notes, Not a Blank AI Prompt**.
   - Search intent: AI sermon notes for pastors; practical first step for reluctant users.
   - Internal links: sermon prep without losing voice, generic chatbots, pastoral judgment.

## Next three recommended actions

1. **Resolve the CTA blocker for YouPastor drafts.**
   - Decide whether drafts should use an email capture URL or `https://youpastor.com`.
   - Replace `EMAIL_CAPTURE_URL_PLACEHOLDER` before publishing anything.

2. **Approve and publish one YouPastor draft this week.**
   - Best first pick: **What Pastors Should Review Before AI Leaves the Sermon Desk** because it maps to a concrete checklist/search intent and supports the approval-gates positioning.

3. **Keep Search Console monitoring YouPastor-only, but do not overreact yet.**
   - The current GSC snapshot has no YouPastor rows.
   - Continue weekly checks until YouPastor URLs show impressions; then prioritize low-CTR and position 8–20 opportunities.

## Content-index updates made

None. No deterministic YouPastor status change was visible from the snapshot. Drafts remain drafts; published items remain published; the social scheduling blocker remains unresolved.
