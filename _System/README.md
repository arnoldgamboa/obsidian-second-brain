---
brain_schema: 1
title: Markdown Brain System
type: reference
status: active
created: 2026-07-21
updated: 2026-07-21
area: Second Brain
tags: [second-brain, system, markdown-brain]
aliases: [Second Brain System]
---

# Markdown Brain System

This vault uses **Markdown Brain**, an Obsidian-compatible, Markdown-first knowledge system.

## Source of truth

Ordinary Markdown notes are canonical. The following are generated and can be rebuilt:

- `Home.md` generated navigation block
- Top-level `_Index.md` generated catalog blocks
- Generated catalog blocks inside existing `content-index.md` notes
- `_System/brain-manifest.json`
- `_System/health-report.md`

Do not edit generated blocks between `markdown-brain:auto` markers. Update source notes and regenerate.

## Note structure

Managed notes use consistent frontmatter. Evolving knowledge notes use:

- **Upper deck:** concise current truth, decisions, open loops, relationships
- **Lower deck:** dated history, evidence, provenance, and changes

Use templates in `_System/templates/` for new notes.

## Agent update rule

1. Search before creating.
2. Read the complete target note before editing.
3. Append meaningful evidence to the lower deck.
4. Reconcile the upper deck when current truth changes.
5. Update `updated`.
6. Preserve unknown metadata and manual sections.
7. Regenerate indexes and validate.

## Maintenance

The reusable Hermes skill is `markdown-brain`. Load it and use the returned `skill_dir`:

```bash
python3 <skill_dir>/scripts/brain_maintain.py index /opt/data/My-Second-Brain
python3 <skill_dir>/scripts/brain_maintain.py validate /opt/data/My-Second-Brain
python3 <skill_dir>/scripts/brain_maintain.py search /opt/data/My-Second-Brain "query"
```

## Safety

- Keep client vaults isolated.
- Never store credentials; use `[REDACTED]`.
- Back up before bulk migration.
- Do not silently rename or delete notes.
- Markdown remains useful even if every generated artifact is removed.
