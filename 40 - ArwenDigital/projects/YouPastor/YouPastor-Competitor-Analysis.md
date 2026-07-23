---
tags: [project, YouPastor, competitors, analysis, positioning, strategy]
date: 2026-05-14
status: draft
---

# YouPastor — Competitor Analysis: Sermonly vs. Pastor AI Skills

> **Date:** 2026-05-14  
> **Purpose:** Compare YouPastor against its two closest alternatives to identify positioning gaps, differentiation opportunities, and the right angle for product-market fit.  
> **Key insight:** YouPastor should be positioned as a **pastor brainstorming and research assistant**, not a sermon creator.

---

## 1. Executive Summary

| | **Sermonly** | **Pastor AI Skills** | **YouPastor (Proposed)** |
|---|---|---|---|
| **What it is** | All-in-one sermon writing app | Claude Code skills / AI workflows | Desktop AI workspace for pastors |
| **Core promise** | "Write, research, plan, and share sermons" | "Real multi-step skills that handle the weekly grind" | "Your theological research assistant that never loses context" |
| **Positioning** | Sermon creator + storage | Workflow automation for pastors | Pastor brainstorming & communication partner |
| **Pricing** | $9.99–$19.99/mo | Free (MIT), but requires Claude Pro ($20/mo) | $19/mo + credits |
| **Platform** | Web, desktop, mobile | Claude Code CLI / Claude.ai Projects | Desktop (Electron), local-first |
| **AI approach** | Inline AI research + outline generation | Command-based skills (`/sermon-research`, `/church-email`) | Agentic loop with approval gates |
| **Theology** | Generic AI output | Pastor-built, denomination-aware | Configurable guardrails |
| **Offline** | No | No (cloud-dependent) | Yes (IndexedDB + sync) |

---

## 2. Deep Dive: Sermonly (sermon.ly)

### 2.1 What It Does
Sermonly is a sermon writing and storage platform owned by **Tithe.ly**. It provides:

- **Write and Store:** Centralized sermon library with tags and search
- **AI Researcher:** Generates outlines, character studies, modern-day examples
- **Snippets:** Collect content from websites/books into a library
- **Templates:** Custom sermon templates based on personal style
- **Read-only Mode:** Prevents accidental edits while preaching
- **Built-in Bible:** Multiple translations accessible while writing
- **Import:** Word, Pages, TXT file import
- **Multi-device:** Web, desktop, mobile sync

### 2.2 Pricing
- **Monthly:** $19.99/mo
- **Yearly:** $9.99/mo (billed annually = ~$120/yr)
- **Trial:** 7-day free trial

### 2.3 Strengths
- **Polished UX:** Professional, consumer-grade interface
- **Cross-platform:** Works on phone, tablet, and desktop
- **Tithe.ly ecosystem:** Integration potential with giving/platform tools
- **Read-only preaching mode:** Smart pastoral UX detail
- **Snippets feature:** Useful for collecting research artifacts

### 2.4 Weaknesses
- **AI is bolted on, not native:** The AI researcher feels like a feature, not the core architecture. It generates outlines but doesn't *guide* the pastor through a thinking process.
- **No communication tools:** No email drafting, announcement scripts, social media, or small group guides. It's sermon-only.
- **No context carry:** Each sermon is an isolated document. The AI doesn't know what you preached last week or what your series theme is.
- **No theological guardrails:** Generic AI output without denominational alignment.
- **No offline mode:** Requires internet to access sermons.
- **Single-user only:** No team collaboration (acknowledged as future feature).

### 2.5 How Sermonly Positions Itself
> "The all-in-one sermon writing tool dedicated to pastors who love to preach."

**The problem:** This frames the tool as a *replacement* for the pastor's creative work. It says "we help you write sermons faster," which can feel like outsourcing the sacred task. This is why some pastors resist AI tools—they don't want a robot writing their sermon.

---

## 3. Deep Dive: Pastor AI Skills (Thomas Costello)

### 3.1 What It Does
A collection of **13 AI workflow skills** built for Claude Code and Claude.ai Projects. Created by Thomas Costello (20+ years in ministry, founder of REACHRIGHT).

**The 13 Skills:**

| Category | Skill | Output |
|---|---|---|
| **Sermon Prep** | `/sermon-research` | Formatted PDF with commentaries, word studies, context |
| | `/sermon-brainstorm` | Interactive brainstorm → sermon brief |
| | `/sermon-series` | Multi-week series plan |
| **Communication** | `/church-email` | Weekly church email (subject, preview, body) |
| | `/announcement-script` | 60–90 second spoken script |
| | `/church-letter` | Formal letters for any occasion |
| **Repurposing** | `/small-group-questions` | Discussion questions (OIA method) |
| | `/sermon-to-blog` | 800–1200 word blog post |
| | `/sermon-to-youtube` | Title, description, tags, thumbnail concept |
| **Social Media** | `/church-social-post` | Platform-specific posts |
| | `/social-media-calendar` | Week/month content calendar |
| **Pastoral Rhythm** | `/midweek-devotional` | 200–300 word devotional |
| | `/meeting-agenda` | Structured leadership meeting agenda |

