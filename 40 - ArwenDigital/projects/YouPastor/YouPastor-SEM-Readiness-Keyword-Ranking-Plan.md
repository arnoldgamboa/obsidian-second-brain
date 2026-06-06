---
tags: [project, youpastor, seo, sem, marketing, analytics]
date: 2026-06-06
status: draft
source: telegram-document
---

# YouPastor Priority 3 — SEM Readiness & Keyword Ranking Plan

## Main Goal

Make YouPastor ready to:

1. Rank organically for pastor/ministry AI keywords.
2. Track paid and social campaigns accurately.
3. Convert visitors into downloads/trials.
4. Build landing pages for specific ad/search intent.

---

## Phase 1 — Measurement Foundation

### 1. Add Analytics Infrastructure

Recommended setup:

- Google Tag Manager
- GA4
- Google Ads conversion tracking
- Meta Pixel
- Optional later:
  - LinkedIn Insight Tag
  - Microsoft Ads UET
  - PostHog or Plausible for product-style analytics

### 2. Define Core Conversion Events

#### Website Events

- `view_homepage`
- `view_download_page`
- `click_download_mac`
- `click_download_windows`
- `click_pricing_cta`
- `click_hero_download`
- `click_footer_download`
- `click_external_github_download`
- `view_contact`
- `click_email_contact`

#### Funnel Events

- `download_started`
- `download_page_view_after_click`
- `billing_success_view`
- `billing_cancel_view`

#### Future App Events, If Possible

- `app_installed`
- `account_created`
- `first_sermon_started`
- `first_download_to_signup`
- `subscription_started`

### 3. Preserve UTM Attribution

Capture and store:

- `utm_source`
- `utm_medium`
- `utm_campaign`
- `utm_content`
- `utm_term`
- `gclid`
- `fbclid`
- `msclkid`
- landing page
- first referrer
- first visit timestamp

Store in `localStorage` and attach to tracked events.

---

## Phase 2 — Keyword Strategy

### Primary Keyword Targets

These should shape homepage and main landing pages.

#### Sermon Prep Keywords

- AI sermon prep
- AI sermon assistant
- sermon preparation software
- sermon prep software
- AI sermon writer
- AI sermon outline generator
- sermon outline generator
- sermon series planner
- sermon research tool

#### Pastor/Ministry Workflow Keywords

- AI tools for pastors
- AI ministry assistant
- pastor productivity software
- church communication software
- ministry workflow software
- pastoral assistant software
- church admin AI tool

#### Bible Research Keywords

- AI Bible study tool
- Bible passage research tool
- Greek Hebrew Bible study tool
- sermon Bible research assistant
- Bible study AI for pastors

#### Church Content/Social Keywords

- church social media content
- church social media post generator
- sermon to social media posts
- sermon repurposing tool
- church email generator
- church announcement generator

---

## Phase 3 — Landing Page Strategy

The homepage should remain broad. For ranking and ads, we need intent-specific pages.

### Recommended SEO/SEM Landing Pages

### 1. `/ai-sermon-prep`

Target:

- AI sermon prep
- AI sermon assistant
- sermon preparation software

Purpose:

- Core SEO page.
- Core Google Ads page.

Content sections:

- What AI sermon prep should and should not do
- How YouPastor helps with passage, angle, research, outline
- Why it is not an AI preacher
- Features
- FAQ
- CTA to download

---

### 2. `/ai-sermon-assistant`

Target:

- AI sermon assistant
- AI tools for pastors
- AI ministry assistant

Purpose:

- Brand/positioning page for pastors skeptical of AI.

Content:

- Human-in-the-loop explanation
- Theological guardrails
- Context persistence
- Pastoral workflow
- Comparison vs ChatGPT

---

### 3. `/sermon-outline-generator`

Target:

- sermon outline generator
- AI sermon outline generator
- sermon outline software

Purpose:

- Capture high-intent users looking for practical sermon help.

Important positioning:

- Avoid sounding like “push button sermon.”
- Position as outline support, not replacement.

---

### 4. `/sermon-series-planner`

Target:

- sermon series planner
- sermon series planning tool
- AI sermon series planner

Purpose:

- Search and ad page for planning multi-week preaching series.

---

### 5. `/church-social-media`

Target:

- church social media content
- church social media post generator
- sermon to social media posts

Purpose:

- Paid social and organic page.
- Strong for Facebook/Instagram campaigns.

---

### 6. `/church-communication`

Target:

- church communication software
- church email generator
- church announcement generator

Purpose:

- Reach pastors/church staff who need emails, announcements, and follow-up content.

---

### 7. `/ai-bible-research`

Target:

- AI Bible study tool
- Bible passage research tool
- sermon research tool
- Greek Hebrew Bible study tool

Purpose:

- Capture Bible study/research intent.

---

### 8. `/download-mac` and `/download-windows`

Target:

- Download YouPastor Mac
- Download YouPastor Windows
- AI sermon prep app for Mac
- AI sermon prep app for Windows

Purpose:

- Better ad quality score.
- Better platform-specific conversion tracking.

---

## Phase 4 — Page Template for Each Landing Page

Each landing page should follow a consistent structure:

1. SEO title and meta description
2. Hero with exact keyword
3. Problem statement
4. How YouPastor solves it
5. 3–5 feature cards
6. Trust/boundary section
7. Comparison section
8. FAQ section
9. Final CTA
10. JSON-LD structured data
11. Tracking events on CTA clicks

Example title:

```txt
AI Sermon Prep Software for Pastors | YouPastor
```

Example description:

