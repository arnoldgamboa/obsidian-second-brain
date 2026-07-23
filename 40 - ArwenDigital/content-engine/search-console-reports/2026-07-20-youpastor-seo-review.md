---
brain_schema: 1
title: "Weekly YouPastor SEO & Content Operations Review — 2026-07-20"
type: report
status: active
created: 2026-07-20
updated: 2026-07-20
area: ArwenDigital
tags: []
aliases: []
---

# Weekly YouPastor SEO & Content Operations Review — 2026-07-20

## Scope and sources

This review is intentionally limited to YouPastor. ArwenHQ, AI Employee, agency, client-reporting, proposal/project-management, and build-in-public items were excluded.

Sources used:

- Injected content-engine and Search Console snapshot generated 2026-07-20.
- `content-index.md` and the eight local YouPastor draft/source notes.
- Google Search Console property `sc-domain:arnold.gamboa.ph` using Arnold's personal token.
- Recent period: 2026-06-20 through 2026-07-18; comparison period: 2026-05-22 through 2026-06-19.
- Bear Blog listing/detail checks were attempted, but the listing returned no records and detail requests failed with `Could not find header content in post` before the MCP server became temporarily unreachable.

The expected `topic-clusters.md`, `publishing-calendar.md`, and `content-workflow.md` files are absent from the live content-engine folder, and their snapshot fields were empty. Operational conclusions therefore use the canonical index and individual YouPastor notes.

## Search Console access/status

Search Console access is working. The broad snapshot returned one unrelated WordPress query row, which was excluded. A targeted YouPastor page/query query plus a page-level recent-vs-previous comparison was run.

No YouPastor page/query rows were returned. Page-level data shows five early indexing signals:

| Page | Recent clicks | Recent impressions | CTR | Avg. position | Previous impressions |
|---|---:|---:|---:|---:|---:|
| `ai-for-bivocational-pastors` | 0 | 3 | 0% | 6.3 | 0 |
| `pastors-ai-context-switching` | 0 | 2 | 0% | 7.5 | 0 |
| `pastors-need-approval-gates-not-autopilot-ai` | 0 | 1 | 0% | 6.0 | 0 |
| `prompt-fatigue-is-why-pastors-stop-using-ai` | 0 | 1 | 0% | 10.0 | 0 |
| `sermon-is-not-the-whole-pastoral-workflow` | 0 | 2 | 0% | 9.5 | 2 |

## YouPastor-only GSC findings

### Low CTR

No actionable low-CTR opportunity. Every YouPastor page has three or fewer impressions, so 0% CTR is not yet statistically meaningful.

### Striking distance

- `prompt-fatigue-is-why-pastors-stop-using-ai` at position 10.0 and `sermon-is-not-the-whole-pastoral-workflow` at 9.5 technically fall in the 8–20 range.
- These are early indexing signals, not refresh triggers: they have only one and two impressions respectively, and no query-level rows are available.
- Three other pages are showing top-eight average positions, but each has only one to three impressions. Monitor rather than rewrite.

### Decay

No decay is established. Four of the five visible pages had no previous-period impressions. `sermon-is-not-the-whole-pastoral-workflow` stayed at two impressions, with average position moving from 8.5 to 9.5; that sample is far too small to call decay.

### New content ideas from the signals

1. **A weekly workflow for bivocational pastors when sermon prep is not the only job** — supports the strongest current page-level signal without duplicating the existing product-boundary article.
2. **How pastors reduce context switching between sermon prep, care, and follow-up** — practical companion to the existing context-switching article.
3. **A simple post-sermon follow-up workflow for pastors** — can support the broad pastoral-workflow page and connect naturally to the new sermon-repurposing draft.

## Index and Bear operations findings

### Wins

