# YouPastor SEO/content operations review — 2026-07-13

## Scope and sources

This review is limited to YouPastor. ArwenHQ, AI Employee, agency, client-reporting, proposal/project-management, and unrelated build-in-public items were excluded.

Sources used:

- Injected content-engine and Search Console snapshot generated 2026-07-13.
- Live `content-index.md`.
- Bear post detail for the five active YouPastor drafts indexed locally.
- Public URL checks for publication-state drift.
- Targeted Google Search Console queries for known YouPastor URLs covering 2026-06-13 through 2026-07-11, plus recent and previous 14-day page comparisons.

`topic-clusters.md`, `publishing-calendar.md`, and `content-workflow.md` are absent from the content-engine directory, and their snapshot fields were empty. The index is therefore the only available local operating source of truth this week.

## Search Console access/status

Status: **available and healthy** via Arnold's personal Google token with the Search Console read-only scope. Property queried: `sc-domain:arnold.gamboa.ph`.

The broad snapshot returned one unrelated WordPress query and no opportunities. A targeted YouPastor query was therefore run. Query-level rows were suppressed/absent at the current low volume, but page-level data showed six impressions across four YouPastor pages in the recent 14-day period. The previous 14-day period had no rows for the same known YouPastor URLs.

## YouPastor-only GSC findings

### Low CTR

No actionable low-CTR opportunity. The four visible pages had only 1–2 impressions each, which is too little evidence for title or meta-description changes.

### Striking distance

- `sermon-is-not-the-whole-pastoral-workflow/` appeared at average position **10** with **1 impression** and no clicks.

This is an early indexing signal, not a refresh trigger. The sample is too small to justify rewriting the title or description.

Other early visibility signals, outside the formal 8–20 striking-distance range:

- `ai-for-bivocational-pastors/` — 2 impressions, position 6.5.
- `pastors-ai-context-switching/` — 2 impressions, position 7.5.
- `pastors-need-approval-gates-not-autopilot-ai/` — 1 impression, position 6.

### Decay

No decay can be established. The previous 14-day comparison returned no page rows, so there is no meaningful click/impression baseline. Recent impressions are better treated as first visibility rather than recovery or decline.

### New content ideas supported by current signals

1. **A Monday-after-the-sermon workflow for pastors** — a practical supporting article for the broader “sermon is not the whole pastoral workflow” intent.
2. **A weekly ministry workflow for bivocational pastors** — support the page showing the strongest early visibility without duplicating its broad argument; focus on a concrete Monday-to-Sunday checklist.
3. **How pastors turn sermon notes into small-group questions without losing context** — connects sermon notes, saved church context, and the sermon-to-week product boundary.

These are directional ideas, not keyword-validated opportunities yet; query-level GSC data is still too sparse.

## Index/Bear operations findings

### Publication-state drift corrected

Bear detail and public HTTP 200 checks showed two locally indexed drafts are already published:

- **Your Church Context Belongs in the Workflow, Not Every AI Prompt** — published 2026-06-25.
- **Start With Your Sermon Notes, Not a Blank AI Prompt** — published 2026-06-22.

Both local draft frontmatters and `content-index.md` were updated deterministically with published status, Bear state, public URL, and publication date.

### CTA risks

Both newly reconciled live posts still contain `EMAIL_CAPTURE_URL_PLACEHOLDER`, so their visible CTA is broken/non-converting:

- `youpastor-church-context-belongs-in-workflow/`
- `youpastor-sermon-notes-before-ai-prompts/`

Three remaining unpublished Bear drafts also contain the placeholder and must not be published until it is replaced:

- **AI Sermon Research Needs a Trail Back to the Source**
- **What Pastors Should Review Before AI Leaves the Sermon Desk**
- **The Friday Reset Pastors Need Before Sunday**

All five inspected Bear items have meta descriptions. The published YouPastor backfill entries in the index also record meta descriptions as present. No missing-meta-description repair was identified from the available evidence.

### Duplicate/cannibalization risk

The approval-gates cluster remains the clearest duplication risk. Keep **Pastors Do Not Need Autopilot AI. They Need Approval Gates.** as canonical. The unpublished near-duplicate **Pastors Need Approval Gates, Not AI Autopilot** should remain unpublished unless rewritten for a distinct intent. The newer review-checklist draft may support the canonical article, but should retain its checklist intent and internal link rather than compete for the same broad phrase.

### Internal-link opportunities

The two reconciled published posts should link into the established cluster:

- sermon notes → generic chatbots, prompt fatigue, approval gates;
- saved church context → context switching, AI workspace, approval gates.

Do not edit live Bear content automatically; these are approval-required refreshes.

## Deterministic content-index updates made

- Corrected `youpastor-church-context-belongs-in-workflow` from draft/unpublished to verified published, with URL and date.
- Corrected `youpastor-sermon-notes-before-ai-prompts` from draft/unpublished to verified published, with URL and date.
- Mirrored those corrections in the corresponding local draft frontmatter.
- No other index status was changed.

## Risks/cleanup needed

1. **Immediate conversion risk:** two live posts expose the email CTA placeholder.
2. **Publishing blocker:** three active unpublished YouPastor drafts still use the placeholder CTA.
3. **Sparse search evidence:** six impressions and no query rows are not enough for CTR optimization, decay claims, or aggressive refreshes.
4. **Operating-file gap:** topic clusters, publishing calendar, and content workflow files are missing, leaving the index to carry all planning/state.
5. **Canonicalization:** approval-gates articles need disciplined internal linking to the established canonical URL.

## Next 3 recommended YouPastor actions

1. **Repair the two broken live CTAs first** by replacing `EMAIL_CAPTURE_URL_PLACEHOLDER` with the approved destination (or `https://youpastor.com` if that remains the intended fallback), then verify both public pages.
2. **Review and approve “AI Sermon Research Needs a Trail Back to the Source”** after CTA replacement; it is the freshest draft, has a complete meta description, and adds a distinct source-verification angle.
3. **Strengthen the emerging pastoral-workflow cluster** with approved internal links and next draft a practical “Monday after the sermon” workflow article; monitor GSC another 28 days before changing titles/meta descriptions.

## Report path

`/opt/data/My-Second-Brain/40 - ArwenDigital/content-engine/search-console-reports/2026-07-13-youpastor-seo-review.md`
