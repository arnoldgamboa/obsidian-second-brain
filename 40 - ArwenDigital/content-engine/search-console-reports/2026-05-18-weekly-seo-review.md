---
tags: [content-engine, seo-review, search-console]
date: 2026-05-18
status: active
source: hermes-cron
blog: https://arnold.gamboa.ph/
---

# Weekly SEO / Content Operations Review — 2026-05-18

## Executive summary

Google Search Console data could not be pulled this week because the active personal Google token is missing the required Search Console scope.

- **Token path checked:** `/Users/arnoldgamboa/.hermes/google_token_personal.json`
- **Required scope:** `https://www.googleapis.com/auth/webmasters.readonly`
- **Error:** `RefreshError('invalid_scope: Bad Request', {'error': 'invalid_scope', 'error_description': 'Bad Request'})`
- **Impact:** No reliable 28-day page/query metrics are available yet for low CTR, striking-distance keywords, or decay analysis.

Because GSC metrics are unavailable, this review is based on the content engine snapshot: `content-index.md`, `topic-clusters.md`, `publishing-calendar.md`, and `content-workflow.md`.

## Content engine status

### Current strategic priorities

1. **YouPastor** — attract pastors and ministry leaders who may eventually use the app.
2. **AI Employee / AI Agent consultancy** — attract operators and business owners for managed agent deployments.

### Published / queued content in index

| Cluster | Title | Status | URL / Notes |
|---|---|---:|---|
| YouPastor | Prompt Fatigue Is Why Pastors Stop Using AI | published | https://arnold.gamboa.ph/prompt-fatigue-is-why-pastors-stop-using-ai/ |
| AI Employee | Hire a Digital Employee, Not Another AI Tool | published | https://arnold.gamboa.ph/hire-a-digital-employee-not-another-ai-tool/ |
| YouPastor | Why Generic Chatbots Are Not Enough for Sermon Preparation | published | https://arnold.gamboa.ph/generic-chatbots-sermon-preparation/ — index notes still say scheduled for 2026-05-20 |
| AI Employee | The Real Cost of AI Adoption Is Friction | published | https://arnold.gamboa.ph/real-cost-of-ai-adoption-is-friction/ — index notes still say scheduled for 2026-05-21 |
| YouPastor | The AI Workspace Pastors Actually Need | drafted | Draft saved locally; Bear draft not created because Bear MCP tools were unavailable in the cron job toolset. |

## Index-based review

### Wins

- **Cluster balance is healthy.** The current index has a near-even split between YouPastor and AI Employee content.
- **Both strategic offers are represented.** YouPastor content targets the pastoral AI pain point; AI Employee content targets business operators worried about friction and implementation drag.
- **The strongest YouPastor narrative is emerging:** generic chatbots create context loss, prompt fatigue, and shallow sermon-prep outputs.
- **The strongest AI Employee narrative is emerging:** the product is not “another AI tool,” but a managed digital employee with no learning curve.
- **Cadence is clear and approved:** 2 Bear posts/week, 3 LinkedIn posts/week, 5 X posts/week, weekly SEO review.

### Risks / cleanup items

1. **Search Console cannot be queried yet.** The token needs Search Console readonly scope before metrics-based SEO decisions are possible.
2. **Several published records have conflicting scheduling notes.** Two records are marked `published` while `next_action` still says “scheduled to publish” on future dates. This may be harmless if they were intentionally pre-created as Bear drafts, but it should be reconciled after Bear status is verified.
3. **Internal linking is underdeveloped.** All current content records show `internal_links_out: []` and `internal_links_in: []`. With four related published posts, internal links can now be added naturally.
4. **Social derivatives are not populated.** The workflow requires 2 X posts and 1 LinkedIn post per approved blog draft, but the content index does not yet show derivative paths or IDs.
5. **YouPastor CTA is still placeholder-based.** Until the email capture URL exists, YouPastor posts should use the approved placeholder CTA consistently.
6. **Bear draft gap:** `The AI Workspace Pastors Actually Need` exists as a local draft but not as a Bear draft because MCP tools were unavailable in the cron toolset.

## Duplicate / overlap check

No hard duplicate titles or slugs were found in the snapshot.

There is intentional topical overlap in the YouPastor cluster:

- `Prompt Fatigue Is Why Pastors Stop Using AI`
- `Why Generic Chatbots Are Not Enough for Sermon Preparation`
- `The AI Workspace Pastors Actually Need`

This overlap is strategically useful if each post has a distinct angle:

- **Prompt fatigue:** user behavior and adoption failure.
- **Generic chatbots:** tool category critique.
- **AI workspace:** product/category vision.

## Cluster balance

Current content mix from the snapshot:

- **YouPastor:** 3 active blog records — 2 published, 1 drafted.
- **AI Employee:** 2 active blog records — 2 published.
- **Build in Public:** present only as secondary cluster, not yet as a primary post.

