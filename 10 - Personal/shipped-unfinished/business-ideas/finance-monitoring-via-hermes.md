# Finance Monitoring via Hermes

- Will need to create finance monitoring via Hermes after I received Zed's billing on May 15
- Trigger: Zed billing arrives (May 15)
- Goal: Build a system to track finances through Hermes Agent

## Context
- Zed is likely Zed editor (AI code editor) — subscription billing
- Want to use Hermes to monitor/track finances once billing comes in
- Could involve: expense tracking, subscription monitoring, budget alerts, financial dashboards

## Next Steps
- [ ] Receive Zed billing on May 15
- [ ] Design finance monitoring workflow in Hermes
- [ ] Implement tracking system (spreadsheets, Notion, Airtable, or custom)

## Ideas to Explore
- Subscription tracker (monthly/annual costs)
- Expense categorization
- Budget alerts via cronjob
- Financial brief (weekly/monthly spending summary)
- Integration with existing finance tools

## Proposed Workflow
1. **Upload PDF statement** (bank, credit card, or Zed billing)
2. **Hermes extracts + curates** transactions from the PDF
3. **Auto-categorization** (subscriptions, food, transport, ministry, business, etc.)
4. **Sync to Google Sheet** — maintained month-to-month by Hermes
5. **Big picture analysis** — spending trajectory over time
6. **Recommendations** — personalized suggestions to improve personal spending
