# 2026-06-29 YouPastor SEO/content operations review

## Scope and sources

Scope: YouPastor only. I excluded ArwenHQ, AI Employee, agency process/SaaS, client reporting, proposal/project-management, and Build-in-Public-for-ArwenHQ angles unless they directly affected YouPastor.

Sources checked:

- Deterministic content-engine snapshot from `/opt/data/scripts/content_engine_snapshot.py`
- Search Console snapshot from `/opt/data/scripts/search_console_snapshot.py`
- Vault files under `/opt/data/My-Second-Brain/40 - ArwenDigital/content-engine/`
  - `content-index.md`
  - `topic-clusters.md` / `publishing-calendar.md` / `content-workflow.md` were absent in the current folder
  - YouPastor draft and approval notes under `drafts/` and `approvals/`

## Search Console status

Search Console API access is available and working for Arnold's personal Google account.

Snapshot details:

- Site: `sc-domain:arnold.gamboa.ph`
- Date range: `2026-05-30` to `2026-06-27`
- Rows returned: 1
- YouPastor rows returned: 0
- Snapshot status: `ok`

Returned row, excluded because it is not YouPastor:

| Page | Query | Clicks | Impressions | CTR | Position |
|---|---:|---:|---:|---:|---:|
| `/why-i-wont-build-your-website-in-wordpress-and-what-i-recommend-instead/` | `wordpress site built badly` | 0 | 39 | 0% | 58.74 |

### YouPastor-only GSC findings

#### Low CTR opportunities

None yet. The last-28-day Search Console snapshot did not surface any YouPastor page/query rows, so there is no YouPastor CTR signal to optimize from GSC this week.

#### Striking-distance keywords, position 8–20

None yet for YouPastor. The only position data in the snapshot was non-YouPastor and was excluded.

#### Decaying posts

None deterministically measurable. Without YouPastor query/page rows in the snapshot, there is no reliable way to identify decay from Search Console this week.

#### New content ideas from GSC

No YouPastor-specific query data surfaced, so Search Console is not yet driving topic selection.

## Index-based YouPastor review

### Current published YouPastor set looks healthy

The content index still shows the published YouPastor posts with verified public URLs, meta descriptions, and YouPastor CTA context present.

The canonical approval-gates article remains the right internal-link target:

- **Pastors Do Not Need Autopilot AI. They Need Approval Gates.**
  - slug: `pastors-need-approval-gates-not-autopilot-ai`
  - note: canonical approval-gates/autopilot target

### Current draft set

The current YouPastor drafts in the index are:

- **The Friday Reset Pastors Need Before Sunday**
- **Your Church Context Belongs in the Workflow, Not Every AI Prompt**
- **Start With Your Sermon Notes, Not a Blank AI Prompt**

The new Friday-reset draft is the freshest YouPastor content in the engine and is aligned with the current focus on pastor-facing workflow clarity.

### CTA review

No published YouPastor CTA problems were detected.

Drafts still carry placeholder email-capture CTAs, which is expected until the real capture URL is supplied, but it means they are not publish-ready yet:

- `The Friday Reset Pastors Need Before Sunday`
- `Your Church Context Belongs in the Workflow, Not Every AI Prompt`
- `Start With Your Sermon Notes, Not a Blank AI Prompt`

### Meta description review

Meta descriptions are present for the reviewed YouPastor drafts and published posts. No urgent meta-description cleanup was found.

### Duplicate / canonicalization risk

The existing canonicalization note is still correct:

- Keep **Pastors Do Not Need Autopilot AI. They Need Approval Gates.** as the canonical approval-gates/autopilot target.
- Leave **Pastors Need Approval Gates, Not AI Autopilot** unpublished unless it is rewritten around a distinct search intent.

## Risk notes

1. **Search visibility gap remains**  
   YouPastor pages are published and verified in Bear/public checks, but Search Console still did not surface YouPastor rows in the last 28 days.

2. **Draft CTA placeholders still block publishing**  
   The draft set is solid, but the three active YouPastor drafts still need the real capture URL before they can ship.

3. **Topic-cluster / publishing-calendar / workflow notes are absent**  
   The current content-engine folder does not contain populated `topic-clusters.md`, `publishing-calendar.md`, or `content-workflow.md`, so planning is happening mainly from the index itself.

4. **Approval-gates duplication risk persists**  
   The duplicate-risk approval-gates draft should remain parked unless it is rewritten for a truly different intent.

## Deterministic content-index updates made

None.

Reason: nothing required an obvious status change, and I did not want to invent state changes without a real publish/verify event.

## Recommended YouPastor topics for next week

1. **How pastors should review AI output before it leaves the sermon desk**  
   Practical, review-oriented, and distinct from the already-published approval-gates essay.

2. **How to turn one sermon into the rest of the week without losing pastoral voice**  
   Good bridge between the current sermon-focused posts and broader YouPastor workflow value.

3. **What a Friday reset looks like for bivocational pastors**  
   Extends the new Friday-reset draft into a concrete, high-intent workflow piece.

## Next 3 recommended YouPastor actions

1. **Replace the Friday draft CTA placeholder with the live capture URL and approve it for publishing.**  
   This is the clearest near-term content win in the engine right now.

2. **Decide the fate of the YouPastor bivocational X pack that was drafted but not queued.**  
   Either schedule it for distribution or archive it so the workflow stays clean.

3. **Draft one practical workflow article next week.**  
   Best option: a “review step” article that shows exactly how pastors should approve AI output before it becomes public.

## Report path

`/opt/data/My-Second-Brain/40 - ArwenDigital/content-engine/search-console-reports/2026-06-29-youpastor-seo-review.md`
