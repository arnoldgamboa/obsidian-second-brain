---
tags: [mind-dump, prospecting, cold-outreach, prospeo, mcp]
date: 2026-07-17
status: inbox
source: telegram
brain_schema: 1
title: "Prospeo free credits for cold-outreach testing"
type: note
created: 2026-07-17
updated: 2026-07-17
area: Inbox
aliases: []
---

# Prospeo free credits for cold-outreach testing

## Raw thought

Got free credits for Prospeo. I can use this to test cold calls/outreach by pulling a list of actual target prospects and checking whether the contact data and emails are valid.

Prospeo MCP documentation: https://prospeo.io/api-docs/mcp

## Free-credit offer

1. Sign up free at https://prospeo.io and verify the email address.
2. Open **Upgrade** in the top-right.
3. Choose **Monthly → Growth**.
4. At checkout, select **Have a coupon?** and enter `YSKEUI`.
5. Add the billing address; a company address is acceptable and no card is required.
6. Confirm the upgrade.

Credits should land instantly. The coupon is expected to remain valid for roughly one week from July 17, 2026, so it should be tested soon.

## MCP notes

- Hosted MCP endpoint: `https://mcp.prospeo.io`
- Authentication: OAuth or a Prospeo API key in the `X-KEY` header.
- Local package: `@prospeo/prospeo-mcp-server`
- Main capabilities:
  - Search people and companies using ICP filters.
  - Enrich professional emails and mobile numbers.
  - Enrich company details, including headcount, funding, and technology stack.
  - Check current plan and remaining credits with `get_account_info`.
- Credit examples from the documentation:
  - Person email enrichment: 1 credit.
  - Person email + mobile enrichment: 10 credits.
  - Person/company search: 1 credit per page.
  - Company enrichment: 1 credit per matched company.

## Possible next actions

- Configure Prospeo as a Hermes MCP server after the account and API key are ready.
- Define a narrow ICP and pull a small list of real prospects before spending credits broadly.
- Start with email-only enrichment, then validate deliverability and relevance before spending 10 credits per mobile number.
- Use the first test to evaluate data quality, match rate, and whether the resulting contacts are suitable for cold email or calls.
