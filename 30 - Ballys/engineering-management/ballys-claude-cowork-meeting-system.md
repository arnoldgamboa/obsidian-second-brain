# Bally's Meeting OS via Claude Co-work + Obsidian

- Use Bally's-issued machine with Bally's Claude Co-work account
- Dedicated work-only Obsidian vault (not synced to personal vault)
- Goal: full meeting management pipeline — agenda, notes, summary, action items

## Constraints
- Machine: Bally's issued only
- Account: Bally's Claude Co-work (not personal)
- Vault: work-only, no personal sync
- No audio recording/transcription built-in to Claude Code

## What Claude Co-work Can Do
- Read/write Obsidian markdown files
- Generate agendas from topics/attendees
- Structure raw notes into formatted meeting docs
- Extract action items + create task lists
- Summarize notes into executive briefs
- Search across past meetings

## What It Can't Do + Workarounds
- **No native audio recording** → Use macOS Dictation (Fn-Fn) or Zoom/Teams live transcript, paste into Obsidian, then process with Claude
- **No real-time transcription** → External tool or manual notes into scratch file

## Proposed Vault Structure
```
Ballys-Brain/
├── 1-Projects/
├── 2-Areas/
│   └── meetings/
│       ├── templates/
│       │   ├── agenda-template.md
│       │   ├── meeting-notes-template.md
│       │   └── action-items-tracker.md
│       ├── 2026-05/
│       │   └── YYYY-MM-DD-meeting-name.md
│       └── attendees/
│           └── team-roster.md
├── 3-Resources/
└── 4-Archives/
    └── meetings/
```

## Proposed Claude Custom Commands (`.claude/commands/`)

### `/meeting-agenda`
Generate agenda using `2-Areas/meetings/templates/agenda-template.md`.
Include attendees, topics with time blocks, prep materials, desired outcomes.
Save to `2-Areas/meetings/YYYY-MM-DD-<meeting-name>.md`

### `/meeting-process`
Read raw notes file. Structure using `meeting-notes-template.md`.
Extract all action items with owners + deadlines.
Append action items to `2-Areas/meetings/templates/action-items-tracker.md`

### `/meeting-summary`
Read specified meeting notes → produce 3-paragraph executive summary.
Highlight: decisions made, blockers, next steps.

## Example Workflow

### 1. Before Meeting
```bash
claude -p "Generate agenda for Engineering Sprint Review on May 5. Attendees: Arnold, Zed, team leads. Topics: Q2 deliverables, tech debt review, headcount planning." --allowedTools Read,Write
```

### 2. During Meeting
- Take raw notes in Obsidian (or macOS Dictation into scratch pad)
- Save as `2-Areas/meetings/2026-05/2026-05-05-sprint-review-raw.md`

### 3. After Meeting
```bash
claude -p "Process 2-Areas/meetings/2026-05/2026-05-05-sprint-review-raw.md using meeting-notes-template. Extract action items to action-items-tracker.md." --allowedTools Read,Write,Edit
```

## Audio/Transcription Options on Bally's Machine
- **macOS Dictation** (built-in, offline, Fn-Fn toggle) — dictate directly into Obsidian
- **Zoom/Teams live transcript** — copy-paste into Obsidian, then Claude structures it
- **Whisper CLI** (if Bally's allows install) — local transcription, then Claude processes

## Next Steps (when ready)
- [ ] Create template files (agenda, meeting notes, action items tracker)
- [ ] Build Claude custom commands as installable files
- [ ] Design weekly cronjob to nag about open action items
- [ ] Test end-to-end with one real meeting
