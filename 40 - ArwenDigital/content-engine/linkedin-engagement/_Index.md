---
tags: [linkedin, engagement, ai-employee, source-of-truth]
created: 2026-07-02
status: active
---

# LinkedIn Engagement System

This folder is the source of truth for Arnold's daily LinkedIn engagement cron.

## Files

- [[engagement-strategy]] — the operating strategy adapted from the HeyReach video and Arnold's positioning.
- [[power-list]] — the rotating target list of people/accounts to prioritize before broad search.
- [[comment-style-guide]] — Arnold's preferred comment types, voice, and approval rules.

## Current goal

Move the weekday LinkedIn engagement cron from broad/random topical search to a relationship-driven power-list system:

1. Prioritize specific people whose audiences match Arnold's AI Employee buyers.
2. Find recent posts from those people first.
3. Score posts by buyer relevance, relationship value, recency, and conversation quality.
4. Draft useful comments for Telegram approval only.
5. Do not post automatically from the cron.

## Related automation

- Hermes cron job: `LinkedIn engagement suggestions — weekdays`
- Job ID: `b46111d82f97`
- Schedule: weekdays 10:00 AM Asia/Manila
- Delivery: Telegram
