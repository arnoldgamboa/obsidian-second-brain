---
title: "YouPastor Monthly Search Performance — June 2026"
date: 2026-07-16
site: "sc-domain:youpastor.com"
current_period: "2026-06-01 to 2026-06-30"
comparison_period: "2026-05-01 to 2026-05-30"
source: "Google Search Console via Composio"
status: complete
tags: [youpastor, seo, search-console, monthly-review]
brain_schema: 1
type: report
created: 2026-07-16
updated: 2026-07-16
area: ArwenDigital
aliases: []
---

# YouPastor Monthly Search Performance — June 2026

## Scope and reproducibility

- **Run time:** 2026-07-16 09:12 PST (Asia/Manila)
- **Property:** `sc-domain:youpastor.com`; active Google Search Console connection confirmed with `siteOwner` permission.
- **Latest complete date used:** 2026-07-13 (run date minus three days).
- **Current window:** 2026-06-01–2026-06-30, the complete previous calendar month. **No June days were excluded** because the lag cutoff falls after month-end.
- **Equal-length comparison:** 2026-05-01–2026-05-30 (30 days).
- **Year-earlier window:** 2025-06-01–2025-06-30.
- **Method:** Web search, final data. Totals were queried with `dimensions: []`; query, page, date, device, country, and query+page cuts were queried separately with `row_limit: 5000`, `start_row: 0`. Every result set was shorter than 5,000 rows, so pagination was complete. CTR below is recomputed as clicks ÷ impressions; position is Search Console’s impression-weighted average.

## Executive summary

YouPastor entered measurable organic discovery in June: **3 clicks from 68 impressions**, after no rows in the equal-length May comparison or June 2025. This is a new-site/discovery baseline, not yet enough volume for reliable trend or CTR optimization conclusions. Google began recording activity on June 15. The homepage and `/ai-sermon-prep` generated all page-visible clicks, while `/best-ai-sermon-tools` produced the most page-level impressions but no clicks and ranked too low for snippet changes alone to solve.

The most important issue is not broad deindexing: URL Inspection passed for the homepage and three priority pages. The priority is to consolidate topical relevance, strengthen internal links, and move the pages currently ranking in the 60s–90s into consideration range.

## Performance scorecard

| Metric | Jun 1–30 | May 1–30 | Period change | Jun 2025 |
|---|---:|---:|---|---:|
| Clicks | 3 | 0 | New activity (+3; percentage not meaningful from zero) | 0 |
| Impressions | 68 | 0 | New activity (+68; percentage not meaningful from zero) | 0 |
| CTR | 4.41% | N/A | New baseline | N/A |
| Average position | 64.84 | N/A | New baseline; no comparable ranking | N/A |

**Interpretation:** June is the first measurable period in the queried history. There is no evidence-supported decline, decay, or year-over-year trend yet.

## Top queries

Search Console exposed 24 query rows, all with zero visible clicks; the three total clicks were anonymized at query level. Highest visible impressions:

| Query | Clicks | Impressions | CTR | Position |
|---|---:|---:|---:|---:|
| ai sermon generator | 0 | 4 | 0% | 80.75 |
| ai tools for pastors | 0 | 4 | 0% | 78.50 |
| pocket pastor | 0 | 4 | 0% | 43.25 |
| sermon generator | 0 | 4 | 0% | 80.75 |
| ai for pastors | 0 | 3 | 0% | 73.67 |
| ai sermon outlines | 0 | 3 | 0% | 87.00 |
| ai sermon preparation | 0 | 3 | 0% | 79.33 |
| pocket pastor ai | 0 | 3 | 0% | 64.33 |

There are **no query-level striking-distance terms at positions 8–20** and no disclosed query rows at positions 1–7. Therefore, no keyword should yet be treated as a proven refresh or defense opportunity.

## Top pages

Page-level aggregation differs from property aggregation, so page rows are used for prioritization—not summed as site totals.

| Page | Clicks | Impressions | CTR | Position |
|---|---:|---:|---:|---:|
| `/best-ai-sermon-tools` | 0 | 37 | 0% | 72.73 |
| `/ai-sermon-prep` | 1 | 18 | 5.56% | 68.67 |
| `/` | 2 | 13 | 15.38% | 26.54 |
| `/church-communication` | 0 | 5 | 0% | 39.00 |
| `/sermon-outline-generator` | 0 | 4 | 0% | 91.25 |
| `/download` | 0 | 3 | 0% | 19.67 |

The homepage is the strongest click generator. `/best-ai-sermon-tools` is the clearest visibility leader but is not a conventional low-CTR opportunity because its average position is 72.73. `/download` is technically in striking distance at the page level, but three impressions are too sparse to justify major optimization.

## Winners, declines, and continuity

Because May returned no rows, all June visibility is new:

1. `/best-ai-sermon-tools`: +37 page-level impressions.
2. `/ai-sermon-prep`: +18 impressions and +1 click.
3. Homepage: +13 impressions and +2 clicks.

No evidence-backed declining or disappeared query/page can be identified. No previous monthly report was present in this directory, so continuity against prior recommendations cannot yet be assessed.

## Intent, overlap, and internal linking

**Data-backed:** several intents appeared across multiple pages:

