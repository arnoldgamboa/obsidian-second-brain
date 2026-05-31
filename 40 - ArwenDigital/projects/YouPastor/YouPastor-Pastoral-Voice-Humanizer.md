---
tags: [youpastor, product, ai-feature, pastoral-voice]
date: 2026-05-31
status: implementation-reference
source: hermes-session
---

# YouPastor Pastoral Voice / Humanizer Feature

## Core idea

Build a YouPastor rewrite feature that helps pastors take rough AI-generated drafts and make them sound more natural, pastoral, warm, and human.

Do **not** frame this primarily as “Humanizer” in the app. That sounds generic and AI-tool-ish.

Better labels:

- Make this sound more pastoral
- Make this sound more like me
- Warm this up
- Remove AI tone
- Pastoral voice pass
- Rewrite in a more natural voice
- Make this ready to send

## What it should do

The feature should not merely “make text less AI.”

It should help pastors revise drafts so they sound:

- more pastoral
- more natural
- less generic
- less polished in a fake way
- more appropriate for church communication
- more like something a real pastor would say

Example transformation:

> We invite you to join us for a powerful time of worship, fellowship, and spiritual growth as we gather together to experience the transformative presence of God.

Into:

> We’d love for you to join us this Sunday. We’ll worship together, open Scripture, and make space to respond to what God is doing in our lives.

Less hype. More pastor.

## Basic technical flow

At MVP level, this is another AI action in the app.

1. User has text in a draft field.
2. User clicks/selects **Make this sound more pastoral**.
3. App sends the current text to the LLM with a specialized instruction.
4. LLM returns a revised version.
5. App shows:
   - original
   - revised version
   - actions like **Accept**, **Try again**, **Make warmer**, **Shorter**, or **More direct**

A separate model or fine-tune is not necessary at first. Start with prompt engineering.

## Core prompt draft

```text
You are editing copy for a pastor.

Rewrite the text so it sounds natural, pastoral, warm, and human. Remove generic AI-sounding language, hype, overly polished phrases, and vague spiritual cliches.

Preserve the meaning. Do not add new claims. Do not make it sound like marketing copy.

Use simple, clear language. Keep the pastor’s voice present. Make it suitable for a real church context.

Avoid:
- “powerful time”
- “transformative experience”
- “spiritual growth” as filler
- “unlock”
- “journey”
- “impactful”
- “vibrant”
- “life-changing” unless clearly warranted
- overly dramatic church marketing language

Prefer:
- clarity
- warmth
- humility
- directness
- Scripture-shaped language when appropriate
- practical pastoral tone

Return only the rewritten version.
```

## Rewrite modes

Instead of one generic humanizer button, offer a few pastoral rewrite modes.

### 1. More pastoral

For announcements, emails, devotionals, and sensitive communication.

Prompt direction:

> Make this warmer, gentler, and more pastoral without becoming sentimental.

### 2. More concise

For announcements and emails.

Prompt direction:

> Make this shorter and clearer. Keep the tone warm, but remove filler.

### 3. More like me

This is the premium version.

The user provides a few writing samples, and YouPastor learns their tone.

Prompt direction:

> Rewrite this in the pastor’s voice using the writing profile below.

### 4. Less AI / less generic

For anything that sounds overproduced.

Prompt direction:

> Remove generic AI phrasing, inflated language, and polished-but-empty sentences.

### 5. More congregational

For messages to the church.

Prompt direction:

> Rewrite this so it sounds like a pastor speaking to their own church family, not a brand speaking to an audience.

## Product opportunity: Pastoral Voice

The strongest version is not just **Humanize**.

The stronger feature is:

## Pastoral Voice

This could become a paid feature.

App language:

> Save your pastoral voice so YouPastor can help drafts sound more like you.

During onboarding, ask pastors to paste:

- one sermon excerpt
- one church email
- one announcement
- one devotional or pastoral note

YouPastor creates a voice profile with:

- tone: warm, direct, reflective, encouraging
- sentence style: short, simple, spoken
- theological language: uses Scripture naturally, avoids hype
- communication style: invitational, not pushy
- common closings or phrases
- words to avoid

Future generations can then use that profile.

## MVP implementation path

### Phase 1 — Simple rewrite button

Add a button/action:

**Make this sound more pastoral**

Behind the scenes, it should:

- remove AI tone
- reduce hype
- simplify wording
- keep the pastor’s voice
- preserve meaning
- make the copy feel appropriate for church context

Low effort. High value.

### Phase 2 — Add rewrite options

After generation, offer:

- Shorter
- Warmer
- More direct
- Less AI-sounding
- More devotional
- More announcement-like

### Phase 3 — Add saved pastor voice

Let users save a voice profile from writing samples.

This becomes a major differentiator from “just use ChatGPT.”

### Phase 4 — Add before/after review

Show original and revised copy side by side so pastors trust it and stay in control.

## Data needed

For the basic version:

- text to rewrite
- optional content type: sermon, devotional, announcement, email, social post

For the better version:

- pastor writing samples
- preferred tone settings
- denomination/theological preferences, if relevant
- disliked words or phrases
- audience context: church members, leaders, volunteers, guests, small group, etc.

## Suggested UI

Inside any generated draft, add a section:

**Refine this draft**

Options:

- Make it more pastoral
- Make it shorter
- Make it warmer
- Make it less AI-sounding
- Make it sound more like me
- Make it ready to send

For desktop, this could be a right-side panel or inline action menu.

## Recommendation

Start simple:

**Button:** `Make this sound more pastoral`

Then later build the bigger paid feature:

## Pastoral Voice Profile

That is the feature that could make YouPastor feel meaningfully different from “just use ChatGPT.”

## Related

- [[YouPastor-PRD]]
- [[YouPastor-Branding]]
- [[YouPastor-Onboarding-Email-Sequence]]
