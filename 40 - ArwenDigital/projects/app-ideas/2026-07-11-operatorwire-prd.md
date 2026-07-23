---
tags: [app-idea, product-development, operatorwire, ai-agents, decision-intelligence]
created: 2026-07-11
updated: 2026-07-11
version: 1.3
status: approved-for-epics
project: OperatorWire
---

# OperatorWire — Product Requirements Document

## Document Information

| Field | Value |
|---|---|
| Product | OperatorWire |
| Version | 1.4 |
| Status | Product definition approved for epic and story decomposition |
| Author | Arnold Gamboa |
| Last updated | 2026-07-11 |
| Initial market | Automation consultants, AI implementation agencies, fractional operations specialists, and technically capable SMB operators serving businesses with 5–100 employees |
| Initial platform | Responsive web application, public website, email/Telegram briefings, and read-only API |
| Product stage | MVP followed by evidence-network expansion |

---

## 1. Executive Summary

OperatorWire is an evidence-backed decision system for people responsible for making AI tools and automations work in real businesses. It continuously monitors what changed, verifies what can be verified, and uses the operator’s workflow, budget, existing stack, risk tolerance, and technical capacity to recommend what to evaluate or use. Unlike directories that catalogue what exists or news aggregators that rank what is popular, OperatorWire answers a situational question: **“Given my requirements, which option is the best-supported fit, what are its limitations, and what should I do next?”**

The MVP will focus on **AI automation tools and developments for small-business operators**. It will collect information from official changelogs, product documentation, GitHub releases, status pages, pricing pages, selected publications, and structured submissions. The system will normalize and deduplicate those signals into intelligence records, identify material claims, attach supporting evidence, and publish concise reports answering:

1. What changed?
2. Why does it matter?
3. Who should care?
4. What evidence supports it?
5. What should the operator do next?

OperatorWire’s long-term defensibility will come from its **proof-of-use dataset**: structured field reports showing whether a tool completed a real task, its observed cost and latency, the conditions of the test, and whether results were independently reproduced.

---

## 2. Problem and Opportunity

### 2.1 Problem Statement

Operators face an overwhelming stream of AI product launches, directory listings, affiliate content, vendor announcements, and social posts. These sources make discovery easy but decision-making difficult. They rarely establish whether a product works as advertised, remains operational, represents a meaningful improvement, or suits a specific workflow.

The resulting problems include:

- Time wasted comparing near-identical products.
- Adoption of tools based on promotion rather than evidence.
- Missed pricing, API, policy, and reliability changes.
- Repeated evaluation work across teams and agents.
- Outdated recommendations persisting after products change or fail.
- Difficulty distinguishing vendor claims from independently verified facts.

### 2.2 Market Gap

Existing products generally serve one of four purposes:

| Category | What it does well | Unmet need |
|---|---|---|
| AI tool directories | Discovery and SEO coverage | Current reliability, evidence, context, and decision guidance |
| Technology news sites | Reporting announcements | Reproducible testing and workflow-specific relevance |
| Review sites | Human opinions and broad comparisons | Continuous monitoring and machine-readable evidence |
| Benchmark sites | Controlled model or API comparisons | Real operational workflows, changes over time, and personalized recommendations |

OperatorWire occupies the gap between discovery, monitoring, testing, and decision support.

### 2.3 Why Now

- AI tools and APIs change faster than conventional review cycles.
- Agents can continuously monitor sources and perform bounded verification tasks.
- Operators increasingly need recommendations tailored to workflows rather than generic categories.
- Machine-readable intelligence is becoming valuable to both humans and autonomous systems.
- Trust is becoming scarcer as directories and content sites rely on sponsorship, affiliate incentives, and vendor-submitted descriptions.

---

## 3. Product Vision and Positioning

### 3.1 Vision

Become the trusted evidence layer that humans and agents consult before selecting, changing, or recommending an operational tool.

### 3.2 Positioning

> OperatorWire is the intelligence feed ranked by what proved useful in real work.

### 3.3 Core Differentiator

> Directories answer, “What tools are available?” OperatorWire answers, “What should I use, under what conditions, and what evidence supports that decision?”

### 3.4 Product Principles

1. **Evidence over promotion:** Vendor claims are labeled and never treated as verified facts without supporting evidence.
2. **Utility over popularity:** Ranking favors operational usefulness, not clicks, follower counts, submission payments, or sponsorship.
3. **Primary sources first:** Every material claim links to its source and identifies the source type.
4. **Freshness is a feature:** Reports are re-evaluated when pricing, availability, documentation, or test results change.
5. **Specificity over hype:** Reports state the task, environment, constraints, and observed outcome.
6. **Transparent uncertainty:** Unknown, conflicting, and unverified claims are explicitly labeled.
7. **Human and machine readability:** Content must work as a concise web report and as structured API data.
8. **Commercial separation:** Revenue relationships cannot alter editorial scoring or evidence status.

---

## 4. Goals and Non-Goals

### 4.1 MVP Goals

- Aggregate high-signal changes from a curated set of at least 50 authoritative sources.
- Turn source items into deduplicated, structured intelligence records.
- Publish 5–10 useful reports per weekday for the initial audience.
- Clearly distinguish reported, corroborated, verified, field-tested, disputed, and outdated claims.
- Let users follow topics, tools, and workflows and receive a personalized briefing.
- Capture structured proof-of-use reports from trusted internal agents and approved contributors.
- Establish initial trust through transparent evidence and scoring explanations.
- Validate willingness to pay for personalized monitoring and decision support.

### 4.2 Business Goals

- Reach 1,000 registered users within six months of public launch.
- Convert at least 5% of active free users to a paid plan during initial pricing validation.
- Secure 10 design partners who provide workflows, feedback, or field-test evidence.
- Develop a structured evidence dataset that becomes more valuable as tests and history accumulate.

### 4.3 Non-Goals for MVP

- Becoming a comprehensive directory of every AI product.
- Covering general world news or every technology category.
- Building an open social network or discussion forum.
- Supporting anonymous public submissions without moderation.
- Selling ranking position or accepting undisclosed sponsored content.
- Running exhaustive scientific benchmarks across all models and tools.
- Automating procurement, purchasing, or vendor contracting.
- Building a native mobile application.
- Using blockchain, tokens, staking, or cryptocurrency for ranking.
- Providing legal, medical, financial, or security guarantees.

---

## 5. Target Market and Personas

### 5.1 Initial Market

The MVP targets **automation consultants, AI implementation agencies, fractional operations specialists, and technically capable small-business operators** who evaluate AI tools for businesses with approximately 5–100 employees. These users make repeated tool decisions, bear financial or reputational risk when recommendations fail, can supervise a pilot, and can contribute useful field evidence. General small-business owners remain an important later audience but are not the primary launch segment.

### 5.2 Primary Persona: Small-Business Operator

**Profile:** Owner, founder, or operations lead at a company with 1–50 employees.

**Goals:** Reduce operating cost, automate repetitive work, identify dependable tools, and avoid wasted subscriptions.

**Frustrations:** Too many directories, affiliate-heavy recommendations, unclear setup effort, and products that fail outside demonstrations.

**Technical proficiency:** Low to moderate.

### 5.3 Primary Persona: Automation Practitioner

**Profile:** Consultant, agency operator, no-code builder, AI engineer, or fractional operations specialist.

**Goals:** Select reliable components, monitor vendor changes, compare alternatives, and recommend tools confidently to clients.

**Frustrations:** API changes, inconsistent vendor documentation, hidden costs, and repeated testing across projects.

**Technical proficiency:** Moderate to high.

### 5.4 Secondary Persona: Engineering or Product Leader

**Profile:** Technical decision-maker at a startup or mid-sized organization.

**Goals:** Track relevant infrastructure changes, reduce evaluation effort, and maintain an approved technology stack.

**Frustrations:** Noise, security uncertainty, untraceable recommendations, and rapid platform changes.

### 5.5 Secondary Persona: Tool Vendor

**Profile:** Product, developer-relations, growth, or customer-success leader at an AI tool company.

**Goals:** Understand how the product performs in real workflows, identify failure patterns, and monitor competitive movement.

**Constraint:** Vendors may provide facts, access, and sponsored test requests but may not buy ranking improvements.

### 5.6 Machine Consumer

**Profile:** An AI assistant or autonomous agent selecting tools or preparing recommendations.

**Goals:** Query current, structured, evidence-backed information with source provenance and confidence metadata.

---

## 6. Core Use Cases

### UC-01: Discover actionable developments

A user opens a personalized feed and sees only changes relevant to their role, workflows, and monitored tools.

### UC-02: Decide whether to adopt a tool

A user views a tool profile containing current capabilities, pricing observations, verified tasks, failures, limitations, and alternatives.

### UC-03: React to a material change

A user receives an alert that a monitored product changed pricing, API behavior, availability, terms, or capabilities.

