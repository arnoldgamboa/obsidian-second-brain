---
tags: [content-engine, workflow, hermes-automation]
date: 2026-05-16
status: active
---

# Content Workflow

## Principle

Hermes can write, but the system decides what should be written. Use deterministic indexing and topic selection before LLM drafting.

## Approval queue folders

Use these folders as the operational source of truth for approval state:

- `for-approval/` — only files Arnold still needs to approve. Blog drafts and social packs waiting for approval go here. If there is nothing to approve, this folder should be clear except `README.md`.
- `blog-approved/` — blog drafts move here only after Arnold says `approved blog`, or when legacy drafts are reconciled as already published.
- `approved-social/` — social packs move here only after Arnold says `approved social`, or when legacy packs are reconciled as already scheduled/approved.

Cron jobs must never publish/schedule directly from `for-approval/`. They should publish/schedule only from `blog-approved/` and `approved-social/`.

## Workflow A — Blog draft creation

1. Read [[topic-clusters]] and [[content-index]].
2. Select the next topic based on:
   - cluster balance
   - no duplicate slug/title
   - strategic priority: YouPastor only while ArwenHQ / AI Employee is paused
   - source notes available
3. Create an SEO brief:
   - target audience
   - search intent
   - primary keyword
   - working title
   - outline
   - CTA
   - internal link candidates
4. Draft in Arnold's voice:
   - first-person where appropriate
   - scar-tissue opinions
   - honest tradeoffs
   - not generic AI marketing fluff
   - for YouPastor, do not frame the product as only a sermon-writing tool; broaden toward helping bivocational and small-church pastors carry sermon prep, communication, follow-up, admin, care, and weekly ministry rhythms
   - when discussing bivocational pastors, tap Arnold's lived experience as a bivocational pastor: limited time, ministry after work, family pressure, Sunday still coming, and the need for encouragement plus practical help
   - include visible references/sources when making statistical claims in blog drafts and X posts
   - default length: 600–900 words unless Arnold asks for long-form
   - if a draft feels bloated, cut it roughly in half: one clear point, fewer sections, less explaining, sharper opinion
5. Generate metadata:
   - slug
   - tags
   - meta description, 140–160 chars
6. Save the local approval copy under `for-approval/YYYY-MM-DD-<cluster>-<slug>.md` with `status: needs-approval`.
7. If Bear Blog MCP is connected, create/update an unpublished Bear draft only; do not publish.
8. Update [[content-index]].
9. Send Telegram summary to Arnold with approve/edit/reject options and the `for-approval/` path.

## Workflow B — Internal linking

1. Before drafting, scan [[content-index]] for related published posts.
2. Insert 2–4 natural links if relevant.
3. After publishing, identify 1–3 older posts that should link to the new post.
4. Do not force links. If no relevant published posts exist, write `internal_links_out: []`.

## Workflow C — Social derivative creation

Every Wednesday, for the approved/published YouPastor blog draft, create a social pack for Arnold's approval:

- 3 LinkedIn posts
- 5 X posts

Save social packs that need Arnold's approval under `for-approval/`, not `social-drafts/`. When Arnold says `approved social`, move the approved pack to `approved-social/` and update its frontmatter/status/checklist.

Do not push to Buffer on Wednesday unless Arnold explicitly asks. Thursday is the normal Buffer push day for files in `approved-social/`.

Do not create Threads posts. Arnold is not using Threads for this content engine. When his Facebook Page is set up, replace Threads with Facebook Page derivatives.

Social posts should not simply summarize. They should extract the tension, opinion, or practical lesson.

## Workflow D — Weekly SEO review

Once Search Console is connected:

1. Pull last 28 days of GSC data.
2. Find pages with:
   - high impressions + low CTR
   - average position 8–20
   - declining clicks
3. Recommend:
   - title/meta changes
   - refresh sections
   - new supporting posts
   - internal links
4. Update [[content-index]] statuses.
5. While ArwenHQ / AI Employee is paused, restrict weekly SEO reviews to YouPastor pages, queries, drafts, and recommendations.

## Workflow E — Monthly content refresh

1. Select posts marked `refresh-needed` or older than 90 days.
2. Refresh factual claims, CTA, internal links, and meta description.
3. Preserve URL unless there is a serious SEO reason to change it.
4. Update `last_refreshed` in [[content-index]].

## Approval policy

Until changed by Arnold:

- Blog posts: create as drafts only under `for-approval/`; do not publish automatically.
- If Arnold says `approved blog`, move the blog draft from `for-approval/` to `blog-approved/`. That means approved for the next normal publish slot, not immediate publication.
- Immediate publication requires explicit language like “publish now,” “publish today,” or “go live now.”
- Social posts that need review must live in `for-approval/`. If Arnold says `approved social`, move the social pack from `for-approval/` to `approved-social/`.
- Thursday Buffer jobs schedule only from `approved-social/`; Tuesday Bear Blog jobs publish only from `blog-approved/`.
- Exception: Arnold has approved a recurring YouPastor bivocational pastors X workflow: every Friday, research/create at least 8 referenced X posts in Arnold's voice and save the pack directly to `approved-social/`; every Monday, queue the latest eligible approved pack to Buffer without an extra approval loop.
- Existing published posts: do not edit without explicit approval.

## Confirmed setup decisions — 2026-05-16

- Bear Blog origin: `arnold-gamboa-dev.bearblog.dev`
- Public custom domain: `https://arnold.gamboa.ph/`
- Blog mode: **drafts only by default**; Hermes may publish only after explicit Arnold approval.
- Voice: personal founder voice with SEO discipline.
- YouPastor CTA: email capture link, to be added later.
- AI Employee CTA: `https://cal.com/arnold-gamboa-wxar6f/ai-agents-setup-free-call`
- Google Search Console: verified; use Arnold's personal Google account.
- Cadence approved: Bear Blog 1/week while YouPastor is the focus, LinkedIn 3/week, X 5/week plus recurring Friday-researched/Monday-queued bivocational pastors X pack, weekly SEO review.
- Current YouPastor weekly workflow — updated 2026-06-09: Monday suggest/create blog draft in `for-approval/` and queue the latest Friday bivocational pastors X pack from `approved-social/`; Tuesday publish approved blogs from `blog-approved/`; Wednesday draft social posts into `for-approval/`; Thursday push approved social posts from `approved-social/` to Buffer; Friday research/create next pre-approved bivocational pastors X pack directly in `approved-social/`.

## CTA rules

### YouPastor

Until the email capture URL exists, use a placeholder CTA:

> I’m building YouPastor for pastors who want AI help without outsourcing their calling. Join the email list when it opens, or message me if you want to be part of early feedback.

Once Arnold provides the URL, replace with the actual email capture link.

### AI Employee / AI Agent consultancy

Paused as of 2026-05-23. Do not use this CTA in new reports/drafts/social packs until Arnold reactivates ArwenHQ / AI Employee work.

Use this CTA:

> Want to see what your first AI employee could do? [Book a free 15-minute AI workflow audit](https://cal.com/arnold-gamboa-wxar6f/ai-agents-setup-free-call).

