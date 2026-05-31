---
tags: [project, YouPastor, pricing, monetization, business-model, strategy]
date: 2026-05-14
status: draft
---

# YouPastor — Pricing & Monetization Strategy

> **Date:** 2026-05-14  
> **Goal:** Define the best pricing mechanism and distribution model for YouPastor, balancing pastor psychology, AI cost economics, and the need for sustainable MRR.

---

## 1. The Core Tension

YouPastor has a structural conflict built into its business model:

| Force | Implication |
|-------|-------------|
| **AI costs are real and variable** | Every sermon outline, Greek word study, and email draft costs money via OpenRouter |
| **Pastors hate wasted subscriptions** | A flat $30/mo fee feels like theft during vacation weeks or light months |
| **You need MRR to survive** | The PRD targets $5,000 MRR by Month 6. Pure credit top-ups generate **zero** recurring revenue |
| **Smaller churches are budget-constrained** | Sub-200-member churches scrutinize recurring expenses. Board approval often required above $50/mo |

**The wrong model kills you.** Pure subscription = high churn and pastor resentment. Pure credit top-up = lumpy revenue and no predictable runway.

---

## 2. Competitor & Market Context

- **ChatGPT Plus / Claude Pro:** $20/mo flat. Pastors are *already* paying this for generic output. YouPastor must beat this on perceived value or undercut on price.
- **Sermonly:** ~$15–30/mo subscription. Simpler feature set, traditional SaaS model.
- **Logos Bible Software:** One-time purchase ($300–1,000+) *plus* Faithlife Connect subscription ($10–50/mo). Logos trains pastors to pay for tools, but their model is content-heavy, not AI-agentic.
- **Jasper/Copy.ai:** Credit-based or tiered subscription. Business users tolerate this; pastors would find it opaque.

**Key insight:** Pastors are already spending ~$20/mo on AI. Your job is to capture that budget by proving pastor-specific value, not generic chat.

---

## 3. Recommended Model: "Base + Meter" Hybrid

This gives you **predictable MRR** (subscriptions) + **usage fairness** (credits) + **low-friction entry** (free tier).

### 3.1 Tier Structure

| Plan | Price | Credits | What's Included |
|------|-------|---------|-----------------|
| **Free** | $0 | 75/mo | Sermon Prep + Communication workspaces only. 3 saved sermons max. |
| **Pastor** | **$19/mo** or $190/yr | 400/mo | All 5 workspaces. Unlimited saves. Basic guardrails. Email support. |
| **Church** | **$49/mo** or $490/yr | 1,200/mo | Up to 5 users. Shared sermon library. Advanced/custom guardrails. Priority support. |

### 3.2 Credit Top-ups (All Paid Plans)

| Pack | Price |
|------|-------|
| 200 credits | $9 |
| 500 credits | $19 |
| 1,200 credits | $39 |

**Credits reset monthly** on the subscription date. Unused credits roll over **one month only** (creates urgency without being punitive).

---

## 4. Why This Model Wins

**1. It anchors against ChatGPT Plus**
At $19/mo, you're $1 *cheaper* than ChatGPT Plus. Your pitch writes itself: *"Stop paying $20 for an AI that doesn't know your church calendar. Get a pastor's brain for $19."*

**2. The "Base + Meter" removes purchase anxiety**
Pastors know their $19 covers their normal week. If Easter season hits hard, they buy a $9 top-up instead of feeling trapped in an expensive unlimited plan or nickel-and-dimed on every click.

**3. It actually creates MRR**
400 credits at $19/mo = ~$0.05/credit. If your OpenRouter cost averages $0.015–0.03 per credit consumed, you have 40–70% gross margins. The subscription base gives you predictable cash flow. The top-ups are pure margin.

**4. Free tier is your SEO funnel engine**
The distribution strategy depends on free web tools and blog content driving signups. A generous free tier (75 credits ≈ 1 full sermon workflow or 3–4 emails) lets pastors actually *experience* the product before paying. This is critical because pastors are skeptical of AI and need to feel the time-save themselves.

**5. Annual plans match church budgeting cycles**
Churches often approve software annually, not monthly. The $190/yr option (2 months free) captures this preference and improves your cash flow.

---

## 5. The Economics of Credits

You need a **published cost table** so pastors trust the system.