### UC-04: Compare tools for a job

A user selects a task, such as invoice extraction, and compares tools using task-specific evidence rather than generic feature lists.

### UC-05: Submit proof of use

A trusted agent or contributor submits a structured report describing a task, environment, outcome, cost, latency, and evidence.

### UC-06: Verify an announcement

An internal verifier converts a vendor announcement into a bounded verification task and publishes the result.

### UC-07: Query intelligence programmatically

An external agent requests the most suitable tools for a defined task and receives ranked results with evidence, timestamps, and confidence.

---

## 7. User Stories

- As a small-business operator, I want a short daily feed tailored to my workflows so that I can identify useful developments without reading dozens of sources.
- As an automation practitioner, I want to see whether a capability was independently tested so that I do not rely solely on vendor marketing.
- As an operator, I want every recommendation to explain why it applies to me so that I can make a quick decision.
- As an engineering leader, I want alerts when monitored APIs or prices change so that my team can respond before production or budget impact occurs.
- As a consultant, I want task-specific comparisons so that I can recommend tools to clients with supporting evidence.
- As a contributor, I want to submit a field report with evidence so that useful operational knowledge benefits others.
- As a reviewer, I want suspicious or conflicting claims routed to a moderation queue so that low-confidence information is not presented as fact.
- As a vendor, I want to correct factual metadata while preserving independent test conclusions so that the profile is accurate but credible.
- As an AI agent, I want a structured API response with provenance and freshness metadata so that I can safely use it in recommendations.
- As a user, I want to understand how an item’s score was calculated so that I can judge the ranking rather than blindly trust it.

---

## 8. Scope and Feature Priorities

### 8.1 MVP — Must Have

- Curated source registry
- Scheduled RSS/API/page/GitHub collection
- Raw snapshot storage and content hashing
- Entity resolution and deduplication
- Claim extraction and source attribution
- Intelligence-record editorial workflow
- Evidence-status model
- Manual review and publishing queue
- Public feed and report pages
- Tool/entity profile pages
- Topic, tool, and workflow follows
- Email and Telegram daily briefing
- Structured field-report submission for approved contributors
- Transparent utility score with component breakdown
- Search and filtering
- Basic free and Pro accounts
- Read-only public API with rate limits
- Analytics and data-quality monitoring

### 8.2 V1 — Should Have

- Automated change detection for pricing and documentation pages
- Repeatable test-runner framework
- Tool comparison pages by task
- Team workspaces and shared watchlists
- Slack delivery
- Vendor factual-correction workflow
- Saved searches and real-time alerts
- API keys and metered API plans
- Webhooks for intelligence updates
- Contributor reputation and verification history

### 8.3 Future — Could Have

- Private enterprise source monitoring
- Procurement and approved-stack integrations
- Browser extension
- Agent-to-agent field-report protocol
- Public benchmark packs
- Vendor analytics dashboard
- Marketplace or referral transactions
- Regional and industry-specific editions
- Community comments with evidence requirements

---

## 9. Information Aggregation Process

### 9.1 End-to-End Pipeline

```text
Source Registry
   ↓
Scheduled Collection
   ↓
Raw Snapshot + Metadata
   ↓
Parsing and Normalization
   ↓
Entity Resolution + Deduplication
   ↓
Claim and Change Extraction
   ↓
Relevance and Risk Triage
   ↓
Verification Task or Editorial Review
   ↓
Evidence Attachment + Utility Scoring
   ↓
Publication
   ↓
Field Reports + Ongoing Monitoring
   ↓
Record Revision, Dispute, or Expiration
```

### 9.2 Source Tiers

| Tier | Examples | Default trust treatment |
|---|---|---|
| Tier 1: Primary | Official docs, changelogs, repositories, status and pricing pages | Authoritative for what the vendor claims or publishes, not proof of performance |
| Tier 2: Independent authoritative | Established reporting, research papers, security advisories | Strong corroboration, subject to scope and freshness |
| Tier 3: Practitioner evidence | Reproducible field reports, public workflow logs, technical write-ups | Useful when methodology and identity are clear |
| Tier 4: Discovery sources | Directories, social posts, forums, newsletters | Leads only; material claims require better sources |
| Tier 5: Commercial submissions | Vendor submissions, press releases, sponsored-test requests | Explicitly labeled and independently evaluated |

### 9.3 Content Lifecycle

1. **Discovered:** Raw source item collected.
2. **Parsed:** Relevant text and metadata extracted.
3. **Grouped:** Linked to an entity and related event cluster.
4. **Triaged:** Assigned relevance, novelty, risk, and testability scores.
5. **Reviewed:** Claims and source attribution checked.
6. **Verified:** Automated or human test executed where feasible.
7. **Published:** Intelligence record made visible.
8. **Updated:** New evidence or changes appended.
9. **Disputed:** Conflicting evidence visibly recorded.
10. **Outdated/Archived:** Freshness threshold exceeded or facts superseded.

### 9.4 Editorial Record Template

Every published report must answer:

- **Headline:** Specific description of the material development.
- **What changed:** Factual summary.
- **Why it matters:** Operational consequence.
- **Who should care:** Relevant roles, workflows, and industries.
- **What we verified:** Tests or corroboration actually completed.
- **What remains unknown:** Unverified or uncertain claims.
- **Recommended action:** Ignore, monitor, investigate, test, migrate, or adopt.
- **Evidence:** Source links, timestamps, artifacts, and status.
- **Commercial disclosure:** Sponsorship, affiliate, vendor access, or none.

---

## 10. Evidence and Trust Model

### 10.1 Evidence Statuses

| Status | Definition |
|---|---|
| Reported | A source made the claim; OperatorWire has not independently confirmed it |
| Corroborated | At least two sufficiently independent credible sources support the claim |
| Verified | OperatorWire reproduced or directly inspected the material claim |
| Field-tested | The tool or insight succeeded in a real or representative workflow with documented conditions |
| Disputed | Credible evidence conflicts with the claim or with another result |
| Failed verification | A bounded attempt did not reproduce the claimed result |
| Outdated | Evidence no longer reflects the current product or environment |

### 10.2 Proof-of-Use Requirements

A field report must include:

- Tool and version, when available
- Task definition
- Test date and region
- Environment or relevant configuration
- Input class without exposing sensitive payloads
- Outcome: success, partial success, failure, or inconclusive
- Observable measures such as latency, cost, accuracy proxy, and corrections
- Evidence reference or cryptographic hash
- Contributor identity and trust level
- Disclosure of vendor, affiliate, or employment relationship

### 10.3 Independence Rules

Two reports count as independently corroborating only if they do not share the same operator, execution, evidence artifact, or vendor-controlled source. The system must prevent one organization from appearing as multiple independent confirmations.

### 10.4 Freshness Rules

- News and announcements: freshness review after 30 days.
- Pricing and terms: recheck at least weekly for monitored entities.
- API availability and latency: display exact test time; no evergreen reliability claim from a single test.
- Field reports: flag for revalidation after 90 days or a material product version change.
- Security-sensitive reports: use a separate disclosure and review process.

---

## 11. Ranking Model

### 11.1 Initial Utility Score

The published score ranges from 0–100:

| Component | Weight | Description |
|---|---:|---|
| User relevance | 25 | Match to the user’s role, workflows, followed entities, and constraints |
| Evidence quality | 20 | Strength, provenance, reproducibility, and independence of evidence |
| Practical utility | 20 | Expected time, cost, quality, or risk impact |
| Verification confidence | 15 | Corroboration and successful tests |
| Recency | 10 | Time since event and most recent verification |
| Source credibility | 10 | Historical source quality and directness |

Penalties are applied for:

- Duplicated or recycled information
- Undisclosed commercial relationship
- Contradictory evidence
- Failed verification
- Stale tests
- Misleading headline or unsupported claim scope
- Suspected coordinated submissions

### 11.2 Ranking Requirements

- Scores MUST expose a user-readable explanation.
- Sponsorship MUST NOT add ranking points.
- Affiliate relationships MUST NOT affect scoring.
- Personalization MUST not overwrite the global evidence score; relevance and evidence must remain distinguishable.
- Ranking-model versions MUST be stored on each score calculation.
- Material score changes MUST be auditable.
- Editors MAY override ranking only with a recorded reason, author, and timestamp.

---

## 12. Functional Requirements

### 12.1 Source Registry and Collection

