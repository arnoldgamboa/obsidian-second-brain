---
tags: [linkedin, engagement, cron, template]
created: 2026-07-02
status: active
brain_schema: 1
title: "LinkedIn Engagement Cron Output Template"
type: note
updated: 2026-07-02
area: ArwenDigital
aliases: []
---

# LinkedIn Engagement Cron Output Template

Use this structure for the weekday Telegram output.

```text
LinkedIn engagement suggestions — YYYY-MM-DD

Power-list coverage:
- Checked: [N] target people from [[power-list]]
- Freshness windows searched: same-hour [N candidates], last 4 hours [N], last 24 hours [N], last 5 days [N fallback]
- Strong candidates found from power list: [N]
- Fallback broad-search candidates used: [N]
- Already-commented posts skipped via [[engaged-posts-log]]: [N]
- Power-list candidates skipped as too thin/unsubstantial to comment on: [N]

1) [Author name] — [Category: operator-founder / agency-consultant / ops-systems / revops-gtm / practical-ai / creator-operator]
Post: [LinkedIn URL or stable identifier]
Why this person matters: [1 sentence]
Why this post is worth engaging: [1 sentence]
Comment type: [value-add / supportive-deepening / challenge-nuance / witty-relatable]
Relationship angle: [1 sentence]
Suggested reply:
"[2–5 sentence reply]"

Follow-up if they respond:
[one short suggestion]

2) ...

Reply with:
- "yes to all" to approve all replies
- "approve 1,3,5" to approve selected replies
- edits in plain text if you want changes
```

## Notes

- Do not include weak candidates just to reach 5.
- If fewer than 5 strong candidates exist, return fewer and explain why.
- Never post comments from the scheduled job.
- Always report how many candidate posts were skipped because they were already in [[engaged-posts-log]].
