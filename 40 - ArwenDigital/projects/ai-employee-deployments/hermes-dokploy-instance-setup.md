---
tags: [ai-employee, hermes, dokploy, llm-setup, operations]
date: 2026-06-01
status: parked
source: telegram
---

# Hermes Dokploy Instance Setup

Save this as the working setup checklist for the future AI Employee / agent deployment business.

## Why this matters

For each future customer or internal AI Employee instance, treat Hermes as a small persistent service:

1. Persistent Hermes home volume
2. LLM provider/API key configured
3. Gateway configured, usually Telegram
4. Tools/skills enabled
5. Health checks verified before handoff

## Dokploy app shape

Use a Docker Compose app where possible.

Persist Hermes data outside the container:

```bash
HERMES_HOME=/data/.hermes
```

Hermes keeps config, sessions, skills, memories, auth, and logs under `~/.hermes`, so in containers make the path explicit and backed by a volume.

Example volume target:

```yaml
volumes:
  hermes-data:
```

Mount it to:

```bash
/data
```

## Basic Dockerfile shape

```dockerfile
FROM python:3.12-slim

RUN apt-get update && apt-get install -y \
    curl git tmux bash ca-certificates build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN curl -fsSL https://raw.githubusercontent.com/NousResearch/hermes-agent/main/scripts/install.sh | bash

ENV PATH="/root/.local/bin:$PATH"
ENV HERMES_HOME="/data/.hermes"

VOLUME ["/data"]

CMD ["hermes", "gateway", "run"]
```

## Environment variables

Minimum:

```bash
HERMES_HOME=/data/.hermes
```

LLM provider keys, depending on chosen provider:

```bash
OPENROUTER_API_KEY=...
OPENCODE_GO_API_KEY=...
ANTHROPIC_API_KEY=...
OPENAI_API_KEY=...
KIMI_API_KEY=...
GOOGLE_API_KEY=...
DEEPSEEK_API_KEY=...
```

Telegram gateway:

```bash
TELEGRAM_BOT_TOKEN=...
```

Do not reuse the same Telegram bot token across two live Hermes instances unless intentionally coordinating them. They can conflict over updates.

## First-time LLM setup

Open the Dokploy terminal/shell for the container and run:

```bash
hermes setup
```

Or just model setup:

```bash
hermes setup model
```

Model picker:

```bash
hermes model
```

For non-interactive OpenRouter setup:

```bash
hermes config set model.provider openrouter
hermes config set model.default moonshotai/kimi-k2
```

Alternative example:

```bash
hermes config set model.provider openrouter
hermes config set model.default anthropic/claude-sonnet-4
```

If using OpenCode Go, prefer `hermes model` interactively the first time because provider/model names may vary by Hermes version.

Verify the model:

```bash
hermes chat -q "Say hello and confirm the model is working."
```

## Health checks

Run inside the container:

```bash
hermes doctor
hermes status --all
hermes config check
```

Fix missing env vars/config, then restart the Dokploy app.

## Telegram gateway setup

Run:

```bash
hermes gateway setup
```

Pick Telegram and provide the bot token if it is not already in env.

In containers, the running command should usually be foreground mode:

```bash
hermes gateway run
```

Avoid `hermes gateway install` inside the Dokploy container; that is for systemd/background service setups.

## Pair / authorize user

Message the new Telegram bot.

If pairing is required, check pending requests in the container:

```bash
hermes pairing list
```

Approve:

```bash
hermes pairing approve <id>
```

From Telegram, send:

```text
/status
/sethome
```

`/sethome` makes the current chat the default delivery target.

## Toolsets to enable

Useful defaults for an AI Employee deployment:

```bash
hermes tools enable terminal
hermes tools enable file
hermes tools enable web
hermes tools enable skills
hermes tools enable memory
hermes tools enable session_search
hermes tools enable cronjob
hermes tools enable delegation
hermes tools enable todo
hermes tools enable clarify
hermes tools enable messaging
```

Or run the interactive UI:

```bash
hermes tools
```

Restart the gateway/container after changing tools.

## Optional profile/memory/skills migration

If the new instance should behave like an existing Hermes install, copy or export/import:

```bash
~/.hermes/config.yaml
~/.hermes/.env
~/.hermes/skills/
~/.hermes/memories/
~/.hermes/auth.json
```

Safer approach:

```bash
hermes profile export default
```

Then import on the new instance.

For separate customer instances, do not blindly copy personal memory, auth, or Telegram configuration.

## Recommended Compose shape

```yaml
services:
  hermes:
    build: .
    container_name: hermes-agent
    restart: unless-stopped
    environment:
      HERMES_HOME: /data/.hermes
      OPENROUTER_API_KEY: ${OPENROUTER_API_KEY}
      TELEGRAM_BOT_TOKEN: ${TELEGRAM_BOT_TOKEN}
    volumes:
      - hermes-data:/data
    command: ["hermes", "gateway", "run"]

volumes:
  hermes-data:
```

## Final verification checklist

Inside the container:

```bash
hermes doctor
hermes chat -q "What model are you using?"
hermes gateway status
```

From Telegram:

```text
/status
/platforms
```

Then test a real tool call:

```text
what time is it on the server?
```

Hermes should answer from live terminal output, not from memory.

## Recommended internal default

For Arnold's own future setup:

- Dokploy app with persistent `/data`
- `HERMES_HOME=/data/.hermes`
- OpenCode Go or OpenRouter as primary provider
- Kimi K2.6 if available in provider picker
- Telegram gateway
- Tools: terminal, file, web, skills, memory, session_search, cronjob, delegation
- Telegram `/sethome`
- `hermes doctor` before relying on it

## Key first-time commands

```bash
hermes setup
hermes model
hermes doctor
hermes gateway setup
hermes gateway run
```

## Related

- [[_Index|AI Employee Deployments]]
- [[seo-ads-game-plan]]
- [[landing-page-copy]]