### 3.2 Pricing
- **Skills:** Free (MIT license)
- **Required substrate:** Claude Code (free tier limited) or Claude Pro ($20/mo)
- **Effective cost:** $0–$20/mo depending on Claude usage

### 3.3 Strengths
- **Pastor-built credibility:** Thomas Costello is a practitioner, not a Silicon Valley founder. This matters enormously for trust.
- **Workflow depth, not prompts:** Each skill has structured processes, format rules, and quality standards. Not just "here's a prompt."
- **Foundation layer:** Church details (name, denomination, attendance, location, translation) carry across all skills automatically.
- **Communication coverage:** Goes far beyond sermons into emails, announcements, social media, devotionals—the full weekly grind.
- **Theological sensitivity:** Explicitly built with pastoral awareness. The research skill "never writes the sermon."
- **Free and open-source:** Zero barrier to entry. Pastors can try without commitment.

### 3.4 Weaknesses
- **Requires technical setup:** Installing Claude Code, cloning repos, managing skills folders. Non-technical pastors will bounce.
- **No persistent context:** Each `/command` is an isolated session. The AI doesn't remember last week's sermon or your current series.
- **No GUI:** Terminal/CLI-based for Claude Code users. Pastors want a visual interface.
- **No offline mode:** Requires internet and Claude API access.
- **No collaboration:** Single-user only.
- **No billing/business model:** It's a free resource, not a sustainable product. This is fine for Thomas (he has REACHRIGHT), but means no support, no roadmap guarantees, no SLA.

### 3.5 How Pastor AI Skills Positions Itself
> "These are workflow tools, not prompt templates."  
> "Sermon prep tools help you research and think. They never write the sermon."  
> "That's between you and the Holy Spirit."

**This is brilliant positioning.** It addresses the core theological objection pastors have: *"I don't want AI writing my sermon."* By framing the tool as a *research and thinking partner*, it respects pastoral authority and spiritual responsibility.

---

## 4. Where YouPastor Fits

### 4.1 The Positioning Gap

Both competitors have a critical gap that YouPastor can own:

| Gap | Sermonly | Pastor AI Skills | YouPastor Opportunity |
|-----|----------|------------------|----------------------|
| **Context persistence** | ❌ Isolated sermons | ❌ Isolated commands | ✅ Context carries across entire weekly workflow |
| **Guided process** | ❌ AI is a search tool | ⚠️ Commands require initiative | ✅ Agentic loop with approval gates |
| **Beyond sermons** | ❌ Sermon-only | ✅ Full communication stack | ✅ 5 workspaces, context-aware |
| **Theological guardrails** | ❌ Generic output | ⚠️ Hardcoded preferences | ✅ Configurable denomination + style |
| **Ease of use** | ✅ Polished GUI | ❌ CLI/technical | ✅ Desktop app, no setup |
| **Offline access** | ❌ Cloud-only | ❌ Cloud-only | ✅ Local-first, sync when online |
| **Business model** | ✅ Sustainable ($10–20/mo) | ❌ No revenue | ✅ Base + Meter hybrid |

### 4.2 The "Pastor Brainstorming Tool" Angle

**You should NOT position as a "sermon creator."** Both Sermonly and generic AI tools (ChatGPT) already own that mental slot, and it triggers pastoral resistance.

**Instead, position as:**

> **"YouPastor is your theological research assistant and weekly ministry partner. It helps you think, research, and communicate—but you remain the pastor."**

This borrows the best insight from Pastor AI Skills ("never writes the sermon") but adds what it lacks: **persistent context, a visual interface, and an agentic workflow that guides rather than demands.**

**Key messaging:**
- "YouPastor doesn't write your sermon. It researches with you, brainstorms with you, and remembers what you're preaching all month."
- "Your sermon on Sunday becomes your email on Monday, your small group guide on Wednesday, and your social posts all week—automatically."
- "Theologically aligned to your tradition, not generic AI output."

### 4.3 Differentiation from Sermonly

**Sermonly = Microsoft Word for sermons + AI research bolt-on.**

**YouPastor = Your ministry brain that never forgets.**

| Comparison Point | Sermonly | YouPastor |
|------------------|----------|-----------|
| **Metaphor** | Better word processor | Ministry assistant |
| **AI role** | Research lookup | Guided thinking partner |
| **Scope** | Sermon document only | Entire weekly ministry output |
| **Context** | Per-sermon isolation | Series-wide, cross-workspace memory |
| **Theology** | Generic | Configurable guardrails |
| **Offline** | No | Yes |

### 4.4 Differentiation from Pastor AI Skills

