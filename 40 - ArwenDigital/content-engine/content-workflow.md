---
tags: [content-engine, workflow, hermes-automation]
date: 2026-05-16
status: active
---

# Content Workflow

## Principle

Hermes can write, but the system decides what should be written. Use deterministic indexing and topic selection before LLM drafting.

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
6. Save as Bear Blog draft when MCP is connected.
7. Update [[content-index]].
8. Send Telegram summary to Arnold with approve/edit/reject options.

## Workflow B — Internal linking

1. Before drafting, scan [[content-index]] for related published posts.
2. Insert 2–4 natural links if relevant.
3. After publishing, identify 1–3 older posts that should link to the new post.
4. Do not force links. If no relevant published posts exist, write `internal_links_out: []`.

## Workflow C — Social derivative creation

Every Wednesday, for the approved/published YouPastor blog draft, create a social pack for Arnold's approval:

- 3 LinkedIn posts
- 5 X posts

Do not push to Buffer on Wednesday unless Arnold explicitly asks. Thursday is the normal Buffer push day for approved social packs.

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

- Blog posts: create as drafts only, do not publish automatically.
- If Arnold says a blog draft is “approved” without saying “publish now,” treat it as approved for the next normal publish slot, not immediate publication. Ask only if timing is unclear and there is no default slot.
- Immediate publication requires explicit language like “publish now,” “publish today,” or “go live now.”
- Social posts: create Buffer drafts or send Telegram previews, do not auto-post without approval during first two weeks.
- Exception: Arnold has approved a recurring YouPastor bivocational pastors X workflow: every Friday, research/create at least 8 referenced X posts in Arnold's voice; every Monday, queue the latest pack to Buffer without an extra approval loop.
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
- Current YouPastor weekly workflow — updated 2026-05-29: Monday suggest/create blog draft and queue the latest Friday bivocational pastors X pack; Tuesday publish approved blog; Wednesday draft social posts; Thursday push approved social posts to Buffer; Friday research/create next bivocational pastors X pack.

## CTA rules

### YouPastor

Until the email capture URL exists, use a placeholder CTA:

> I’m building YouPastor for pastors who want AI help without outsourcing their calling. Join the email list when it opens, or message me if you want to be part of early feedback.

Once Arnold provides the URL, replace with the actual email capture link.

### AI Employee / AI Agent consultancy

Paused as of 2026-05-23. Do not use this CTA in new reports/drafts/social packs until Arnold reactivates ArwenHQ / AI Employee work.

Use this CTA:

> Want to see what your first AI employee could do? [Book a free 15-minute AI workflow audit](https://cal.com/arnold-gamboa-wxar6f/ai-agents-setup-free-call).