- **FR-001 [MUST]** Authorized editors can create, update, pause, and remove sources.
- **FR-002 [MUST]** Each source stores name, URL, source type, tier, owner entity, polling frequency, parser type, terms notes, and status.
- **FR-003 [MUST]** The system collects RSS/Atom feeds, JSON APIs, public HTML pages, and GitHub releases.
- **FR-004 [MUST]** Each collection stores retrieval time, HTTP status, canonical URL, response hash, and raw or permitted extracted content.
- **FR-005 [MUST]** Collection retries transient failures with bounded exponential backoff.
- **FR-006 [MUST]** Repeated failures generate an operational alert and degrade the source’s health status.
- **FR-007 [MUST]** The collector respects robots directives, rate limits, and configured licensing restrictions.
- **FR-008 [SHOULD]** Sources support conditional requests using ETag and Last-Modified.
- **FR-009 [SHOULD]** Pricing and documentation pages support visual or structural change detection.
- **FR-010 [MAY]** Authorized users can submit a source for editorial approval.

### 12.2 Parsing, Entity Resolution, and Deduplication

- **FR-011 [MUST]** The system normalizes titles, timestamps, URLs, source identity, entities, and event types.
- **FR-012 [MUST]** The system associates each item with zero or more entities and workflows.
- **FR-013 [MUST]** Exact URL, canonical URL, and content-hash duplicates are automatically grouped.
- **FR-014 [MUST]** Semantic near-duplicates are suggested for editorial confirmation.
- **FR-015 [MUST]** Editors can merge and unmerge clusters without deleting source history.
- **FR-016 [MUST]** A single intelligence record can contain multiple sources and evolving evidence.
- **FR-017 [SHOULD]** Entity aliases, domains, products, parent companies, and renamed products are resolved.
- **FR-018 [SHOULD]** The system detects when an old announcement is republished without a material change.

### 12.3 Claim Extraction and Triage

- **FR-019 [MUST]** The system extracts material claims with exact source attribution.
- **FR-020 [MUST]** Extracted claims are drafts until reviewed or supported by deterministic extraction.
- **FR-021 [MUST]** Each claim receives novelty, relevance, impact, risk, and testability values.
- **FR-022 [MUST]** High-risk claims involving security, legal allegations, financial harm, or personal reputation require human review before publication.
- **FR-023 [MUST]** The system distinguishes vendor claims from OperatorWire conclusions.
- **FR-024 [SHOULD]** Low-value promotional items are suppressible with a recorded reason.
- **FR-025 [SHOULD]** Editors can create a verification task directly from a claim.

### 12.4 Verification and Field Reports

- **FR-026 [MUST]** Approved contributors can submit structured field reports.
- **FR-027 [MUST]** Required report fields are validated before submission.
- **FR-028 [MUST]** Evidence artifacts can be private, public, or represented by a hash and metadata.
- **FR-029 [MUST]** The system records contributor identity, disclosures, and organization relationships.
- **FR-030 [MUST]** Reviewers can approve, reject, request revision, or mark a report inconclusive.
- **FR-031 [MUST]** Failed tests remain visible where relevant and are not silently discarded.
- **FR-032 [MUST]** Verification attempts store methodology, environment, date, tool version, and result.
- **FR-033 [SHOULD]** Repeatable tests can execute in isolated workers with secrets scoped per test.
- **FR-034 [SHOULD]** Multiple test results can be aggregated without hiding variance.
- **FR-035 [MAY]** Contributors can cryptographically sign reports.

### 12.5 Editorial Workflow

- **FR-036 [MUST]** Editors have queues for new, high-impact, conflicting, stale, and sponsored items.
- **FR-037 [MUST]** Intelligence records support draft, review, scheduled, published, disputed, outdated, and archived states.
- **FR-038 [MUST]** All editorial changes retain revision history.
- **FR-039 [MUST]** Published corrections display what changed and when.
- **FR-040 [MUST]** Sponsored tests and commercial relationships are prominently disclosed.
- **FR-041 [MUST]** An editor can schedule publication or suppress distribution while preserving the record.
- **FR-042 [SHOULD]** AI-generated summaries show source coverage and unsupported-sentence warnings to reviewers.

### 12.6 Public Feed and Intelligence Reports

- **FR-043 [MUST]** Visitors can browse published intelligence without an account.
- **FR-044 [MUST]** Every report displays evidence status, last verified date, sources, relevant personas, recommended action, and disclosures.
- **FR-045 [MUST]** Reports distinguish source facts, OperatorWire analysis, and field-test observations.
- **FR-046 [MUST]** Users can filter by topic, workflow, entity, evidence status, and date.
- **FR-047 [MUST]** Users can sort by relevance, recency, and evidence strength.
- **FR-048 [MUST]** Outdated or disputed records display a prominent status banner.
- **FR-049 [SHOULD]** Reports expose a machine-readable JSON representation.
- **FR-050 [SHOULD]** Users can share stable report URLs with meaningful social previews.

### 12.7 Entity and Tool Profiles

- **FR-051 [MUST]** Each entity profile displays current description, official links, monitored sources, recent changes, evidence history, and field reports.
- **FR-052 [MUST]** Vendor-provided metadata is visibly distinguishable from independent content.
- **FR-053 [MUST]** Profiles display the date each material fact was last checked.
- **FR-054 [SHOULD]** Profiles show known alternatives and task-specific comparisons.
- **FR-055 [SHOULD]** Authorized vendor representatives can propose factual corrections.
- **FR-056 [MUST]** Vendor corrections cannot modify independent conclusions or delete unfavorable evidence.

### 12.8 Accounts, Personalization, and Alerts

- **FR-057 [MUST]** Users can register, sign in, sign out, maintain a secure session, and recover access through Convex Auth.
- **FR-058 [MUST]** Users can select roles, interests, workflows, constraints, and tools they use.
- **FR-059 [MUST]** Users can follow or unfollow topics, entities, and workflows.
- **FR-060 [MUST]** The personalized feed combines relevance with global evidence quality.
- **FR-061 [MUST]** Users can configure daily or weekly email briefings.
- **FR-062 [MUST]** Users can connect Telegram and choose delivery frequency.
- **FR-063 [MUST]** Every notification includes a working unsubscribe or preference-control path.
- **FR-064 [SHOULD]** Pro users can configure immediate alerts for material changes.
- **FR-065 [SHOULD]** Users can save reports and add private notes.

### 12.9 Search and Comparisons

- **FR-066 [MUST]** Search covers entities, reports, claims, workflows, and tags.
- **FR-067 [MUST]** Search results display evidence status and freshness.
- **FR-068 [SHOULD]** Natural-language queries can map to structured filters.
- **FR-069 [SHOULD]** V1 users can compare tools against a defined task and constraints.
- **FR-070 [SHOULD]** Comparisons cite the exact reports and tests supporting each conclusion.
- **FR-071 [MUST]** The system must not claim a definitive winner when evidence is insufficient.

### 12.10 API

- **FR-072 [MUST]** The read API exposes published reports, entities, sources, evidence statuses, and freshness metadata.
- **FR-073 [MUST]** API responses use stable identifiers, pagination, documented schemas, and ISO 8601 timestamps.
- **FR-074 [MUST]** Public access is rate limited.
- **FR-075 [MUST]** API data includes canonical web URLs and source provenance.
- **FR-076 [MUST]** Breaking schema changes require a versioned endpoint.
- **FR-077 [SHOULD]** Paid API plans support API keys, higher limits, and usage reporting.
- **FR-078 [SHOULD]** Webhooks can notify subscribers of new or materially updated records.

### 12.11 Administration and Moderation

- **FR-079 [MUST]** Role-based access supports administrator, editor, reviewer, contributor, vendor representative, and user.
- **FR-080 [MUST]** Administrative actions are audit logged.
- **FR-081 [MUST]** Reviewers can suspend contributors and quarantine questionable evidence.
- **FR-082 [MUST]** Users can report factual errors, conflicts, undisclosed relationships, and unsafe content.
- **FR-083 [MUST]** Data exports and deletion requests are supported for user-owned personal data.
- **FR-084 [SHOULD]** Moderators receive coordinated-submission and unusual-voting alerts if community features are introduced.

### 12.12 Monetization

- **FR-085 [MUST]** The system supports Free and Pro entitlements without changing editorial rankings.
- **FR-086 [MUST]** Sponsored evaluations are labeled before, during, and after publication.
- **FR-087 [MUST]** Affiliate links are disclosed and added only after editorial scoring.
- **FR-088 [MUST]** Payment status cannot modify evidence status or utility score.
- **FR-089 [SHOULD]** Team plans support shared watchlists and member management.
- **FR-090 [SHOULD]** Vendor analytics use aggregated data and do not expose private user behavior without consent.

---

## 13. Key User Flows

### 13.1 New User Onboarding

1. User arrives from a report, search result, or invitation.
2. User can read public content before registration.
3. User creates an account to personalize the feed.
4. User selects one or more roles.
5. User selects workflows, topics, and existing tools.
6. System previews a personalized feed and explains why each item appears.
7. User chooses email or Telegram briefing frequency.
8. System records preferences and delivers the first briefing at the selected time.

**Success condition:** User follows at least five entities/topics/workflows or enables a briefing.

### 13.2 Intelligence Publication Flow

