---
tags: [linkedin, engagement, ai-employee, source-of-truth]
created: 2026-07-02
status: active
brain_schema: 1
title: "LinkedIn Engagement System"
type: index
updated: 2026-07-02
area: ArwenDigital
aliases: []
---

# LinkedIn Engagement System

This folder is the source of truth for Arnold's daily LinkedIn engagement cron.

## Files

- [[engagement-strategy]] — the operating strategy adapted from the HeyReach video and Arnold's positioning.
- [[power-list]] — the rotating target list of people/accounts to prioritize before broad search.
- [[engaged-posts-log]] — hard-skip log of posts Arnold has already commented on; the cron must not suggest these again.
- [[2026-06-26-linkedin-ai-automation-people-to-follow]] — seed note for building a LinkedIn follow/power list around AI automation business development.
- [[comment-style-guide]] — Arnold's preferred comment types, voice, and approval rules.

## Current goal

Move the weekday LinkedIn engagement cron from broad/random topical search to a relationship-driven power-list system:

1. Prioritize specific people whose audiences match Arnold's AI Employee buyers.
2. Find recent posts from those people first.
3. Check [[engaged-posts-log]] and skip any post already touched before, even if it is still recent or highly relevant.
4. Score posts by buyer relevance, relationship value, recency, and conversation quality.
5. If the power list does not surface substantial enough content to comment on, search outside the list using the same freshness ladder and buyer-fit rules.
6. Draft useful comments for Telegram approval only.
7. Do not post automatically from the cron.

## Related automation

- Hermes cron job: `LinkedIn engagement suggestions — weekdays`
- Job ID: `b46111d82f97`
- Schedule: weekdays 10:00 AM Asia/Manila
- Delivery: Telegram
