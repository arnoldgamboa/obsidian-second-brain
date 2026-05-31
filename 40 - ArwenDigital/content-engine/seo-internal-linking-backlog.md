---
tags: [content-engine, seo, internal-linking, backlog]
date: 2026-05-20
status: tabled
source: Telegram discussion with Arnold
---

# SEO internal linking backlog

Arnold's concern: the blog posts feel like they are being published and then left alone, without enough connection between them or enough paths for people to discover them from social posts.

That feeling is accurate. The content engine is producing blog posts and social derivatives, but the next layer needs to turn those standalone posts into a connected SEO system.

## Current diagnosis

- Blog posts exist, but several records in `content-index.md` still show `internal_links_out: []` and/or `internal_links_in: []`.
- The weekly SEO review already flagged internal linking as underdeveloped.
- Social derivatives are being created and queued, but not all of them intentionally point readers back to the blog.
- Google Search Console review is not yet fully usable because the active Google token is missing the Search Console readonly scope.
- We are still making SEO decisions mostly from structure and intuition, not live query/page data.

## Strategic principle

Do not treat the blog as isolated posts.

Treat it as a small topical web:

- each post targets a query or problem
- each post supports a cluster
- each post links naturally to related posts
- older posts get updated to point to newer posts
- social posts occasionally route readers back to the blog
- Search Console eventually tells us which pages to improve

## Topic cluster structure

### YouPastor cluster

Future pillar page idea:

**AI for Pastors: A Practical Guide to Sermon Prep, Church Communication, and Ministry Workflows**

Supporting posts:

- Prompt Fatigue Is Why Pastors Stop Using AI
- Why Generic Chatbots Are Not Enough for Sermon Preparation
- The AI Workspace Pastors Actually Need
- How Pastors Can Use AI Without Outsourcing Their Calling
- The Future of Sermon Prep Is Human-in-the-Loop, Not Fully Automated
- Theological Guardrails for AI Sermon Prep
- AI Tools for Bivocational Pastors

Desired internal link flow:

- Prompt fatigue -> Generic chatbots
- Generic chatbots -> AI workspace
- AI workspace -> Prompt fatigue and Generic chatbots
- All supporting posts -> future YouPastor pillar/waitlist page

### AI Employee cluster

Future pillar page idea:

**AI Employee for Small Business: What It Is, What It Can Do, and How to Deploy One**

Supporting posts:

- Hire a Digital Employee, Not Another AI Tool
- The Real Cost of AI Adoption Is Friction
- What an AI Employee Can Actually Do in a Small Business
- Why Most Teams Do Not Need More SaaS — They Need Managed Agents
- How We Deploy AI Agents in 48 Hours
- AI Tool Fatigue Is an Implementation Problem

Desired internal link flow:

- Hire a Digital Employee -> Real Cost of AI Adoption Is Friction
- Real Cost of AI Adoption Is Friction -> Hire a Digital Employee
- What an AI Employee Can Actually Do -> Hire a Digital Employee and workflow audit CTA
- All supporting posts -> future AI Employee pillar/service page

## Rules to add to the content workflow later

For every new blog post:

1. Before publishing:
   - choose one primary keyword
   - choose 2-4 internal links out
   - add a CTA
   - add meta description
   - add related reading if natural

2. After publishing:
   - update 1-3 older posts to link back to the new post
   - update `content-index.md` with `internal_links_out` and `internal_links_in`
   - generate social derivatives
   - make at least one derivative include the blog URL when appropriate

3. Weekly:
   - check Search Console
   - identify high-impression/low-CTR pages
   - identify striking-distance keywords in positions 8-20
   - refresh titles, meta descriptions, internal links, and sections based on data

## Blog post template addition

Consider adding this near the end of posts when useful:

```md
## Related reading

- If this is the pain you feel, read: [Why Generic Chatbots Are Not Enough for Sermon Preparation](URL)
- If you want the product direction, read: [The AI Workspace Pastors Actually Need](URL)
```

Keep it useful, not forced.

## Social derivative rule

Not every social post needs a link. Some should remain native and engagement-first.

But for every blog post, at least one social derivative should intentionally point back to the blog:

- X: short thought + "I wrote more here: [URL]"
- LinkedIn: standalone post + "I expanded this here: [URL]"

This gives readers a path from social attention to owned content.

## Search Console setup task

Fix Google Search Console access by re-authorizing the personal Google token with this scope:

```text
https://www.googleapis.com/auth/webmasters.readonly
```

Once fixed, the weekly SEO review should pull the last 28 days for:

```text
https://arnold.gamboa.ph/
```

Report:

- queries/pages with high impressions and low CTR
- keywords ranking positions 8-20
- pages with declining clicks or impressions
- internal linking opportunities
- refresh recommendations
- new supporting post ideas based on query demand

## First execution checklist when we pick this back up

1. Open `content-index.md`.
2. Verify which Bear posts are actually live.
3. For all live YouPastor posts, add mutual internal links where natural.
4. For all live AI Employee posts, add mutual internal links where natural.
5. Add related reading sections to published posts if Bear editing is available.
6. Update `content-index.md` internal link fields.
7. Adjust the social derivative workflow so at least one derivative per blog includes the blog URL.
8. Fix Search Console OAuth scope.
9. Run a new weekly SEO review after the token is fixed.

## Files involved

- `content-index.md`
- `topic-clusters.md`
- `content-workflow.md`
- `publishing-calendar.md`
- `search-console-reports/2026-05-18-weekly-seo-review.md`

## Status

Tabled for now. Return to this after the current YouPastor/product focus allows a dedicated SEO/content systems pass.