1. Collector creates a raw source item.
2. Parser extracts metadata and candidate claims.
3. System associates the item with an entity and event cluster.
4. Triage determines relevance, novelty, impact, and verification needs.
5. Editor reviews source context and claim wording.
6. If testable, a verifier performs or schedules a bounded test.
7. Evidence and uncertainty are attached.
8. Utility score is calculated.
9. Editor previews and publishes the intelligence record.
10. Distribution service sends it to eligible feeds and briefings.

### 13.3 Tool Decision Flow

1. User chooses a supported workflow and states the decision to make.
2. System runs a workflow-specific diagnostic using conditional questions.
3. System presents a normalized Decision Profile for correction and confirmation.
4. System evaluates candidates against mandatory requirements before ranking.
5. Ineligible and unknown candidates are identified with requirement-level reasons.
6. Eligible candidates receive separate Fit and Confidence assessments.
7. System generates a versioned Decision Brief with recommendation, alternatives, evidence, limitations, and pilot plan.
8. User can inspect evidence, adjust a requirement, save the brief, or start the proposed pilot.
9. User later records whether the option was shortlisted, piloted, adopted, rejected, or abandoned.
10. Private outcome data remains private unless the user consents to submit it as a reviewed Field Report.

### 13.4 Field Report Flow

1. Approved contributor selects an entity and task.
2. Contributor enters environment, methodology, outcome, and metrics.
3. Contributor uploads evidence or submits artifact hashes.
4. Contributor declares relationships and commercial incentives.
5. System validates completeness and checks for duplicates.
6. Reviewer evaluates methodology and evidence.
7. Reviewer approves, requests revision, rejects, or marks inconclusive.
8. Approved result updates relevant records and scores.

### 13.5 Disputed Claim Flow

1. New evidence conflicts with a published claim.
2. System or reviewer marks the record disputed.
3. A visible banner appears immediately when impact is material.
4. Normal promotional distribution is paused.
5. Reviewer investigates source independence and methodology.
6. Record is corrected, narrowed, retained as disputed, or marked outdated.
7. Subscribed users receive a correction if the original item triggered an alert.

---

## 14. UX and Design Requirements

### 14.1 Experience Principles

- **Decision-first:** Lead with implications and recommended action, not a long summary.
- **Evidence visible:** Status, freshness, and sources must be understandable without expanding hidden sections.
- **Progressive detail:** Operators get a concise answer; technical users can inspect methodology and artifacts.
- **No artificial urgency:** Alerts should reflect material impact, not engagement optimization.
- **Honest empty states:** Insufficient evidence must look different from a negative evaluation.

### 14.2 Primary Navigation

- Feed
- Discover
- Workflows
- Tools
- Saved
- Alerts
- About the methodology

Administrative navigation is separate and role restricted.

### 14.3 Report Card Structure

Each feed card should show:

- Specific headline
- One-sentence significance
- Evidence badge
- Last verified timestamp
- Relevant role/workflow labels
- Recommended action
- Utility-score explanation trigger
- Primary source count

### 14.4 Key UI States

- **Loading:** Skeletons with no fabricated content or score.
- **Empty personalized feed:** Suggest topics and show high-quality global reports.
- **No evidence:** “Reported; not independently verified” with a clear explanation.
- **Stale:** Warning with last verification date and option to request a recheck.
- **Disputed:** Prominent conflict summary and links to both sides.
- **Collection error:** Preserve last known content but label freshness risk.
- **Success:** Confirm saved preferences, follows, submissions, and alert creation.

### 14.5 Accessibility

- Conform to WCAG 2.2 AA for public and authenticated interfaces.
- All status badges include text, not color alone.
- Full keyboard navigation and visible focus states.
- Semantic heading hierarchy and table markup.
- Screen-reader labels for score explanations and evidence timelines.
- Respect reduced-motion preferences.

---

## 15. Data Model

### 15.1 Core Entities

| Entity | Purpose | Key fields |
|---|---|---|
| Source | Defines where information is collected | id, name, URL, type, tier, owner entity, cadence, status |
| SourceSnapshot | Immutable retrieval evidence | id, source_id, retrieved_at, status, hash, content location, headers |
| SourceItem | Parsed unit from a snapshot | id, source_snapshot_id, canonical_url, title, author, published_at |
| Organization | Company, publisher, or contributor organization | id, name, domain, relationships |
| Entity | Product, API, model, company, or project | id, type, name, aliases, official URLs |
| EventCluster | Groups source items about the same development | id, event_type, occurred_at, entity links |
| Claim | Atomic attributable assertion | id, text, source_item_id, status, scope, risk level |
| IntelligenceRecord | Published decision-oriented report | id, slug, headline, summary, impact, action, status, revision |
| Evidence | Supports or challenges a claim | id, type, provenance, artifact reference, visibility, created_at |
| VerificationRun | Bounded test execution | id, methodology, environment, started_at, result, metrics |
| FieldReport | Structured proof of use | id, contributor, entity, task, outcome, disclosures, reviewed state |
| Workflow | Operational job to be done | id, name, description, required capabilities |
| Score | Versioned utility calculation | id, record_id, model_version, components, total, calculated_at |
| User | Account and identity | id, email, role, status, locale |
| Preference | Personalization settings | user_id, topics, workflows, entities, constraints |
| Subscription | Delivery configuration | user_id, channel, cadence, filters, status |
| Disclosure | Commercial or organizational relationship | actor, entity, type, effective dates |
| AuditEvent | Immutable administrative history | actor, action, target, timestamp, metadata |

### 15.2 Relationship Notes

- A source can produce many snapshots and source items.
- An event cluster can involve multiple entities and source items.
- A claim must have at least one source item.
- An intelligence record can summarize many claims and evidence items.
- Evidence may support, contradict, or qualify one or more claims.
- Scores are immutable calculations; a new calculation creates a new score version.
- Field reports can create evidence and trigger record updates.

### 15.3 Data Retention

- Published records and revision histories are retained indefinitely unless legally removed.
- Raw snapshots follow source-specific legal and licensing rules.
- Sensitive test payloads must not be retained by default.
- Account deletion removes or anonymizes personal data while preserving legitimate public evidence with attribution rules communicated in advance.
- Logs containing secrets or payloads must be redacted and retained for the minimum operational period.

---

## 16. Technical Architecture

### 16.1 Proposed Components

1. **Astro web application:** Responsive public website, authenticated advisor experience, editorial console, and server-rendered/interactive pages where appropriate.
2. **Convex backend and Convex Auth:** Canonical application database, user authentication, sessions, identity linkage, reactive queries, mutations, actions, scheduled functions, file metadata, audit records, and application APIs.
3. **Convex ingestion orchestration:** Scheduled collection, source-health tracking, retries, content normalization, deduplication, and job state. Lightweight deterministic work runs in Convex functions/actions.
4. **Hermes agent workflows, when needed:** Claim extraction, evidence synthesis, relevance triage, Decision Brief drafting, and other bounded reasoning tasks that materially benefit from an agent. Hermes is invoked from controlled backend jobs and is not the source of truth.
5. **Verification runner:** Isolated deterministic tests for APIs, integrations, synthetic customer-support scenarios, cost, latency, and reliability. Verification may be triggered by Convex and may use Hermes only for explicitly approved semantic evaluation.
6. **Editorial and review console:** Astro interface backed by Convex for queues, evidence inspection, corrections, revision history, Workflow Packs, and publication.
7. **Search:** Convex search capabilities for initial keyword and structured retrieval; semantic/vector retrieval is introduced only if validated as necessary.
8. **Notification delivery:** Convex scheduled functions and actions coordinate email, Telegram, and later Slack/webhooks.
9. **Artifact and image storage:** **Cloudflare R2** stores product images, report images, screenshots, test artifacts, and larger permitted source snapshots. Convex stores object keys, URLs, hashes, provenance, visibility, and retention metadata. Small application-native files may use Convex storage only when operationally simpler.
10. **Observability:** Convex logs and metrics plus application/error monitoring for Astro, Hermes jobs, verification runners, collection health, and data quality.
11. **Decision Engine:** Versioned Workflow Pack execution, requirement evaluation, candidate eligibility, Fit and Confidence calculation, and Decision Brief generation, with deterministic rules stored and executed through Convex.

### 16.2 Approved MVP Stack