**Pastor AI Skills = Powerful CLI scripts for technical pastors.**

**YouPastor = Those same workflows, but in a beautiful app that any pastor can use.**

| Comparison Point | Pastor AI Skills | YouPastor |
|------------------|------------------|-----------|
| **Interface** | Terminal / Claude.ai chat | Desktop GUI with workspaces |
| **Setup** | Clone repo, install dependencies | Download app, sign in |
| **Context** | Per-command isolation | Persistent across all workspaces |
| **Approval gates** | None (single-shot output) | Human-in-the-loop at key decisions |
| **Offline** | No | Yes (local-first) |
| **Cost** | Free (+ $20/mo Claude) | $19/mo + credits |
| **Support** | Community / none | Founder-led support |

**The pitch to a Pastor AI Skills user:** *"Love the workflows? YouPastor automates the same thinking process Thomas Costello built—but with a visual interface, context that carries across your whole week, and offline access."*

---

## 5. Strategic Recommendations

### 5.1 Positioning
Adopt the **"pastor brainstorming and research assistant"** framing explicitly. Avoid "sermon writer," "sermon generator," or "AI preacher" language anywhere in your marketing.

**Headline options:**
- "Your Theological Research Assistant"
- "The AI That Thinks Like a Pastor—Because It Was Built With One"
- "Brainstorm, Research, and Communicate. You Preach."

### 5.2 Feature Differentiation Priorities
Based on this analysis, prioritize features neither competitor has:

1. **Cross-workspace context** (your biggest moat)
   - When you finish a sermon in Sermon Prep, Communication workspace auto-loads it
   - Social Media workspace knows your series theme without re-prompting
   
2. **Approval gates / human-in-the-loop**
   - Sermonly generates outlines. YouPastor *proposes* angles and waits for your choice.
   - Pastor AI Skills outputs in one shot. YouPastor branches and iterates with you.

3. **Local-first / offline**
   - Sermonly dies without WiFi. Pastor AI Skills dies without Claude API.
   - YouPastor works on a plane, in a rural church, or during internet outages.

4. **Theological guardrails**
   - Neither competitor lets you configure denominational theology.
   - YouPastor's guardrails are a trust-builder and a feature Sermonly can't easily copy.

### 5.3 Pricing Strategy
| Competitor | Price | Weakness YouPastor Exploits |
|------------|-------|----------------------------|
| Sermonly | $9.99–19.99/mo | No communication features, no context carry |
| Pastor AI Skills | Free (+ $20 Claude) | Requires technical skill, no GUI, no persistence |
| **YouPastor** | **$19/mo + credits** | Justified by: guided workflows, context persistence, offline, full communication stack |

Your $19/mo Pastor plan is **feature-comparable to Sermonly + Pastor AI Skills combined**, with added value from context persistence and offline access. The credit top-ups handle heavy usage months (Easter, Christmas) without penalizing normal weeks.

### 5.4 Distribution Angles

**Vs. Sermonly:**
- Target pastors who tried Sermonly but felt it was "just a better Word doc"
- SEO comparison page: "Sermonly vs. YouPastor: From Document Storage to Ministry Partner"
- Emphasize: communication tools, context carry, offline access

**Vs. Pastor AI Skills:**
- Target pastors who love Thomas Costello's workflows but want a GUI
- Position as: "The Pastor AI Skills you love, now in a beautiful desktop app"
- Reach out to Thomas Costello for potential partnership or endorsement (he's a practitioner, not a competitor building a business)

**Shared target:**
- Pastors paying $20/mo for ChatGPT/Claude Pro but frustrated with generic output and context loss
- SEO: "ChatGPT for Pastors Isn't Enough"

---

## 6. Risk: What If Sermonly or Pastor AI Skills Copies You?

| Competitor | Likelihood | Why / Why Not |
|------------|------------|---------------|
| **Sermonly (Tithe.ly)** | Medium | Has engineering resources, but corporate pace is slow. Adding agentic workflows and context persistence requires architectural changes. They'd more likely acquire than build. |
| **Pastor AI Skills** | Low | Thomas Costello is a solo builder with a full-time job. His project is open-source and free by design. He has no incentive to build a competing commercial product. Potential ally. |
| **ChatGPT / Claude** | High (indirect) | General AI will keep improving. But pastors need *guided workflows*, not better chat. The niche isn't raw model capability; it's pastoral UX and theological alignment. |

**Your moat is not the AI. Your moat is the pastoral workflow design.**

Sermonly has the money but not the pastoral UX depth. Pastor AI Skills has the pastoral UX but not the product engineering. YouPastor must own both.

---

## 7. Related

- [[YouPastor-PRD]] — Product requirements
- [[YouPastor-Pricing-Strategy]] — Pricing and monetization model
- [[YouPastor-Distribution-Strategy]] — SEO and marketing
- [[Pastor AI Skills]] — Reference to Thomas Costello's project