Recommendation: next week should include one AI Employee post and one Build-in-Public bridge post, unless the main goal is to deepen the YouPastor launch narrative first.

## CTA review

### YouPastor

Use the approved placeholder CTA until the email capture URL exists:

> I’m building YouPastor for pastors who want AI help without outsourcing their calling. Join the email list when it opens, or message me if you want to be part of early feedback.

### AI Employee

Use the approved live CTA:

> Want to see what your first AI employee could do? [Book a free 15-minute AI workflow audit](https://cal.com/arnold-gamboa-wxar6f/ai-agents-setup-free-call).

## Meta description review

Records with complete meta descriptions:

- `The AI Workspace Pastors Actually Need`
- `Why Generic Chatbots Are Not Enough for Sermon Preparation`
- `The Real Cost of AI Adoption Is Friction`

Records that need meta descriptions added to the index if not already present in Bear:

- `Prompt Fatigue Is Why Pastors Stop Using AI`
- `Hire a Digital Employee, Not Another AI Tool`

Suggested meta descriptions:

- **Prompt Fatigue Is Why Pastors Stop Using AI:** Pastors do not need to become prompt engineers. AI for ministry works best when it remembers context, guides workflows, and keeps pastors in control.
- **Hire a Digital Employee, Not Another AI Tool:** Stop adding more AI tools to your stack. A managed digital employee handles workflows, follow-up, and admin without a learning curve.

## Refresh / internal linking opportunities

No posts are old enough to need a factual refresh. The main opportunity is internal linking.

Recommended internal links once Bear editing is available:

1. From `Prompt Fatigue Is Why Pastors Stop Using AI` → `Why Generic Chatbots Are Not Enough for Sermon Preparation`
   - Anchor idea: “generic chatbots are not enough for sermon preparation.”
2. From `Why Generic Chatbots Are Not Enough for Sermon Preparation` → `The AI Workspace Pastors Actually Need` after the workspace post is published.
   - Anchor idea: “what pastors actually need is an AI workspace.”
3. From `Hire a Digital Employee, Not Another AI Tool` → `The Real Cost of AI Adoption Is Friction`
   - Anchor idea: “the real cost is adoption friction.”
4. From `The Real Cost of AI Adoption Is Friction` → `Hire a Digital Employee, Not Another AI Tool`
   - Anchor idea: “hire a managed digital employee instead of buying another tool.”

## Recommended topics for next week

### 1. AI Employee post: Why Most Teams Do Not Need More SaaS — They Need Managed Agents

- **Primary keyword:** managed AI agents
- **Secondary keywords:** AI agent consultancy, business automation, AI tool fatigue, AI employee
- **Search intent:** commercial / problem-aware
- **Angle:** Teams do not fail at AI because they lack tools. They fail because no one owns implementation, maintenance, and workflow fit.
- **CTA:** Book a free 15-minute AI workflow audit.

### 2. YouPastor post: How Pastors Can Use AI Without Outsourcing Their Calling

- **Primary keyword:** AI for pastors
- **Secondary keywords:** sermon prep AI, theological guardrails, church AI tools
- **Search intent:** thought-leadership
- **Angle:** AI should support pastoral discernment, not replace it. The key is human-in-the-loop approval and theological guardrails.
- **CTA:** Join the YouPastor early feedback list / message Arnold.

### 3. Build-in-public bridge post: What I Learned Using Hermes as a Founder

- **Primary keyword:** AI agents for founders
- **Secondary keywords:** personal AI operating system, founder automation, AI workflows
- **Search intent:** thought-leadership
- **Angle:** Practical scars from using agents to run content, email, research, and operations — including what still breaks.
- **CTA:** Soft bridge to AI Employee audits for operators or YouPastor feedback for ministry leaders.

## Search Console setup action

To enable next week’s metrics-based review, re-authorize the personal Google token with Search Console readonly scope included:

```bash
https://www.googleapis.com/auth/webmasters.readonly
```

After the token is refreshed, the weekly review should pull the last 28 days for `https://arnold.gamboa.ph/` and report:

- Queries/pages with high impressions and low CTR.
- Striking-distance keywords in average position 8–20.
- Pages with declining clicks or impressions.
- New supporting post ideas based on query demand.

## Deterministic index updates

No content-index changes were made in this run. The ambiguous items require external verification before updating:

- Whether the two posts with future scheduled notes are live, merely scheduled, or accidentally marked `published` early.
- Whether Bear draft creation succeeded for `The AI Workspace Pastors Actually Need` after the previous MCP limitation.
- Whether social derivatives exist outside the snapshot.

## Next 3 recommended actions

1. **Fix Search Console OAuth scope** so the next weekly report can use real query/page data.
2. **Create or verify the Bear draft** for `The AI Workspace Pastors Actually Need` and prepare it for approval.
3. **Add internal links and missing meta descriptions** across the four current published posts once Bear editing is available.