| Layer | Approved technology | Responsibility |
|---|---|---|
| Frontend and web delivery | **Astro** | Public feed, tool profiles, onboarding, Decision Profiles, Decision Briefs, editorial console, and SEO pages |
| Backend, data, and authentication | **Convex + Convex Auth** | Data model, user authentication and sessions, reactive queries, mutations/actions, scheduled jobs, APIs, workflow state, audit history, and initial search |
| Agent/reasoning layer | **Hermes, only when an agent is needed** | Bounded extraction, synthesis, triage, semantic evaluation, and drafting tasks |
| Deterministic verification | Isolated TypeScript or Python runners | Repeatable API/integration tests, synthetic test packs, latency, cost, and reliability measurements |
| Images and evidence artifacts | **Cloudflare R2** | Product/report images, screenshots, test artifacts, permitted snapshots, and public/private asset delivery; Convex stores metadata and object references |
| Deployment | Astro and verification/Hermes services on Dokploy where appropriate; Convex as the managed backend | Runtime hosting and operations |
| Delivery integrations | Transactional email provider and Telegram Bot API | Briefings and alerts |

### 16.3 Architecture Boundaries

- Convex is the canonical source of truth for entities, evidence metadata, Workflow Packs, Decision Profiles, assessments, briefs, outcomes, entitlements, and audit history.
- Convex Auth is the sole MVP user-authentication layer. Authorization remains enforced server-side in Convex using the authenticated identity and application roles.
- Astro must access product data through defined Convex queries, mutations, and actions rather than maintaining a second application database.
- Hermes is optional and task-specific. Deterministic collection, requirement gating, scoring, permissions, billing entitlements, and audit logic must not depend on agent judgment.
- Hermes output is always treated as a draft or derived result. It must include provenance and cannot directly mark a claim Verified, alter evidence, publish a high-impact record, or bypass editorial rules.
- Long-running or environment-sensitive verification executes outside Convex in isolated runners; Convex stores job state and results.
- Workflow Pack rules, scoring versions, prompts, models, and agent-run metadata must be versioned for reproducibility.
- A separate Redis queue, PostgreSQL database, or vector database is not part of the MVP unless load testing demonstrates a concrete Convex limitation.

### 16.4 AI and Hermes Usage Guardrails

- Hermes may draft summaries, extract candidate claims, classify relevance, suggest entity matches, synthesize evidence, and draft Decision Brief language.
- Hermes or any LLM output is not itself evidence.
- Every factual sentence in a published record or brief must map to a source, evidence item, capability fact, or explicitly labeled analysis.
- High-impact, disputed, sponsored, or low-confidence content requires human review.
- Model/provider, prompt or skill version, input evidence IDs, output, run status, cost where available, and timestamp must be recorded.
- Source text is untrusted data and must not be able to invoke tools, change policy, expose secrets, or instruct Hermes outside the bounded task.
- Agent failures must degrade gracefully to deterministic processing or human review rather than block the entire ingestion pipeline.

---

## 17. Integrations

### MVP Integrations

- RSS/Atom
- GitHub releases and repository metadata
- Public web pages and JSON APIs
- Email delivery
- Telegram Bot API
- Convex Auth for user authentication, sessions, and identity linkage
- Billing provider for Pro subscriptions
- Analytics and error monitoring

### Later Integrations

- Slack
- Browser extension
- Zapier/Make/n8n webhooks
- Procurement and internal-tool catalogs
- Vendor status services
- Agent protocols and MCP endpoints

---

## 18. Non-Functional Requirements

### 18.1 Performance

- Public pages SHOULD achieve LCP under 2.5 seconds at the 75th percentile on mobile.
- Cached feed API responses MUST return within 500 ms at P95 under expected MVP load.
- Search MUST return within 1 second at P95 for the initial dataset.
- The editorial queue SHOULD load within 2 seconds for up to 10,000 pending items.
- Briefing generation MUST complete before the configured delivery window.

### 18.2 Reliability

- Public read services target 99.9% monthly availability after public launch.
- Collector failure for one source MUST not block other sources.
- Failed jobs MUST be retryable and observable.
- Last-known published data remains readable during ingestion outages, with freshness labels.
- Database backups MUST run daily with point-in-time recovery where supported.
- Restore procedures MUST be tested quarterly after launch.

### 18.3 Security

- Encryption in transit is required for all services.
- Secrets must be stored in a secret manager or encrypted deployment environment, never source code.
- Verification workers must run isolated from the core application and use least-privilege credentials.
- Uploaded artifacts must be scanned, size limited, and non-executable by default.
- Administrative accounts require multi-factor authentication.
- Role-based access is enforced server-side.
- Rate limiting and abuse controls apply to authentication, submissions, search, and API access.
- Audit logs must be append-only for privileged actions.
- Prompt-injection content from sources must not be allowed to invoke tools or modify system policy.

### 18.4 Privacy

- Collect only personalization data needed to provide feeds and alerts.
- Do not publish private workflow payloads or customer data.
- Field-report contributors choose public identity, organization identity, or approved pseudonym according to trust policy.
- Users can export and delete account data.
- Vendor analytics are aggregated and privacy preserving.

### 18.5 Scalability Assumptions

MVP design target:

- 100 sources initially; 1,000 without architectural replacement
- 100,000 source items
- 10,000 published intelligence records
- 10,000 registered users
- 100 requests per second burst on public read endpoints
- 100,000 briefing deliveries per month

### 18.6 Observability

Dashboards and alerts must cover:

- Collection success and latency by source
- Parsing and extraction failure rates
- Queue depth and age
- Duplicate rate
- Time from discovery to publication
- Stale-record counts
- API latency and errors
- Briefing delivery success
- Verification worker failures
- LLM cost and unsupported-claim detection

---

## 19. Content, Legal, and Ethical Requirements

- Store and display only content permitted by source terms and applicable law.
- Prefer summaries, metadata, and links over republishing full copyrighted articles.
- Maintain a takedown and correction process.
- Security vulnerability handling must follow responsible-disclosure practices.
- Reports affecting reputation require higher editorial review.
- Do not present a single synthetic test as universal product quality.
- Sponsored evaluations must guarantee methodological independence, not a favorable outcome.
- Affiliate relationships must be disclosed and separated from ranking logic.
- Vendors may respond to reports, but responses do not erase independent evidence.

---

## 20. Monetization and Entitlements

### 20.1 Free

- Public global feed
- Public reports and entity profiles
- Limited personalization
- Daily or weekly basic briefing
- Rate-limited public API
- One complete Decision Profile and Decision Brief
- One refresh within 30 days
- Evidence citations and basic alternatives
- No scenario modeling or continuous decision monitoring

### 20.2 Pro — Proposed $19–29/month

- Full personalized feed
- Immediate material-change alerts
- Unlimited follows and saved reports
- Advanced filtering
- Detailed comparisons
- Extended evidence and test history
- Higher API allowance
- Three new Decision Profiles per month
- Unlimited edits before a profile is finalized
- Reasonable brief refreshes when evidence changes
- Scenario comparison and detailed exclusion reasons
- Pilot plans and decision-outcome tracking

A Decision Profile consumes allowance only when a final brief is generated. Private beta uses concierge access without strict automated quotas so actual cost per brief can be measured before pricing is finalized.

### 20.3 Team — Proposed starting at $149/month

- Up to 20 new Decision Profiles per month
- Shared watchlists
- Workspace members and roles
- Shared notes
- Slack delivery
- Approved-tool lists
- Team briefing
- Usage and administrative controls
- Shared decision history and workspace/client separation

### 20.4 Vendor Intelligence — Later

- Aggregated performance trends
- Competitive change monitoring
- Integration-failure themes
- Sponsored independent evaluations

### 20.5 Commercial Integrity Rules

- No paid ranking placement.
- No hidden sponsored articles.
- No removal of valid unfavorable evidence in exchange for payment.
- Sponsored testing is disclosed and follows the same methodology as independent testing.
- Affiliate compensation is calculated after ranking and cannot alter it.

---

## 21. Success Metrics

### 21.1 North Star Metric

**Weekly Evidence-Assisted Decisions (WEAD):** Number of weekly active users who view evidence and then perform a meaningful decision action, such as saving a report, following a tool, comparing alternatives, requesting a test, or marking the report useful.

This metric measures decision support rather than raw traffic.

### 21.2 MVP Product KPIs

| Metric | Six-month target |
|---|---:|
| Registered users | 1,000 |
| Weekly active users | 400 |
| Weekly evidence-assisted decisions | 250 |
| Briefing open/read rate | ≥40% |
| Users returning within four weeks | ≥35% |
| Reports with primary-source attribution | 100% |
| Reports with explicit evidence status | 100% |
| Material corrections caused by editorial error | <2% of reports |
| Median discovery-to-publication time for material items | <24 hours |
| Published records reviewed before freshness deadline | ≥95% |
| Paid conversion among eligible active users | ≥5% |

### 21.3 Data Quality Metrics

- Duplicate publication rate under 2%.
- Unsupported factual sentence rate under 1% in audited reports.
- Source collection success above 98% for healthy sources.
- Entity-resolution precision above 95% on reviewed samples.
- At least 30% of high-priority reports contain independent corroboration or verification by month six.
- At least 100 approved field reports by month six.

### 21.4 Business Metrics

