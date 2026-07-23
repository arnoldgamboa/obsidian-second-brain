---
tags: [linkedin, engagement, strategy, ai-employee]
created: 2026-07-02
status: active
source: "HeyReach YouTube video: Full Guide to Engaging & Commenting on LinkedIn"
brain_schema: 1
title: "LinkedIn Engagement Strategy"
type: note
updated: 2026-07-02
area: ArwenDigital
aliases: []
---

# LinkedIn Engagement Strategy

## Purpose

Use LinkedIn comments to build relationships, visibility, and buyer trust for Arnold's AI Employee / AI agent automation services.

This is not random engagement. The goal is to repeatedly show up in the right conversations with useful, practical comments that small-business operators, agency owners, consultants, and ops-minded leaders would respect.

## Core principle

Do not start with random posts. Start with the right people and audiences.

Daily engagement should prioritize:

1. People whose audience overlaps with Arnold's buyers.
2. Posts where Arnold can add a practical operator perspective.
3. Conversations that can lead to trust, relationship capital, or referral surface.

## Target audience priority

Use this mix when building or refreshing the power list:

1. **70% small-business operators / founders / owners**
   - business owners, bootstrapped founders, service-business operators, local/small-business leaders
   - highest priority because they map closest to AI Employee buyers

2. **20% adjacent operators / agencies / consultants / fractional leaders**
   - agency owners, ops consultants, RevOps leaders, fractional COOs/CMOs, business systems consultants
   - useful for partnerships, referrals, and buyer-adjacent conversations

3. **10% practical AI professionals / builders**
   - only include if their content translates into deployable workflows, not AI hype
   - avoid pure model/tool/demo accounts unless the comments can be grounded in business operations

## Hard skip rules

Skip posts that are mostly:

- AI hype without business outcome
- model/tool chatter for technical audiences only
- viral engagement bait
- politics, culture war, outrage, or personal attacks
- posts where Arnold's comment would feel forced
- posts with huge comment sections where Arnold's reply will be buried unless the author/audience is unusually valuable

Also hard-skip any post already listed in [[engaged-posts-log]]. This is post-level dedupe, not just author-level rotation. Do not suggest the same LinkedIn post twice, even if:

- the author is still a good target
- the post is still recent
- the previous comment was several days ago
- the post appears again through a different URL, `activity_id`, `share` URN, or `ugcPost` URN

Normalize candidates by extracting the `activity-<digits>` ID from public URLs and comparing it against the log's `activity_id`, post URL, and canonical URN columns.

## Freshness-first search ladder

LinkedIn comments should prioritize fresh posts where Arnold can appear early in the conversation.

Search and select candidates in this order:

1. **Same-hour posts** — prioritize posts published within the current hour or roughly the last 60 minutes.
2. **Last 4 hours** — only expand here if the same-hour set does not produce enough strong untouched candidates.
3. **Last 24 hours** — only expand here if the first two windows do not produce enough strong candidates.
4. **Last 5 days** — fallback window for high-fit power-list targets or unusually strong buyer-aligned posts when narrower windows do not produce enough strong, untouched candidates.
5. **Older than 5 days** — normally skip unless the author is extremely high-fit and the conversation is still visibly active.

Do not start with “last 5 days” searches. Use the narrowest freshness window first, then expand gradually. A fresher 8/10 fit post is usually better than an older 10/10 fit post because early comments have more visibility.

If the power-list search produces posts but the visible/title/snippet content is too thin, generic, or unsubstantial to write a useful comment, do not force a comment. Treat those as weak candidates and move to broad topical search outside the power list using the same freshness ladder, target mix, and engaged-posts-log skip.

## Candidate scoring

### Person score

Score target people from 0–10:

- +4 small-business owner/operator audience
- +3 adjacent ops / agency / consultant / fractional leader relevance
- +2 practical AI/workflow relevance
- +2 posts consistently
- +2 relationship value / useful network node
- -3 pure AI hype audience

### Post score

Score candidate posts from 0–10:

- +4 same-hour or last-60-minutes post
- +3 posted in the last 4 hours
- +2 posted in the last 24 hours
- +1 posted in the last 5 days only if person/post fit is strong
- +3 workflow/admin/follow-up/ops angle
- +2 clear business outcome
- +2 conversation-worthy
- +2 Arnold can add a practical operator take
- -3 generic AI demo/tool hype
- -3 culture-war/politics/outrage bait
- -2 too crowded or too generic

### Thresholds

- **8–10:** strong candidate; include if comment quality is good
- **5–7:** use only if the queue needs volume
- **0–4:** skip

## Daily workflow for the cron

1. Load [[power-list]] and [[engaged-posts-log]].
2. Prefer priority A and B targets not recently engaged.
3. Search for recent public LinkedIn posts from those target names/profiles using the freshness-first ladder: same-hour first, then last 4 hours, then last 24 hours, then last 5 days only as fallback.
4. Do not expand to a wider time window until the narrower window has been checked and produced too few strong untouched candidates.
5. Normalize each candidate by URL, `activity_id`, `share` URN, and `ugcPost` URN when available.
6. Remove any candidate that matches [[engaged-posts-log]] before scoring.
7. Score each remaining candidate using the person/post scoring above, giving freshness real weight.
8. Select up to 5 strongest fresh posts.
9. Use broad topic search outside the power list as fallback if the power-list search produces fewer than 5 good fresh candidates, or if the candidates found do not have enough substantial visible content to comment on. Apply the same freshness ladder, target mix, and engaged-posts-log skip to fallback candidates.
10. Draft comments using [[comment-style-guide]].
11. Deliver to Telegram for approval.
12. Never post comments automatically from the scheduled job.

## Weekly maintenance

Every Monday or during a manual review:

- Add newly discovered high-fit people.
- Remove inactive or low-fit targets.
- Promote/demote priority based on quality of conversations.
- Review whether the list still matches the 70/20/10 target mix.

## Future enhancement

After the approval/posting workflow is stable, track:

- approved comments
- posted comments
- author replies
- follow-up opportunities
- people who consistently produce good buyer-aligned conversations