- A fresh YouPastor draft was created today: **Do Not Turn Every Sermon Into Twelve Pieces of Content**. It is under 500 words, has a clear search intent, a complete meta description, and links to two relevant published articles.
- All eight local YouPastor notes inspected have a `meta_description`; the nine published backfilled posts are also recorded as having meta descriptions. No known local meta-description gap was found.
- The approval-gates canonical is clearly recorded: `pastors-need-approval-gates-not-autopilot-ai`.
- The newer review-checklist draft links to that canonical, helping distinguish checklist intent from the canonical conceptual article.

### CTA gaps

Four unpublished YouPastor drafts still use `EMAIL_CAPTURE_URL_PLACEHOLDER`:

- `sermon-repurposing-needs-pastoral-purpose`
- `ai-sermon-research-needs-source-trail`
- `review-ai-before-sermon-desk`
- `friday-reset-for-pastors-before-sunday`

Two locally recorded published posts also still contain the placeholder CTA in their source notes and are indexed as live CTA cleanup tasks:

- `youpastor-church-context-belongs-in-workflow`
- `youpastor-sermon-notes-before-ai-prompts`

These are the highest conversion-risk items. Published Bear content was not edited because that requires Arnold's approval and Bear detail verification was unavailable today.

### Duplicate/cannibalization risk

- The known non-canonical duplicate **Pastors Need Approval Gates, Not AI Autopilot** remains a do-not-publish item unless rewritten for a distinct search intent.
- **What Pastors Should Review Before AI Leaves the Sermon Desk** overlaps the approval-gates cluster but has a defensible checklist intent and already links to the canonical. Keep that distinction explicit in title, metadata, and internal links.
- The new sermon-repurposing draft is distinct from **The Sermon Is Not the Whole Pastoral Workflow**, but should link both ways after publication to clarify the broad-workflow versus repurposing-use-case relationship.

### Publication-state drift and Bear reliability

- `bear_list_posts` returned an empty list despite known published records.
- Detail checks first failed with `Could not find header content in post`, then the MCP server became temporarily unreachable.
- The 2026-07-20 draft remains unverified because its create result was only `post_id: new`.
- No local publication status was changed. This is the correct conservative behavior until Bear detail and public URL checks agree.

## Deterministic content-index updates made

None. Search Console did not prove any publication-state change, and Bear detail/public verification was unavailable. Existing YouPastor statuses were left unchanged.

## Risks / cleanup needed

1. **Broken or placeholder conversion paths:** four drafts and two locally recorded live posts still point to `EMAIL_CAPTURE_URL_PLACEHOLDER`.
2. **Bear reconciliation blocker:** the newest draft has no usable Bear post ID, while listing/detail tools were unreliable in this run.
3. **Very low organic sample size:** YouPastor has early indexing signals but insufficient query-level data for CTR rewrites, decay calls, or confident keyword optimization.
4. **Missing planning source files:** topic clusters, publishing calendar, and content workflow are absent, leaving the index as the only operational source of truth.
5. **Canonicalization discipline:** do not publish the non-canonical approval-gates duplicate; keep checklist/supporting articles clearly differentiated and linked to the canonical.

## Next 3 recommended YouPastor actions

1. **Normalize CTAs before more publishing.** Approve one destination—preferably the actual email capture URL, or `https://youpastor.com` as the intentional fallback—then repair the two live placeholders and the four draft placeholders, verifying public pages afterward.
2. **Reconcile Bear and choose the next publish candidate.** Recover a real post ID for the 2026-07-20 sermon-repurposing draft, verify the July 13/July 6/June 29 drafts remain unpublished, and only then approve one distinct-intent draft for publication. The July 13 source-trail article is the strongest next candidate because its intent is differentiated and its metadata/internal-link plan is complete.
3. **Build one support article around the strongest early signal.** Draft a practical bivocational-pastor weekly workflow article that links to `ai-for-bivocational-pastors`, `pastors-ai-context-switching`, and the sermon-to-week workflow content. Do not rewrite existing pages until impressions are meaningful.

## Report path

`/opt/data/My-Second-Brain/40 - ArwenDigital/content-engine/search-console-reports/2026-07-20-youpastor-seo-review.md`