- Monthly recurring revenue
- Free-to-paid conversion
- Pro and Team retention
- Customer acquisition cost by channel
- Revenue concentration
- API usage and expansion
- Number of active design partners

### 21.5 Analytics Events

- `report_viewed`
- `evidence_expanded`
- `source_opened`
- `score_explained`
- `report_saved`
- `entity_followed`
- `workflow_followed`
- `alert_created`
- `comparison_started`
- `comparison_completed`
- `field_report_started`
- `field_report_submitted`
- `field_report_approved`
- `correction_viewed`
- `vendor_site_opened`
- `subscription_started`
- `subscription_cancelled`

Analytics must not influence editorial ranking.

---

## 22. Launch Plan and Phasing

### Phase 0 — Discovery and Validation (2 weeks)

**Objectives:** Confirm the initial audience, source set, report format, and willingness to pay.

- Interview 10–15 small-business operators and automation practitioners.
- Collect recent tool decisions and identify information they lacked.
- Produce 10 manual OperatorWire reports.
- Test report usefulness and evidence-status comprehension.
- Recruit 5–10 design partners.
- Finalize the first 50 sources and 10 workflows.

**Exit criteria:** At least 70% of interviewees say the report would materially improve or accelerate a recent decision; at least five agree to receive a recurring briefing.

### Phase 1 — Internal Alpha (4–6 weeks)

- Source registry and scheduled collection
- Snapshot storage
- Parsing and deduplication
- Basic entity model
- Claim extraction
- Editorial queue
- Public report templates behind access control
- Manual evidence statuses and scoring
- Email/Telegram test briefings

**Exit criteria:** System reliably collects 50 sources, produces a daily internal briefing, and supports 20 high-quality reviewed reports without data-loss or attribution defects.

### Phase 2 — Private Beta (4 weeks)

- User accounts and onboarding
- Personalized feed
- Follows and saved reports
- Public entity profiles
- Field-report submission for approved contributors
- Search and filters
- Free public API preview
- Billing sandbox and Pro entitlement tests

**Exit criteria:** 50 invited users, 30% four-week retention, 40% briefing read rate, and at least 20 evidence-assisted decisions per week.

### Phase 3 — Public MVP (4 weeks)

- Public website and indexing
- Production billing
- Pro plan
- Transparent methodology and commercial policy
- Correction and dispute process
- Operational dashboards and incident runbooks
- Initial launch content and partner distribution

**Exit criteria:** 250 registered users, first 25 paying users, and no unresolved critical trust or security issues.

### Phase 4 — V1 Expansion

- Automated price/documentation change detection
- Repeatable verification runner
- Task-specific comparison pages
- Team workspaces
- Slack and webhooks
- Paid API plans
- Contributor reputation

---

## 23. Acceptance Criteria for MVP Launch

The MVP is launch-ready only when:

- At least 50 sources are active and monitored.
- Collection health has remained above 95% for 14 consecutive days.
- At least 100 reviewed intelligence records exist.
- Every published record has source attribution, evidence status, last-checked date, and commercial disclosure.
- Users can onboard, personalize, follow, save, and receive a briefing.
- Email and Telegram deliveries have unsubscribe/preferences controls.
- Editors can correct or dispute a report with visible history.
- Search and core public pages meet accessibility checks.
- Public API documentation and rate limits are live.
- Backups and a restore test have completed successfully.
- Administrative access and verification-worker isolation have passed security review.
- Billing does not affect score calculations.
- Methodology, correction, privacy, sponsorship, and affiliate policies are public.

---

## 24. Risks and Mitigations

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Product becomes another low-value aggregator | Medium | High | Narrow initial scope; require decision-oriented reports and evidence status |
| Insufficient field reports create a cold-start problem | High | High | Begin with internal tests and design partners; do not overclaim proof-of-use coverage |
| Automated summaries introduce unsupported claims | Medium | High | Claim-to-source mapping, review queues, automated support checks, visible corrections |
| Vendors attempt to manipulate rankings | High | High | Independence graph, disclosures, audit trails, anomaly detection, no paid placement |
| Scraping violates source terms or becomes unstable | Medium | High | Prefer feeds/APIs, store permitted extracts, source-specific policies, conditional requests |
| Verification costs become excessive | Medium | Medium | Triage by impact and testability; reusable test packs; budget limits |
| Tests expose secrets or sensitive data | Medium | High | Isolated workers, scoped credentials, redaction, no private payload retention |
| Rankings imply false precision | High | Medium | Show component explanations, confidence, uncertainty, and evidence rather than score alone |
| Personalization creates a narrow bubble | Medium | Medium | Separate global evidence from relevance and provide a high-impact global view |
| Sponsored work undermines trust | Medium | High | Prominent disclosures and independent methodology; sponsorship never changes scoring |
| Broad scope delays launch | High | High | Limit MVP to AI automation for small-business operators and 50 curated sources |
| Early paid conversion is weak | Medium | Medium | Validate manual briefings and alerts before building advanced subscriptions |
| Defamation or reputational disputes | Low/Medium | High | Strong sourcing, high-risk review, response/correction process, legal consultation |
| Search/API costs grow faster than revenue | Medium | Medium | Use Convex indexes and search first, cache public responses where appropriate, enforce rate limits, and instrument per-brief and per-query unit costs |

---

## 25. Key Assumptions to Validate

1. Operators care more about evidence and context than exhaustive directory coverage.
2. A daily or weekly briefing is a stronger initial habit than frequent website browsing.
3. Fifty curated sources can produce enough useful material for an MVP.
4. Users understand and value explicit evidence statuses.
5. Contributors will share sanitized field reports when attribution and incentives are clear.
6. Personalized alerts and comparisons are strong enough to support a $19/month Pro plan.
7. Automated bounded verification can be run economically for selected claims.
8. Vendors will pay for analytics or independent testing without requiring control over outcomes.

---

## 26. Open Questions and Decisions

| # | Question or decision | Recommended owner | Status |
|---:|---|---|---|
| 1 | Initial customer segment | Founder/Product | **Decided:** automation consultants, AI implementation agencies, fractional operators, and technically capable SMB operators |
| 2 | Launch Workflow Pack | Founder + Design Partners | **Decided:** AI customer-support platform selection for ecommerce and service businesses |
| 3 | Fit and Confidence presentation | Product/Design | **Decided:** descriptive Fit plus factor breakdown; numeric secondary; descriptive Confidence bands |
| 4 | Define what qualifies a contributor as trusted | Product/Editorial | Open |
| 5 | Define the minimum artifact required for each field-report type | Engineering/Editorial | Open |
| 6 | Select the exact MVP framework and hosting architecture | Engineering | Open |
| 7 | Choose email, billing, and analytics providers | Engineering | Open; **authentication decided:** Convex Auth |
| 8 | Determine whether Telegram briefings are available on Free or Pro | Product/Growth | Open |
| 9 | Establish source-content retention and licensing policy | Product/Legal | Open |
| 10 | Establish sponsored-test pricing and acceptance policy | Founder/Editorial | Open |
| 11 | Decide whether vendor factual corrections require verified domain ownership | Product/Engineering | Open |
| 12 | Verification budget and testing boundaries | Founder/Engineering | **Decided:** $500/month initial cap with approval thresholds and safe synthetic-testing boundaries in Section 29.17 |

---

## 27. Initial Workflow Taxonomy

### Committed launch Workflow Pack

The MVP launch pack is **AI customer-support platform selection for ecommerce and service businesses**.

The decision question is:

> Which AI customer-support platform should this business pilot based on its support volume, channels, existing systems, languages, budget, automation policy, data constraints, and escalation requirements?

Initial boundaries:

- Approximately 500–10,000 customer conversations per month
- English required; Filipino support evaluated when claimed or required
- Website chat, email, Messenger, or WhatsApp
- Common systems such as Shopify, WooCommerce, HubSpot, Zendesk, Gorgias, and Gmail
- Monthly software budget approximately $50–$1,000
- Human representatives available for escalation
- No highly regulated healthcare, financial, or legal support in the MVP
- Approximately 8–12 candidate products meeting minimum data requirements

### Future candidate Workflow Packs

1. Lead capture and qualification
2. Meeting transcription and summarization
3. Document and invoice extraction
4. Marketing-content production
5. Social-media scheduling
6. Email triage and drafting
7. Internal knowledge search
8. Workflow orchestration and integration
9. Coding and software-delivery assistance

Future packs are not simultaneous MVP scope. They may be added only after the launch pack demonstrates demand, recommendation quality, sustainable evidence maintenance, and acceptable unit economics.

---

## 28. Example Intelligence Record

### Example headline

**ExampleExtract adds structured invoice parsing at $0.012 per page; basic API test succeeded, but handwritten receipts remain unverified**

### What changed

ExampleExtract announced a structured invoice endpoint and published new pricing documentation.

### Why it matters

The endpoint may lower implementation effort for small businesses automating accounts-payable intake.