- `ai sermon generator` → `/ai-sermon-prep` and `/best-ai-sermon-tools`.
- `ai sermon outlines` → `/ai-sermon-prep`, `/best-ai-sermon-tools`, and `/sermon-outline-generator`.
- `ai tools for pastors` → `/ai-sermon-prep` and `/best-ai-sermon-tools`.
- `sermon generator` → `/best-ai-sermon-tools` and `/sermon-outline-generator`.

**Hypothesis:** this may become cannibalization or intent ambiguity, but current counts (one to four impressions per query) are too low to prove it. Establish a clear role: comparison intent for `/best-ai-sermon-tools`, workflow/product intent for `/ai-sermon-prep`, and utility intent for `/sermon-outline-generator`. Link between them with descriptive anchors and avoid making all three pages target the same primary phrase.

## Device and country

- Desktop: 64 impressions (94.12%), 2 clicks, 3.13% CTR, position 68.81.
- Mobile: 4 impressions (5.88%), 1 click, 25% CTR, position 1.25. This is too sparse to infer a mobile advantage.
- United States: 42 impressions (61.76%), 0 clicks, position 74.33.
- Philippines: 3 impressions (4.41%), 2 clicks, 66.67% CTR, position 3.00. This is encouraging but far too small for a market-level conclusion.

## Technical, schema, and live-page validation

- Search Console URL Inspection returned **PASS / Submitted and indexed / fetch successful / indexing allowed / robots allowed** for `/`, `/ai-sermon-prep`, `/best-ai-sermon-tools`, and `/sermon-outline-generator`; user and Google canonicals matched.
- Breadcrumb rich results were detected and passed on the three inspected landing pages.
- `robots.txt` allows crawling and declares `https://youpastor.com/sitemap.xml`.
- The live sitemap returned HTTP 200 and includes 34 URLs. Search Console reports 34 submitted, 0 indexed, zero errors, zero warnings, and not pending. The “0 indexed” sitemap counter conflicts with successful URL Inspection and search impressions, so treat it as a reporting lag/limitation—not proof that all pages are unindexed.
- Checked pages returned HTTP 200 with one H1, self-canonicals, unique titles/descriptions, and JSON-LD present.

## Content gaps and GEO/AEO opportunities

The first visible demand centers on AI sermon tools, sermon generators, sermon outlines, and pastor AI. Build a coherent cluster around these intents rather than adding unrelated topics. For answer-engine visibility, add concise, pastor-specific answer blocks to the relevant pages: what the tool does, responsible-use guardrails, how it differs from generic chat, and a short workflow example. Keep claims demonstrable, name the author/organization, show update dates, and cite biblical or workflow sources where appropriate. Breadcrumb schema is already valid; FAQ schema should be used only where visible FAQs genuinely exist and should be validated before release.

## Prioritized actions (maximum five)

### Do this month

1. **Clarify and interlink the three-page sermon-AI cluster.** Make `/best-ai-sermon-tools` the comparison hub, `/ai-sermon-prep` the product/workflow page, and `/sermon-outline-generator` the utility page. Add contextual links with distinct anchors. **Evidence:** four query themes currently map to two or three of these URLs; positions are 68.67–91.25.
2. **Strengthen `/best-ai-sermon-tools` for its actual comparison intent.** Add a concise comparison table, selection criteria, pastoral guardrails, and clear links to the prep and outline pages; keep title/description aligned to “best AI sermon tools for pastors.” **Evidence:** it has the most page-level impressions (37) but no clicks and position 72.73, indicating relevance/depth is the first problem—not merely the snippet.
3. **Improve homepage-to-cluster authority flow.** Add prominent, descriptive links from the homepage and relevant blog posts to the three priority landing pages; include links back to the cluster hub. **Evidence:** the homepage earned 2 of 3 clicks and has the best substantial page position (26.54), while the target pages rank much lower.

### Next

4. **Publish one supporting article answering a narrow observed intent**, such as responsible use of AI in sermon writing/preparation, then link it to `/ai-sermon-prep`. Use concise answer blocks and visible sources for GEO/AEO. **Evidence:** `using ai in sermon writing`, `ai sermon preparation`, and adjacent terms appeared, but only at very low volume; this remains a hypothesis to validate.

### Monitor

5. **Track indexing counters and emerging page/query movement monthly.** Recheck sitemap indexed counts and inspect priority URLs only if impressions stall or coverage changes. Watch `/download` (position 19.67, three impressions) and Philippine performance without optimizing around tiny samples. **Evidence:** inspected URLs pass, while the sitemap’s zero-indexed counter conflicts with live search data.

## Data limitations

- Search volume is sparse: only 68 property-level impressions and 3 clicks.
- May 2026 and June 2025 returned valid empty datasets, so percentage, decay, and year-over-year conclusions are unavailable.
- Query privacy/anonymization hides the queries responsible for the three total clicks.
- Search Console aggregation types differ: page rows total more impressions than the by-property total; do not sum page rows as overall performance.
- Missing Search Console rows do not prove that a URL is unindexed.

## Sources

- Google Search Console Search Analytics API via Composio, queried 2026-07-16.
- Google Search Console Sites, Sitemaps, and URL Inspection APIs via Composio, queried 2026-07-16.
- Read-only live checks of `https://youpastor.com/`, `robots.txt`, `sitemap.xml`, and the three priority landing pages, 2026-07-16.
