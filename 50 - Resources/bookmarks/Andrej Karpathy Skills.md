---
tags: [bookmark, ai-coding, llm, claude-code, opencode, skills]
category: AI Tools
type: Repo
url: https://github.com/forrestchang/andrej-karpathy-skills
added: 2026-04-30
---

# Andrej Karpathy Skills

A single `CLAUDE.md` file to improve Claude Code behavior, derived from [Andrej Karpathy's observations](https://x.com/karpathy/status/2015883857489522876) on LLM coding pitfalls.

## What It Is

Behavioral guidelines that make AI coding agents behave more like careful senior engineers. The repo provides a `CLAUDE.md` (and now `CURSOR.md` + plugin support) that you drop into a project root.

## The Four Principles

1. **Think Before Coding** — State assumptions explicitly; ask when confused; present multiple interpretations instead of silently picking one; push back if a simpler approach exists.
2. **Simplicity First** — No speculative features, no abstractions for single-use code, no "flexibility" that wasn't requested. If 200 lines could be 50, rewrite it.
3. **Surgical Changes** — Touch only what the request requires. Don't refactor adjacent code, don't "improve" unrelated comments, don't delete pre-existing dead code unless asked. Clean up only what your own changes made unused.
4. **Goal-Driven Execution** — Turn vague tasks into verifiable goals with tests. "Fix the bug" becomes "Write a test that reproduces it, then make it pass."

## How to Use

- **Claude Code:** Install as a plugin (`/plugin install andrej-karpathy-skills@karpathy-skills`) or curl the `CLAUDE.md` into your project root.
- **Cursor:** Use the included `.cursor/rules/karpathy-guidelines.mdc` rule.
- **OpenCode:** Drop `CLAUDE.md` in the project root — OpenCode auto-loads it via default `contextPaths`.

## Key Insight

> "LLMs are exceptionally good at looping until they meet specific goals... Don't tell it what to do, give it success criteria and watch it go."
> — Andrej Karpathy

## Related

- [[Superpowers — Agentic Skills Framework]] — Skill-based dev methodology for coding agents
- [[Figma Skills for MCP]] — Pre-built AI skills for Figma
- [[Pastor AI Skills]] — 13 AI-powered workflow skills for pastors
