---
tags: [bookmark, ai-agents, knowledge-management, memory, open-source, hermes-agent]
date: 2026-07-20
source: https://github.com/garrytan/gbrain
brain_schema: 1
title: GBrain
type: bookmark
status: active
created: 2026-07-20
updated: 2026-07-21
area: Resources
aliases: [GBrain knowledge runtime]
---

# GBrain

<!-- brain:upper-deck -->

> [!summary] Current truth
> GBrain is a substantial Markdown-first knowledge runtime whose strongest ideas—structured metadata, current truth separated from history, provenance, and rebuildable indexes—are useful for Hermes, but deploying the full runtime is currently unnecessary for this small Obsidian vault.

## Why It Matters

GBrain demonstrates how agents can treat Markdown as canonical while deriving stronger retrieval, graph, timeline, and synthesis capabilities. Its design informed the local [[_System/README|Markdown Brain system]].

## Key Takeaways

- Markdown and frontmatter can remain the durable source of truth.
- Current synthesized knowledge should be separated from chronological evidence.
- Derived databases and indexes should be rebuildable.
- Search should return evidence and provenance, not only matching filenames.
- Shared agent knowledge requires strong source and client isolation.

## Caveats

- The runtime adds Bun, database, embedding, migration, and operational complexity.
- The studied release had unresolved source-scoping concerns and no dedicated Hermes end-to-end runner.
- It is not recommended as the authoritative writer for the live vault.

## Related

- [[Paperclip]]
- [[OpenHuman]]
- [[_System/README|Markdown Brain System]]

<!-- brain:lower-deck -->

---

## History and Evidence

### 2026-07-21 — Architecture assessment completed

**Source:** Repository study of https://github.com/garrytan/gbrain

- Recommended borrowing its design principles without deploying GBrain for the current vault.
- Recommended a dedicated Obsidian vault for each client and an optional isolated retrieval service only when scale justifies it.

### 2026-07-20 — Source captured

**Source:** https://github.com/garrytan/gbrain

- Designed as persistent memory and institutional knowledge for personal agents or teams.
- Supports scoped access and knowledge retrieval through CLI and MCP.
- Includes entity extraction, typed relationships, enrichment, consolidation, and autonomous maintenance cycles.
- Can run locally with PGLite or use Postgres in larger deployments.
