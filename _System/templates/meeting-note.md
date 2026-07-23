---
brain_schema: 1
title: "{{meeting title}}"
type: meeting
status: active
created: "{{date}}"
updated: "{{date}}"
area: "{{area}}"
project: "{{project}}"
tags: [meeting]
aliases: []
source: "{{transcript or meeting source}}"
attendees: []
---

# {{meeting title}}

<!-- brain:upper-deck -->

> [!summary] Current truth
> {{meeting outcome in one or two sentences}}

## Decisions

- {{decision}}

## Commitments

- [ ] {{owner}} — {{commitment}} — {{due date if known}}

## Open Questions

- {{unresolved question}}

## Related

- {{project, people, or client links}}

<!-- brain:lower-deck -->

---

## History and Evidence

### {{date}} — Meeting

**Source:** {{transcript URL or notes}}

## Detailed Notes

{{chronological or topic-based meeting detail}}
