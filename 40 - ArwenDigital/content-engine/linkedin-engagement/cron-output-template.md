---
tags: [linkedin, engagement, cron, template]
created: 2026-07-02
status: active
---

# LinkedIn Engagement Cron Output Template

Use this structure for the weekday Telegram output.

```text
LinkedIn engagement suggestions — YYYY-MM-DD

Power-list coverage:
- Checked: [N] target people from [[power-list]]
- Strong candidates found from power list: [N]
- Fallback broad-search candidates used: [N]

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