### Evidence status

**Verified for one bounded task; broader accuracy is unknown.**

### What OperatorWire tested

- Ten synthetic printed invoices
- API version and test date recorded
- Ten valid structured responses
- Median latency: 1.84 seconds
- Observed API cost: $0.012 per page
- No handwritten inputs tested

### Recommended action

**Test with your own invoice formats before migration.** Existing users processing only printed invoices may consider a limited pilot.

### Evidence

- Official changelog
- Current pricing-page snapshot
- Redacted verification-run metadata and output hashes

### Disclosure

No sponsorship or affiliate relationship.

---

## 29. Product Definition Revision: Specific Decision Advisor

This section resolves the main ambiguity discovered during product review: **OperatorWire is not merely an evidence-ranked news feed. Its core product is an evidence-backed advisor for a specific operational decision.** The feed remains important, but it serves discovery, acquisition, freshness, and evidence supply.

### 29.1 Two connected product experiences

| Experience | Primary job | Business role |
|---|---|---|
| **OperatorWire Feed** | Show what changed, why it matters, and what deserves attention | Free acquisition, retention, SEO, and evidence freshness |
| **OperatorWire Advisor** | Recommend the best-supported option for a defined situation | Core paid decision product |

The two experiences share sources, entities, evidence, and tool profiles. They must not be built as independent products.

### 29.2 The exact question being answered

> Given this operator’s workflow, desired outcome, expected volume, existing systems, mandatory integrations, budget, technical capacity, automation preferences, data constraints, language or regional needs, and risk tolerance: which eligible option has the strongest situational fit, how confident are we, what limitations remain, and what is the safest next step?

OperatorWire must not claim to identify a universally “best” tool.

### 29.3 Product principles added by this decision model

1. **Situational, not universal:** Every recommendation belongs to a versioned decision context.
2. **Requirements before ranking:** Mandatory requirements are evaluated before weighted preferences.
3. **Fit is not Confidence:** Suitability and evidentiary strength are displayed separately.
4. **Unknown is not supported:** Missing evidence reduces Confidence and is never treated as a pass.
5. **Pilot before commitment:** The default action under uncertainty is a bounded test with success and stop conditions.
6. **No forced winner:** “Insufficient evidence to recommend” is a valid result.
7. **Traceability:** Every recommendation and rejection must map to requirements, current facts, and evidence.

### 29.4 Decision Profile

A **Decision Profile** is a versioned, user-confirmed description of the situation. A workflow-specific diagnostic captures:

- Job to be done and desired outcome
- Business type and operating context
- Expected volume and frequency
- Existing stack and mandatory integrations
- Channels, languages, and regions
- Monthly and implementation budget
- Technical capacity and available implementation support
- Desired automation level and human-approval points
- Data sensitivity, privacy, and risk constraints
- Mandatory requirements
- Weighted preferences
- Success measure and target decision date

The system must show the normalized profile to the user for editing and confirmation before generating a recommendation.

### 29.5 Workflow Packs

OperatorWire cannot ask one generic set of questions for every decision. Each supported job uses a versioned **Workflow Pack** containing:

- Conditional diagnostic questions
- Requirement schema and normalization rules
- Candidate eligibility criteria
- Comparable capabilities and metrics
- Default Fit factors and weights
- Evidence freshness requirements
- Standardized test scenarios
- Field-report schema
- Decision Brief template
- Recommended pilot template and success criteria

The MVP launches with **one complete Workflow Pack**, not ten shallow categories: **AI customer-support platform selection for ecommerce and service businesses**. Phase 0 validates the diagnostic, candidate set, and willingness to pay rather than reopening the workflow selection unless evidence shows the segment is not viable.

### 29.6 Eligibility gate

Before ranking, each candidate receives one state:

| State | Meaning |
|---|---|
| Eligible | All mandatory requirements are supported by current evidence |
| Conditionally eligible | A requirement appears supported but must be confirmed in a pilot |
| Ineligible | At least one mandatory requirement is demonstrably unmet |
| Unknown | Evidence is insufficient to determine eligibility |

An ineligible candidate cannot be the primary recommendation. An unknown candidate can appear as a research option but cannot outrank an eligible candidate solely through weighted preferences.

### 29.7 Three separate scoring concepts

| Assessment | Question | Use |
|---|---|---|
| Intelligence Priority | Is this development worth attention? | Feed and alerts |
| Fit | How well does this candidate satisfy this Decision Profile? | Advisor recommendation |
| Confidence | How strongly does current evidence support the Fit assessment? | Risk and next-step guidance |

Initial Fit factors are workflow capability, existing-stack compatibility, cost, setup and maintenance effort, evidence from similar contexts, and risk/governance fit. Exact weights belong to the Workflow Pack.

Confidence is expressed as **High, Moderate, Low, or Insufficient** and considers source quality, independence, recency, product version, context similarity, sample size, variance, conflicts, failed tests, and data completeness. Sponsorship, affiliation, preference, and popularity can never increase Confidence.

### 29.8 Decision Brief contract

Every versioned Decision Brief must contain:

1. Decision question and profile summary
2. Primary recommendation or explicit insufficient-evidence conclusion
3. Eligibility, Fit, and Confidence
4. Estimated cost range and implementation effort
5. Verified strengths and known limitations
6. Mandatory requirements satisfied, unknown, or failed
7. Best alternatives and when each becomes preferable
8. Excluded candidates with concrete reasons
9. Evidence citations and last-checked timestamps
10. Assumptions and unresolved questions
11. Pilot scope, duration, success criteria, and stop conditions
12. Commercial disclosures

Changing the profile or underlying evidence creates a new brief version; historical recommendations are not silently rewritten.

### 29.9 Decision learning loop

After receiving a brief, the operator can record: reviewed, shortlisted, piloted, adopted, rejected, abandoned, or superseded. Optional actual cost, implementation effort, and outcome data remain private by default. With explicit consent and review, an outcome may become a Field Report. Unreviewed private feedback must not directly alter public evidence or rankings.

### 29.10 Business-model fit

The revised product ladder is:

| Tier | Value |
|---|---|
| Free | Global feed, public reports and profiles, limited follows, basic briefing, and a sample or limited brief |
| Pro | Full Decision Profiles, Decision Briefs, scenario changes, refreshed recommendations, alerts, pilot plans, and decision tracking |
| Team | Shared profiles, watchlists, notes, approved-tool views, and team decision history |
| API | Structured evidence, capability facts, Fit/Confidence inputs, and recommendation endpoints |
| Vendor Intelligence | Aggregated trends and independent sponsored testing, with no ranking influence |

The key monetization thesis is that users may consume the feed for free but pay to reduce the time and risk of a specific decision. This must be validated before advanced feed features or broad source coverage are expanded.

### 29.11 Added functional requirements

#### Decision Profiles and Workflow Packs

- **FR-091 [MUST]** Every supported workflow has a versioned Workflow Pack.
- **FR-092 [MUST]** The diagnostic captures the context fields defined in Section 29.4, using conditional questions where possible.
- **FR-093 [MUST]** Answers are normalized into an editable Decision Profile that requires user confirmation.
- **FR-094 [MUST]** Mandatory requirements are stored separately from weighted preferences.
- **FR-095 [MUST]** Profiles store the Workflow Pack version and can be saved, duplicated, revised, and archived.
- **FR-096 [MUST]** Authorized administrators can configure questions, mappings, metrics, weights, freshness rules, tests, and pilot templates without application-code changes.
- **FR-097 [MUST]** The MVP includes one complete Workflow Pack with sufficient candidate and evidence coverage.

#### Eligibility, Fit, Confidence, and briefs

- **FR-098 [MUST]** Mandatory requirements are evaluated before weighted Fit scoring.
- **FR-099 [MUST]** Each candidate receives Eligible, Conditionally eligible, Ineligible, or Unknown status with requirement-level reasons.
- **FR-100 [MUST]** Ineligible candidates cannot be the primary recommendation.
- **FR-101 [MUST]** Unknown requirements remain visible and reduce Confidence.
- **FR-102 [MUST]** Fit and Confidence are calculated and displayed separately.
- **FR-103 [MUST]** Fit explanations identify the profile attributes, capability facts, and evidence that materially affected the result.
- **FR-104 [MUST]** Confidence considers evidence quality, independence, recency, context similarity, sample size, completeness, and conflicts.
- **FR-105 [MUST]** The system can return an insufficient-evidence result instead of forcing a winner.
- **FR-106 [MUST]** Decision Briefs satisfy the contract in Section 29.8.
- **FR-107 [MUST]** Every recommendation and exclusion is traceable to versioned requirements, capability facts, and evidence.
- **FR-108 [MUST]** Decision Briefs are immutable versions; regeneration records what changed.
- **FR-109 [MUST]** The system proposes a bounded pilot whenever Confidence is not High.
- **FR-110 [SHOULD]** Users can see how changing a requirement or preference changes the recommendation.