```txt
YouPastor helps pastors brainstorm sermon ideas, research Bible passages, build outlines, and carry sermon context into church communication and social media.
```

---

## Phase 5 — Paid Campaign Readiness

## Google Search Ads Campaigns

### Campaign 1: AI Sermon Prep

Ad groups:

- AI sermon prep
- AI sermon assistant
- sermon prep software
- sermon outline generator

Landing page:

- `/ai-sermon-prep`

---

### Campaign 2: AI Tools for Pastors

Ad groups:

- AI tools for pastors
- AI ministry assistant
- pastor productivity software

Landing page:

- `/ai-sermon-assistant`

---

### Campaign 3: Church Content Repurposing

Ad groups:

- church social media content
- sermon to social media
- church email generator

Landing pages:

- `/church-social-media`
- `/church-communication`

---

## Meta/Facebook/Instagram Campaigns

### Campaign Angle 1: “Not an AI pastor”

Audience:

- Pastors
- Church planters
- Church leaders
- Seminary interests
- Worship/ministry pages

Landing page:

- `/ai-sermon-assistant`

Creative angle:

> AI should not replace the pastor. It should remember what the pastor is working on.

---

### Campaign Angle 2: Sermon Prep Workload

Landing page:

- `/ai-sermon-prep`

Creative angle:

> Sunday keeps coming. YouPastor helps sermon prep stay connected.

---

### Campaign Angle 3: Turn Sunday into the Rest of the Week

Landing page:

- `/church-social-media`

Creative angle:

> Turn one sermon into social posts, emails, devotionals, and small group questions.

---

## Phase 6 — Conversion Optimization

### CTA Improvements

Use different CTA labels depending on page intent:

- `Download Free`
- `Start with 100 Free Credits`
- `Download for Mac`
- `Download for Windows`
- `Try YouPastor Free`
- `Get Sermon Prep Help`

### Add Objection Handling Near CTA

Examples:

- No credit card required
- 100 free credits
- Human-in-the-loop
- You review every output
- Mac and Windows available

### Add Sticky/Mobile CTA

On mobile, add a bottom sticky button:

```txt
Download Free
```

---

## Phase 7 — Technical SEM Implementation

### Needed Code Features

1. Environment-based tracking IDs:
   - `PUBLIC_GTM_ID`
   - `PUBLIC_GA4_ID`
   - `PUBLIC_META_PIXEL_ID`
   - `PUBLIC_GOOGLE_ADS_ID`
   - `PUBLIC_GOOGLE_ADS_DOWNLOAD_LABEL`

2. Tracking script component:
   - Loads only if env vars exist.

3. Attribution script:
   - Captures UTMs and click IDs.
   - Stores first-touch and last-touch attribution.

4. Event helper:
   - Sends events to `dataLayer`, `gtag`, and Meta Pixel if available.

5. CTA data attributes:
   - `data-event`
   - `data-platform`
   - `data-location`
   - `data-page`

6. Download redirect tracking:
   - Fire event before external download opens.
   - Use short delay if needed.

---

## Phase 8 — Content Ranking Plan

### Short-Term Pages

Build first:

1. `/ai-sermon-prep`
2. `/ai-sermon-assistant`
3. `/church-social-media`
4. `/sermon-outline-generator`

### Medium-Term Pages

Then:

5. `/sermon-series-planner`
6. `/church-communication`
7. `/ai-bible-research`
8. `/download-mac`
9. `/download-windows`

### Blog/Content Cluster Ideas

Later, add articles:

- What Is AI Sermon Prep?
- Should Pastors Use AI for Sermon Preparation?
- AI Sermon Assistant vs ChatGPT
- How to Use AI Without Outsourcing Your Sermon
- How to Turn a Sermon into Social Media Posts
- How Pastors Can Save Time Without Replacing Study
- Sermon Series Planning: A Practical Guide for Pastors
- Church Social Media Ideas from Sunday’s Sermon

---

## Phase 9 — Success Metrics

### Organic SEO Metrics

- Search impressions
- Average position
- Click-through rate
- Pages indexed
- Landing page organic sessions
- Keyword movement

### SEM Metrics

- CTR by campaign
- Cost per download click
- Cost per actual download
- Landing page conversion rate
- Bounce rate
- Scroll depth
- CTA click rate
- Platform split: Mac vs Windows

### Business Metrics

- Download to account creation
- Account creation to first sermon
- First sermon to paid subscription
- Paid conversion by source/campaign
- Revenue by source/campaign

---

## Proposed Execution Order

### Sprint 1 — Tracking Foundation

- Add GTM/GA4/Meta support.
- Add UTM capture.
- Track all download and CTA clicks.
- Verify events.

### Sprint 2 — Core Landing Pages

Build:

- `/ai-sermon-prep`
- `/ai-sermon-assistant`
- `/church-social-media`
- `/sermon-outline-generator`

### Sprint 3 — More SEO Pages

Build:

- `/sermon-series-planner`
- `/church-communication`
- `/ai-bible-research`
- `/download-mac`
- `/download-windows`

### Sprint 4 — Ad Campaign Launch Prep

- Finalize ad copy.
- Set conversion goals.
- Create campaign-specific URLs.
- Test Meta/Facebook preview.
- Test Google Ads conversion flow.

### Sprint 5 — Optimization

- Review data after 7–14 days.
- Improve underperforming pages.
- Add internal links.
- Add blog/content cluster.


## Related

- [[YouPastor-PRD]]
- [[YouPastor-Landing-Page-Copy]]
- [[YouPastor-Distribution-Strategy]]
- [[YouPastor-Pricing-Strategy]]
