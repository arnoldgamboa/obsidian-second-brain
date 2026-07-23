---
tags: [meeting-notes, bukidtek, client-work, budget-request, liquidation]
date: 2026-07-16
status: active
source: chat
transcript: https://notes.granola.ai/t/4708c0de-6dd5-4a2f-b622-5a1f191b7ca0-00demib2
attendees: [Arnold, Noah]
brain_schema: 1
title: "Noah / Bukidtek — Budget Request and Liquidation Redesign"
type: meeting
created: 2026-07-16
updated: 2026-07-21
area: ArwenDigital
project: Bukidtek
aliases: [Bukidtek budget redesign, Bukidtek liquidation redesign]
---

# Noah / Bukidtek — Budget Request and Liquidation Redesign

<!-- brain:upper-deck -->

> [!summary] Current truth
> Bukidtek’s budget request must support multiple communities and carry approved line items into a mirrored liquidation flow. Implementation starts with budget requests, followed by liquidation and community-balance reporting, with incremental staging review.

## Decisions

- One budget request may contain multiple communities.
- Line items are organized by community, farm, activity, workers/days, and amount.
- Approved request line items carry into liquidation as locked references; actual amounts remain editable and unplanned expenses may be added.
- Receipts attach to each budget line item rather than each farmer.
- Community balances carry forward across cycles and exclude overhead.
- Farmers do not enter financial data; Romeo handles budget requests.

## Commitments

- [ ] Arnold — implement the budget-request redesign first.
- [ ] Arnold — push changes incrementally to staging and notify Noah through Basecamp comments.
- [ ] Arnold — implement the mirrored liquidation stage.
- [ ] Arnold — implement community balance and reporting.
- [ ] Arnold — test the complete flow with Romeo and Noah.
- [ ] Arnold — schedule the follow-up review for Friday, 7 August 2026, at the same time.

## Related

- [[40 - ArwenDigital/client-work/bukidtek/_Index|Bukidtek]]

<!-- brain:lower-deck -->

---

## History and Evidence

### 2026-07-16 — Meeting with Noah

**Source:** [Granola transcript](https://notes.granola.ai/t/4708c0de-6dd5-4a2f-b622-5a1f191b7ca0-00demib2)

**Deadline:** Finish the tasks before the first week of August.

#### Budget Request Redesign

- Budget request should support multiple communities in a single submission.
- Line items should be broken down by community, activity type, and per-farmer cost.
- Each line item should include community, farm, activity, number of workers/days, and amount.
- Totals should be broken out by activity, overhead, community carryover, and grand total.
- Overhead remains but is excluded from community surplus/deficit tracking.
- Farmers are not expected to enter financial data; Romeo handles budget requests.
- Future farmer input should focus on photos, short farm updates, and other simple field updates.

#### Liquidation Stage

- Liquidation mirrors the budget-request structure by community, activity, and per-farmer costs.
- Budget-request data carries over as a locked/read-only reference.
- Only amounts are editable; line items are not editable.
- New line items can be added for unplanned expenses.
- Actual amount is entered manually per farmer and is not derived from receipt totals.
- Multiple receipts may be uploaded per budget line item.

#### Community Balance and Reporting

- Community profile shows total requested, total liquidated, and surplus/deficit.
- Running balance accumulates across budget cycles and carries forward week to week.
- Community profile lists assigned farms.
- Balance tracking is community-level only and excludes overhead.
- Cycle delta or settlement tracking is no longer relevant.

#### Implementation Priority

1. Budget request redesign.
2. Liquidation stage mirroring the request structure.
3. Community balance and reporting.
4. Staging review with Noah and Romeo.