| Task | Credit Cost | Est. API Cost | Margin |
|------|-------------|---------------|--------|
| Brainstorm 3 hook angles | 5 credits | ~$0.03 | High |
| Draft church email | 8 credits | ~$0.05 | High |
| Generate sermon outline | 20 credits | ~$0.40 | Good |
| Greek/Hebrew word study | 35 credits | ~$0.80–1.20 | Moderate |
| Full exegetical deep-dive | 50 credits | ~$1.50–2.00 | Moderate |
| 7-day social media calendar | 25 credits | ~$0.50 | Good |
| Small group guide | 30 credits | ~$0.60 | Good |

At $0.05/credit (Pastor plan rate), a full sermon workflow (brainstorm → word study → outline → social calendar) costs ~80 credits = **$4.00**. That's *massive* value versus 10–20 hours of manual work.

---

## 6. Distribution & Sales Motion

**How you sell this matters as much as what you charge.**

### 6.1 Freemium as Distribution, Not Charity
The free tier isn't a giveaway—it's a lead qualification system. A pastor who uses 75 credits in a week is a hot lead. Trigger an in-app email: *"You burned through your credits fast. Here's 50 bonus credits to finish your sermon series."* Then nurture toward the $19 plan.

### 6.2 Annual Push at Onboarding
During signup, present the annual plan prominently: *"Most pastors choose annual—saves $38 and gets approved in one budget cycle."* One annual subscriber = 12 months of locked-in revenue.

### 6.3 "Sermon Season" Surge Promotions
Run credit bonus events before Easter and Christmas (high-usage seasons):
- *"Easter Prep Bonus: Buy any credit pack, get 25% extra credits."*
This captures revenue when pastors are most stressed and most willing to spend.

### 6.4 Referral Program
Pastors trust peer recommendations more than ads. *"Give 100 credits, Get 100 credits"* is cheap acquisition. A referred pastor who subscribes at $19/mo pays for 20+ referral bonuses over their lifetime.

### 6.5 Seminary / Student Pricing
Offer free or $5/mo plans to seminary students. They become paying pastors in 2–3 years. This is a long-term land-and-expand play.

### 6.6 Lifetime Deal (LTD) for Early Funding
For the first 100–200 beta users, offer a **$299 lifetime deal** (500 credits/mo, single user). This injects early cash for development and creates an invested evangelist base. **Do not keep this open forever**—it becomes a support burden. Close it after MVP validation.

---

## 7. What NOT to Do

| Model | Why It Fails for YouPastor |
|-------|---------------------------|
| **Pure top-up credits** | Zero MRR. You can't build a sustainable SaaS on lumpy revenue. Pastors also feel "nickel-and-dimed" and stop using the app when credits run low. |
| **Pure one-time purchase** | Impossible. OpenRouter bills you per API call forever. A $100 one-time sale costs you money in month 6. |
| **Expensive unlimited subscription ($50+/mo)** | Kills adoption in your target demographic (200-member churches). Only the Church Plan at $49 works because it supports *multiple users*, splitting the cost. |
| **Pay-per-sermon** | Too transactional. Pastors want a tool in their workflow, not a vending machine. |

---

## 8. Pricing Page Strategy

Your SEO strategy drives traffic to specific landing pages. Each one should show the same pricing structure but contextualized:

- `/sermon-prep-ai` → *"Prepare your sermon for less than the cost of a study Bible per month."*
- `/church-email-templates` → *"Draft church emails in minutes. Free for light use. $19/mo for your full workflow."*
- `/small-group-discussion-guide-generator` → *"Repurpose Sunday into midweek. 400 credits covers your entire series."*

Include a **credit calculator** on the pricing page:
> *"I write ___ sermons per month and ___ emails/announcements."* → *"Recommended: Pastor Plan with 1 top-up during busy seasons."*

---

## 9. Bottom Line

**Go with the Base + Meter hybrid.**

- **Free:** 75 credits/mo (distribution + trial)
- **Pastor:** $19/mo or $190/yr, 400 credits (your core revenue driver)
- **Church:** $49/mo or $490/yr, 1,200 credits, 5 users (team expansion)
- **Top-ups:** $9–$39 packs for overflow months

This respects pastor budgets, covers your AI costs sustainably, creates the MRR you need to hit $5K by Month 6, and aligns perfectly with your SEO-led, free-tool-funnel distribution strategy.

---

## Open Questions

1. Exact OpenRouter API cost per task type (needs real usage data to finalize credit costs)
2. Should the free tier require a credit card for signup, or truly free?
3. Do churches in developing markets need a lower regional price point?
4. Should theological denomination add-ons be a separate upsell or included?

---

## Related

- [[YouPastor-PRD]] — Product requirements
- [[YouPastor-Distribution-Strategy]] — SEO and marketing
- [[YouPastor-Subscription]] — Payment infrastructure (Paddle)