#### Outcomes

- **FR-111 [MUST]** Users can record a decision state and optional actual cost, effort, and outcome.
- **FR-112 [MUST]** Decision outcomes are private by default.
- **FR-113 [MUST]** Private outcome data cannot become public evidence without explicit consent and review.
- **FR-114 [SHOULD]** An approved outcome can be converted into a Field Report with preserved provenance and disclosure.

### 29.12 Data-model additions

| Entity | Purpose |
|---|---|
| WorkflowPack | Versioned questions, metrics, rules, tests, and pilot template for one job |
| DecisionProfile | User-confirmed situational context and requirements |
| Requirement | Testable mandatory requirement or weighted preference |
| CapabilityFact | Current evidence-linked fact about a candidate |
| CandidateAssessment | Eligibility, Fit, Confidence, and reasons for one candidate |
| DecisionBrief | Immutable recommendation snapshot |
| DecisionOutcome | Private or consented result after the recommendation |

The architecture requires a **Decision Engine** responsible for Workflow Pack execution, requirement evaluation, eligibility, Fit, Confidence, and brief generation. It consumes the same entity, evidence, verification, and field-report data maintained by the aggregation system.

### 29.13 Revised MVP boundary and dependency order

The implementation backlog must preserve this order:

1. **Evidence Supply:** source collection, normalization, entities, and current capability facts.
2. **Trust and Verification:** provenance, status, freshness, tests, field reports, disclosures, and corrections.
3. **Decision Modeling:** one Workflow Pack, Decision Profiles, mandatory-requirement gate, Fit, and Confidence.
4. **Decision Delivery:** traceable Decision Brief, alternatives, exclusions, and pilot plan.
5. **Learning and Commercialization:** private outcomes, subscriptions, and later consented evidence.

A polished recommendation interface is not useful without structured candidate facts. Aggregation alone is not the product without decision modeling.

### 29.14 Revised validation and launch gates

Before backlog decomposition is treated as committed scope, Phase 0 must:

- Conduct 10–15 operator interviews centered on recent real tool decisions.
- Produce 10 manual intelligence reports and 5 concierge Decision Briefs.
- Validate which diagnostic questions actually change recommendations.
- Validate the committed customer-support Workflow Pack using decision frequency, candidate comparability, testability, evidence availability, and willingness to pay.
- Confirm that at least three of five concierge briefs produce a shortlist, pilot, or changed decision.

MVP launch additionally requires:

- A versioned diagnostic, requirement schema, candidate dataset, Fit/Confidence logic, and pilot template for the launch Workflow Pack.
- At least 10 internally reviewed briefs with complete requirement-to-evidence traceability.
- Proof that ineligible candidates cannot become recommendations and unknown facts visibly reduce Confidence.
- Successful generation of an insufficient-evidence brief.
- Private outcome capture and consent controls.

### 29.15 Added success measures

- **Qualified Decision Briefs Generated:** user-confirmed profile, at least two evaluated candidates, and full traceability.
- Decision Profile completion rate.
- Brief-to-shortlist or brief-to-pilot rate; initial target ≥25%.
- Pilot-to-adoption rate by Workflow Pack.
- 100% requirement-to-evidence traceability for generated briefs.
- Percentage of recommendations later contradicted by validated outcomes.
- Time saved compared with the operator’s previous evaluation process.

### 29.16 Risks introduced or clarified

| Risk | Mitigation |
|---|---|
| Diagnostic is too generic to change the answer | Workflow-specific questions; validate each question through concierge decisions |
| Candidate facts are too incomplete | One launch pack, minimum data-completeness rule, and insufficient-evidence result |
| Users interpret recommendations as guarantees | Separate Fit and Confidence; show assumptions; require bounded pilots under uncertainty |
| Workflow schemas become unmaintainable | Versioned configurable Workflow Packs and strict expansion gates |
| Feed scope consumes effort before advisor value is proven | Treat feed as evidence supply and acquisition; prioritize concierge advisor validation |

### 29.17 Approved product decisions

The following decisions were approved by the founder on 2026-07-11 and are no longer open assumptions:

1. **Initial customer:** Automation consultants, AI implementation agencies, fractional operations specialists, and technically capable SMB operators serving businesses with approximately 5–100 employees.
2. **Launch Workflow Pack:** AI customer-support platform selection for ecommerce and service businesses, within the boundaries in Section 27.
3. **Fit presentation:** Lead with descriptive labels—Strong, Good, Conditional, Weak, Ineligible, or Unknown—plus a visible factor breakdown. A numeric Fit score may appear as secondary detail. Confidence uses High, Moderate, Low, or Insufficient bands.
4. **Free allowance:** One complete Decision Profile and Brief plus one refresh within 30 days. Pro initially includes three new finalized profiles per month; Team includes 20. Beta remains concierge-based until unit costs are known.
5. **Verification budget:** Initial cap of **$500 per month**, allocated approximately as $200 tool subscriptions, $150 API/usage fees, $75 test infrastructure, $25 evidence storage/monitoring, and $50 contingency. Founder/editor approval is required for a test over $10, a subscription over $50/month, more than five repeated runs, production access, unusual privileges, or vendor credits that create a disclosure obligation.
6. **Testing boundaries:** MVP tests may use documented APIs, sandboxes, synthetic support conversations and records, controlled test accounts, ordinary integrations, human-handoff behavior, accuracy against known content, latency, cost, and setup effort. It must not use real customer PII, production systems, real financial transactions, destructive actions, vulnerability exploitation, unauthorized load testing, rate-limit bypass, undocumented private endpoints, or highly regulated advice.

### 29.18 Candidate data-completeness and freshness policy

A candidate may be **Eligible** only when all mandatory requirements have current supporting evidence, pricing can be estimated for the Decision Profile, at least one relevant verification run or reviewed Field Report exists, and no unresolved critical contradiction affects a mandatory requirement.

| Candidate data | Required | Maximum evidence age |
|---|---:|---:|
| Product availability | Yes | 7 days |
| Current pricing structure | Yes | 14 days |
| Required channels | Yes | 30 days |
| Required integrations | Yes | 30 days |
| Human escalation | Yes | 30 days |
| Automation controls | Yes | 30 days |
| Data handling/privacy policy | Yes | 90 days |
| Regional availability | Yes | 30 days |
| Required language support | When applicable | 30 days |
| Setup requirements | Yes | 90 days |
| Relevant verification run or reviewed Field Report | Yes | 90 days |
| Known material limitations | Yes | Continuously maintained |
| Commercial disclosures | Yes | Current |

Vendor documentation establishes what a vendor claims, not independent proof of performance. When critical evidence expires, the system recalculates eligibility and Confidence, may downgrade the candidate, preserves historical briefs, and offers users a refreshed brief.

### 29.19 Customer-support verification baseline

The launch Workflow Pack uses approximately 25–50 synthetic conversations covering product questions, order status, returns and refunds, missing information, ambiguity, angry customers, escalation, unsupported requests, policy hallucination, prompt injection, English, Filipino when claimed, channel/integration behavior, and cost per resolved or escalated conversation.

Minimum repetitions:

- Critical functional scenarios: at least three runs each
- Published latency median: at least ten runs
- Reliability claims: repeated across multiple time windows
- Language quality: qualified human review
- Field outcomes: clearly separated from synthetic outcomes

A single successful call proves only that the function worked once; it does not establish general reliability.

---

## 30. Glossary

- **Claim:** An atomic assertion attributed to a specific source.
- **Corroboration:** Support from sufficiently independent credible evidence.
- **Entity:** A product, company, API, model, project, or other monitored subject.
- **Evidence status:** A label communicating how strongly a claim has been checked.
- **Field report:** A structured account of using a tool or insight in a real or representative workflow.
- **Intelligence record:** OperatorWire’s evolving, decision-oriented report about a material event or finding.
- **Operator:** A person responsible for choosing and implementing tools or workflows to produce business outcomes.
- **Proof of use:** Evidence that a tool or recommendation was applied to a defined task with an observable outcome.
- **Source item:** A parsed article, release, post, page change, or API record collected from a source.
- **Utility score:** A versioned ranking composed of relevance, evidence, practical impact, verification, recency, and source credibility.
- **Verification run:** A bounded inspection or test intended to confirm or challenge a specific claim.

---

## 31. Reference Product Statement

**Elevator pitch:** OperatorWire helps operators choose AI tools for their specific workflow using current evidence instead of directories, hype, or generic rankings. It monitors what changed, filters candidates against the operator’s actual requirements, and produces a transparent recommendation with limitations, confidence, and a practical pilot plan.

**Core promise:** Tell us the job, constraints, and desired outcome; OperatorWire will show the best-supported fit, why it fits, what remains uncertain, and the safest next step.
