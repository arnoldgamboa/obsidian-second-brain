from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, Table, TableStyle,
    PageBreak, Image, KeepTogether, HRFlowable
)
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.utils import ImageReader
from datetime import date
import os

BASE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(BASE, "Mustard-Seed-Managed-AI-Employee-Implementation-Plan.pdf")
LOGO = os.path.join(BASE, "mssc-logo.png")

PAGE_W, PAGE_H = A4
M = 18 * mm
BLUE = colors.HexColor("#282A98")
BLUE_DARK = colors.HexColor("#171962")
BLUE_LIGHT = colors.HexColor("#EEF0FF")
GOLD = colors.HexColor("#D7A62A")
GREEN = colors.HexColor("#3C7A57")
INK = colors.HexColor("#1C2230")
MUTED = colors.HexColor("#5E6678")
LINE = colors.HexColor("#D9DDEA")
PALE = colors.HexColor("#F7F8FC")
WHITE = colors.white
RED = colors.HexColor("#A33A3A")

styles = getSampleStyleSheet()

def ps(name, **kw):
    return ParagraphStyle(name, **kw)

TITLE = ps("Title", fontName="Helvetica-Bold", fontSize=29, leading=33, textColor=BLUE_DARK, spaceAfter=10)
SUBTITLE = ps("Subtitle", fontName="Helvetica", fontSize=13, leading=18, textColor=MUTED, spaceAfter=12)
H1 = ps("H1", fontName="Helvetica-Bold", fontSize=21, leading=25, textColor=BLUE_DARK, spaceBefore=2, spaceAfter=9)
H2 = ps("H2", fontName="Helvetica-Bold", fontSize=13, leading=16, textColor=BLUE, spaceBefore=8, spaceAfter=5)
H3 = ps("H3", fontName="Helvetica-Bold", fontSize=10.5, leading=14, textColor=INK, spaceBefore=4, spaceAfter=3)
BODY = ps("Body", fontName="Helvetica", fontSize=9.4, leading=13.2, textColor=INK, spaceAfter=6)
SMALL = ps("Small", fontName="Helvetica", fontSize=7.8, leading=10.5, textColor=MUTED, spaceAfter=3)
CAP = ps("Cap", fontName="Helvetica-Bold", fontSize=7.2, leading=9, textColor=BLUE, tracking=0.8, spaceAfter=3)
WHITE_H = ps("WhiteH", fontName="Helvetica-Bold", fontSize=13, leading=16, textColor=WHITE, spaceAfter=3)
WHITE_B = ps("WhiteB", fontName="Helvetica", fontSize=9.2, leading=13, textColor=WHITE)
QUOTE = ps("Quote", fontName="Helvetica-Bold", fontSize=15, leading=20, textColor=BLUE_DARK, alignment=TA_CENTER, spaceAfter=4)
TABLE_H = ps("TableH", fontName="Helvetica-Bold", fontSize=7.7, leading=9.5, textColor=WHITE)
TABLE_C = ps("TableC", fontName="Helvetica", fontSize=7.6, leading=10, textColor=INK)
TABLE_CB = ps("TableCB", fontName="Helvetica-Bold", fontSize=7.6, leading=10, textColor=INK)
NUM = ps("Num", fontName="Helvetica-Bold", fontSize=17, leading=18, textColor=BLUE, alignment=TA_CENTER)


def P(text, style=BODY):
    return Paragraph(text, style)


def bullet(text, color=BLUE):
    return Table([[P("•", ps("dot", fontName="Helvetica-Bold", fontSize=10, textColor=color, leading=12)), P(text, BODY)]],
                 colWidths=[5*mm, 155*mm], style=[
                     ("VALIGN", (0,0), (-1,-1), "TOP"),
                     ("LEFTPADDING", (0,0), (-1,-1), 0),
                     ("RIGHTPADDING", (0,0), (-1,-1), 0),
                     ("TOPPADDING", (0,0), (-1,-1), 0),
                     ("BOTTOMPADDING", (0,0), (-1,-1), 1),
                 ])


def section_title(kicker, title, intro=None):
    parts = [P(kicker.upper(), CAP), P(title, H1), HRFlowable(width="100%", thickness=1.2, color=GOLD, spaceAfter=8)]
    if intro:
        parts.append(P(intro, BODY))
    return parts


def info_card(title, body, bg=BLUE_LIGHT, accent=BLUE):
    t = Table([[P(title, H3)], [P(body, BODY)]], colWidths=[160*mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), bg),
        ("BOX", (0,0), (-1,-1), 0.7, accent),
        ("LINEBEFORE", (0,0), (0,-1), 4, accent),
        ("LEFTPADDING", (0,0), (-1,-1), 10),
        ("RIGHTPADDING", (0,0), (-1,-1), 10),
        ("TOPPADDING", (0,0), (-1,-1), 7),
        ("BOTTOMPADDING", (0,0), (-1,-1), 7),
    ]))
    return t


def two_cards(cards):
    cells = []
    for title, body in cards:
        c = Table([[P(title, H3)], [P(body, SMALL)]], colWidths=[75*mm])
        c.setStyle(TableStyle([
            ("BACKGROUND", (0,0), (-1,-1), PALE),
            ("BOX", (0,0), (-1,-1), 0.5, LINE),
            ("LEFTPADDING", (0,0), (-1,-1), 8),
            ("RIGHTPADDING", (0,0), (-1,-1), 8),
            ("TOPPADDING", (0,0), (-1,-1), 7),
            ("BOTTOMPADDING", (0,0), (-1,-1), 7),
        ]))
        cells.append(c)
    tbl = Table([cells], colWidths=[80*mm, 80*mm], hAlign="LEFT")
    tbl.setStyle(TableStyle([("VALIGN", (0,0), (-1,-1), "TOP"), ("LEFTPADDING", (0,0), (-1,-1), 0), ("RIGHTPADDING", (0,0), (-1,-1), 5)]))
    return tbl


def footer(canvas: Canvas, doc):
    canvas.saveState()
    if doc.page > 1:
        canvas.setStrokeColor(LINE)
        canvas.setLineWidth(0.5)
        canvas.line(M, 12*mm, PAGE_W-M, 12*mm)
        canvas.setFillColor(MUTED)
        canvas.setFont("Helvetica", 7.5)
        canvas.drawString(M, 7.5*mm, "ArwenDigital  •  Managed AI Employee Implementation Plan")
        canvas.drawRightString(PAGE_W-M, 7.5*mm, f"Mustard Seed Systems Corporation  •  {doc.page}")
    canvas.restoreState()


def cover_bg(canvas: Canvas, doc):
    canvas.saveState()
    canvas.setFillColor(PALE)
    canvas.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    canvas.setFillColor(BLUE_DARK)
    canvas.rect(0, 0, 14*mm, PAGE_H, fill=1, stroke=0)
    canvas.setFillColor(GOLD)
    canvas.rect(14*mm, 0, 2.2*mm, PAGE_H, fill=1, stroke=0)
    canvas.restoreState()


def later_bg(canvas: Canvas, doc):
    footer(canvas, doc)


doc = BaseDocTemplate(
    OUT, pagesize=A4, leftMargin=M, rightMargin=M, topMargin=16*mm, bottomMargin=18*mm,
    title="Managed AI Employee Implementation Plan — Mustard Seed Systems Corporation",
    author="Arnold Gamboa / ArwenDigital",
    subject="Proposed Growth Operations AI Employee implementation plan"
)
cover_frame = Frame(23*mm, 18*mm, PAGE_W-41*mm, PAGE_H-36*mm, id="cover")
body_frame = Frame(M, 18*mm, PAGE_W-2*M, PAGE_H-34*mm, id="body")
doc.addPageTemplates([
    PageTemplate(id="Cover", frames=[cover_frame], onPage=cover_bg),
    PageTemplate(id="Body", frames=[body_frame], onPage=later_bg),
])

story = []
# Cover
if os.path.exists(LOGO):
    story.append(Image(LOGO, width=142*mm, height=25.8*mm))
story += [
    Spacer(1, 25*mm),
    P("CONFIDENTIAL DISCUSSION DRAFT", CAP),
    P("Managed AI Employee<br/>Implementation Plan", TITLE),
    P("A focused six-week deployment for Mustard Seed Systems Corporation", SUBTITLE),
    Spacer(1, 7*mm),
]
cover_card = Table([
    [P("RECOMMENDED INITIAL DEPLOYMENT", CAP)],
    [P("Growth Operations AI Employee", ps("CoverDeploy", fontName="Helvetica-Bold", fontSize=18, leading=22, textColor=WHITE))],
    [P("Connect marketing activity, inbound inquiries, solution routing, and sales follow-through—while preserving human control over pricing, commitments, and customer relationships.", WHITE_B)],
], colWidths=[151*mm])
cover_card.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,-1), BLUE_DARK),
    ("LEFTPADDING", (0,0), (-1,-1), 12),
    ("RIGHTPADDING", (0,0), (-1,-1), 12),
    ("TOPPADDING", (0,0), (-1,-1), 9),
    ("BOTTOMPADDING", (0,0), (-1,-1), 9),
]))
story += [cover_card, Spacer(1, 28*mm), P("Prepared for", CAP), P("Mustard Seed Systems Corporation", H2), P("Prepared by Arnold Gamboa / ArwenDigital", BODY), Spacer(1, 4*mm), P("20 July 2026  •  Version 1.0", SMALL), PageBreak()]

# Page 2
story += section_title("01 / Opportunity", "A practical first AI employee for Mustard Seed",
    "Mustard Seed has helped Philippine organizations adopt business technology since 1999. Its broad portfolio creates a valuable operating opportunity: make every qualified inquiry easier to understand, route, act on, and follow through.")
story += [
    info_card("Recommended starting responsibility", "Ensure every qualified inquiry receives a timely, informed, and traceable next action—from first capture through routing, response preparation, CRM ownership, and follow-up monitoring."),
    Spacer(1, 6*mm),
    P("Why this workflow fits", H2),
    P("Mustard Seed presents multiple solution lines and affiliated websites, including AccountingPro, HRMSPro, BuildingPro, and OfficeWorks. A new inquiry may therefore require more than a generic acknowledgement: the team must understand the prospect, identify the relevant offering, route the opportunity, and maintain consistent follow-through."),
    Spacer(1, 3*mm),
    two_cards([
        ("Business outcome", "Faster response, cleaner ownership, fewer dropped follow-ups, and better-prepared sales conversations."),
        ("Operating principle", "Start with one measurable lane. Expand only after the workflow proves useful, safe, and trusted."),
    ]),
    Spacer(1, 7*mm),
    P("Expected benefits", H2),
]
for x in [
    "Reduce time from inquiry to first meaningful action.",
    "Improve routing consistency across solution lines and teams.",
    "Give sales staff a concise prospect brief before they engage.",
    "Keep every active inquiry attached to an owner, next action, and due date.",
    "Turn inquiry patterns into useful marketing and management insight.",
    "Free sales and marketing staff to focus on relationships, solution design, and closing.",
]: story.append(bullet(x))
story += [Spacer(1, 7*mm), P("Mustard Seed manages the business outcome. ArwenDigital manages the AI employee.", QUOTE), PageBreak()]

# Page 3
story += section_title("02 / Recommended workflow", "Growth Operations AI Employee",
    "The proposed first workflow connects approved inquiry channels to a consistent, reviewable next action. The final workflow will be confirmed during discovery.")
workflow = [
    [P("1", NUM), P("CAPTURE", CAP), P("New inquiry from an approved form, inbox, campaign, referral source, event list, or CRM queue.", TABLE_C)],
    [P("2", NUM), P("CONTEXT", CAP), P("Normalize contact details, check duplicates, and collect approved company and account context.", TABLE_C)],
    [P("3", NUM), P("RECOMMEND", CAP), P("Summarize the need and recommend the likely Mustard Seed solution family or internal owner.", TABLE_C)],
    [P("4", NUM), P("PREPARE", CAP), P("Draft a personalized acknowledgement or follow-up using approved templates and business rules.", TABLE_C)],
    [P("5", NUM), P("ASSIGN", CAP), P("Create or update the record, propose an owner, next action, and due date, subject to agreed controls.", TABLE_C)],
    [P("6", NUM), P("FOLLOW THROUGH", CAP), P("Monitor the agreed response window, surface stalled opportunities, and summarize demand themes.", TABLE_C)],
]
wt = Table(workflow, colWidths=[12*mm, 30*mm, 118*mm], repeatRows=0)
wt.setStyle(TableStyle([
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("BACKGROUND", (0,0), (-1,-1), PALE),
    ("ROWBACKGROUNDS", (0,0), (-1,-1), [WHITE, PALE]),
    ("LINEBELOW", (0,0), (-1,-2), 0.5, LINE),
    ("LEFTPADDING", (0,0), (-1,-1), 6),
    ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ("TOPPADDING", (0,0), (-1,-1), 7),
    ("BOTTOMPADDING", (0,0), (-1,-1), 7),
]))
story += [wt, Spacer(1, 7*mm), P("Human authority retained", H2)]
for x in [
    "Final solution recommendation when requirements are unclear.",
    "Pricing, discounts, proposals, contracts, and commercial commitments.",
    "Sensitive, strategic, unusual, or high-value customer communication.",
    "Final decisions on disqualification, closure, or ownership where judgment is required.",
]: story.append(bullet(x, GOLD))
story += [Spacer(1, 5*mm), info_card("Definition of done", "A processed inquiry has a verified contact and organization record, a solution category or documented exception, an assigned human owner, a traceable next action and due date, and an approved or sent first response according to the agreed control level.", colors.HexColor("#FFF9E9"), GOLD), PageBreak()]

# Page 4
story += section_title("03 / Delivery plan", "Weeks 1–2: define the workflow before building",
    "The project begins with the operating reality—triggers, systems, rules, exceptions, ownership, and measurable outcomes—not with a technology demo.")
phases12 = [
    [P("WEEK 1", TABLE_H), P("DISCOVERY & BASELINE", TABLE_H), P("KEY ACTIVITIES", TABLE_H), P("DELIVERABLES", TABLE_H)],
    [P("01", NUM), P("Current-state workflow", TABLE_CB), P("Map inquiry sources, routing, handoffs, ownership, templates, sample cases, exceptions, and current reporting. Establish baseline volume, first-response time, missed follow-ups, and handling effort.", TABLE_C), P("Workflow map<br/>Scope statement<br/>Baseline<br/>Access list<br/>Risk register<br/>Success criteria", TABLE_C)],
    [P("WEEK 2", TABLE_H), P("SOLUTION DESIGN", TABLE_H), P("KEY ACTIVITIES", TABLE_H), P("DELIVERABLES", TABLE_H)],
    [P("02", NUM), P("Future-state workflow", TABLE_CB), P("Define approved data sources, routing rules, authority levels, human approvals, escalation paths, logging, retention, and test scenarios for normal, duplicate, incomplete, sensitive, and failure cases.", TABLE_C), P("Future-state design<br/>Responsibility matrix<br/>Approval matrix<br/>Security plan<br/>Acceptance-test plan", TABLE_C)],
]
t = Table(phases12, colWidths=[19*mm, 35*mm, 67*mm, 39*mm], repeatRows=0)
t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), BLUE_DARK),
    ("BACKGROUND", (0,2), (-1,2), BLUE),
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("GRID", (0,0), (-1,-1), 0.4, LINE),
    ("LEFTPADDING", (0,0), (-1,-1), 6),
    ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ("TOPPADDING", (0,0), (-1,-1), 8),
    ("BOTTOMPADDING", (0,0), (-1,-1), 8),
]))
story += [t, Spacer(1, 8*mm), info_card("Decision gate after Week 1", "Mustard Seed and ArwenDigital approve the selected workflow, boundaries, owners, measurable outcome, and required access before implementation begins."), Spacer(1, 5*mm), info_card("Decision gate after Week 2", "Mustard Seed approves the future-state workflow, safeguards, and access plan before live credentials or production data are connected.", colors.HexColor("#FFF9E9"), GOLD), PageBreak()]

# Page 5
story += section_title("03 / Delivery plan", "Weeks 3–6: build, test, and launch under control")
phase_data = [
    [P("WHEN", TABLE_H), P("PHASE", TABLE_H), P("WHAT HAPPENS", TABLE_H), P("PRIMARY OUTPUT", TABLE_H)],
    [P("Weeks 3–4", TABLE_CB), P("Build & integration", TABLE_CB), P("Connect approved channels and the system of record. Implement context collection, duplicate checks, lead summaries, routing, response drafts, task creation, follow-up tracking, logs, alerts, and failure handling.", TABLE_C), P("Working controlled-environment implementation", TABLE_C)],
    [P("Week 5", TABLE_CB), P("Acceptance & readiness", TABLE_CB), P("Run normal, exception, duplicate, missing-information, and failure scenarios. Validate routing, drafts, updates, ownership, and escalation. Train designated users and confirm support and rollback.", TABLE_C), P("Signed test record and production checklist", TABLE_C)],
    [P("Week 6", TABLE_CB), P("Controlled launch", TABLE_CB), P("Launch with limited volume or authority. Keep high-impact external actions under human approval. Review activity daily, resolve issues, compare initial results with baseline, and build the improvement backlog.", TABLE_C), P("Production AI employee and launch report", TABLE_C)],
]
t = Table(phase_data, colWidths=[23*mm, 36*mm, 71*mm, 30*mm], repeatRows=1)
t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), BLUE_DARK),
    ("ROWBACKGROUNDS", (0,1), (-1,-1), [WHITE, PALE]),
    ("GRID", (0,0), (-1,-1), 0.4, LINE),
    ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("LEFTPADDING", (0,0), (-1,-1), 6),
    ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ("TOPPADDING", (0,0), (-1,-1), 8),
    ("BOTTOMPADDING", (0,0), (-1,-1), 8),
]))
story += [t, Spacer(1, 8*mm), P("Pilot scope", H2)]
scope = [
    [P("INCLUDED", TABLE_H), P("NOT INCLUDED UNLESS ADDED", TABLE_H)],
    [P("One inquiry-to-follow-up workflow<br/>Up to three primary input channels<br/>One primary CRM or system of record<br/>Approved context, rules, and templates<br/>Human approval and escalation controls<br/>Monitoring, testing, launch support, and onboarding", TABLE_C),
     P("Replacing the CRM, marketing platform, or websites<br/>Autonomous pricing, proposal approval, or contract negotiation<br/>Unrelated historical data migration<br/>Unrestricted access to customer or financial data<br/>Additional departmental workflows<br/>A full redesign of sales and marketing operations", TABLE_C)]
]
st = Table(scope, colWidths=[80*mm, 80*mm])
st.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (0,0), GREEN), ("BACKGROUND", (1,0), (1,0), MUTED),
    ("BOX", (0,0), (-1,-1), 0.5, LINE), ("INNERGRID", (0,0), (-1,-1), 0.5, LINE),
    ("VALIGN", (0,0), (-1,-1), "TOP"), ("LEFTPADDING", (0,0), (-1,-1), 8),
    ("RIGHTPADDING", (0,0), (-1,-1), 8), ("TOPPADDING", (0,0), (-1,-1), 7), ("BOTTOMPADDING", (0,0), (-1,-1), 7),
]))
story += [st, PageBreak()]

# Page 6
story += section_title("04 / Control & security", "Earn autonomy; do not assume it",
    "The first release will default to visible, reviewable work. Automatic action is introduced only for narrowly defined, low-risk cases with testing, logging, and rollback.")
control = [
    [P("LEVEL", TABLE_H), P("AI EMPLOYEE BEHAVIOR", TABLE_H), P("INITIAL MUSTARD SEED USE", TABLE_H)],
    [P("Observe", TABLE_CB), P("Reads approved information and surfaces what needs attention.", TABLE_C), P("Monitor new leads and stalled opportunities.", TABLE_C)],
    [P("Prepare", TABLE_CB), P("Creates a summary, draft, recommendation, or proposed update.", TABLE_C), P("Prospect briefs, routing recommendations, response drafts.", TABLE_C)],
    [P("Act with approval", TABLE_CB), P("Performs the action only after a designated person approves it.", TABLE_C), P("External responses and material CRM updates.", TABLE_C)],
    [P("Act automatically", TABLE_CB), P("Performs a low-risk, reversible action under an explicit rule.", TABLE_C), P("Internal task creation after sufficient testing.", TABLE_C)],
]
t = Table(control, colWidths=[31*mm, 62*mm, 67*mm], repeatRows=1)
t.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), BLUE_DARK), ("ROWBACKGROUNDS", (0,1), (-1,-1), [WHITE, PALE]),
    ("GRID", (0,0), (-1,-1), 0.4, LINE), ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("LEFTPADDING", (0,0), (-1,-1), 6), ("RIGHTPADDING", (0,0), (-1,-1), 6),
    ("TOPPADDING", (0,0), (-1,-1), 7), ("BOTTOMPADDING", (0,0), (-1,-1), 7),
]))
story += [t, Spacer(1, 7*mm), P("The AI employee escalates instead of guessing when", H2)]
for x in [
    "Required information is missing, conflicting, or outside the approved source of truth.",
    "The inquiry involves pricing, commitments, unusual terms, sensitive data, or reputational risk.",
    "The case falls outside documented routing or response rules.",
    "A connected system fails or returns an unexpected result.",
    "A person has explicitly requested review.",
]: story.append(bullet(x, GOLD))
story += [Spacer(1, 5*mm), P("Security principles", H2)]
security = [
    ("Least privilege", "Connect only the systems and permissions required for this workflow."),
    ("Protected credentials", "Keep secrets out of prompts, templates, and informal documents."),
    ("Traceability", "Log material actions, approvals, failures, and escalations."),
    ("Controlled expansion", "Add systems, data, or authority only through approved change control."),
]
for i in range(0,4,2): story.append(two_cards(security[i:i+2])); story.append(Spacer(1,3*mm))
story += [PageBreak()]

# Page 7
story += section_title("05 / Solution design", "Managed operating architecture",
    "The exact tools will be selected after discovery. Mustard Seed receives a managed outcome rather than a collection of disconnected AI subscriptions.")
arch_rows = [
    [P("1", NUM), P("APPROVED INPUTS", CAP), P("Website forms • Shared inboxes • Campaign lists • Referral or event sources • CRM queues", TABLE_C)],
    [P("2", NUM), P("WORKFLOW LAYER", CAP), P("Trigger handling • Scheduling • Duplicate checks • Routing • State • Retry and error handling", TABLE_C)],
    [P("3", NUM), P("AI + CONTEXT", CAP), P("Classification • Summarization • Drafting • Approved solution descriptions • FAQs • Templates • Policies", TABLE_C)],
    [P("4", NUM), P("HUMAN CONTROL", CAP), P("Review • Approve • Reject • Escalate • Override • Request changes", TABLE_C)],
    [P("5", NUM), P("BUSINESS SYSTEMS", CAP), P("CRM or system of record • Task ownership • Approved communication channels • Management reporting", TABLE_C)],
    [P("6", NUM), P("MANAGED OPERATIONS", CAP), P("Hosting • Monitoring • Alerts • Audit history • Backups • Updates • Incident response • Improvement", TABLE_C)],
]
at = Table(arch_rows, colWidths=[13*mm, 37*mm, 110*mm])
at.setStyle(TableStyle([
    ("ROWBACKGROUNDS", (0,0), (-1,-1), [BLUE_LIGHT, WHITE]), ("BOX", (0,0), (-1,-1), 0.6, LINE),
    ("LINEBELOW", (0,0), (-1,-2), 0.4, LINE), ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("LEFTPADDING", (0,0), (-1,-1), 7), ("RIGHTPADDING", (0,0), (-1,-1), 7),
    ("TOPPADDING", (0,0), (-1,-1), 8), ("BOTTOMPADDING", (0,0), (-1,-1), 8),
]))
story += [at, Spacer(1, 8*mm), info_card("Managed technical responsibility", "Within the agreed scope, ArwenDigital selects, administers, monitors, maintains, and improves the AI models, workflow components, hosting, integrations, safeguards, logs, and support procedures needed by the AI employee."), Spacer(1,5*mm), P("Existing subscriptions", H2), P("Mustard Seed's existing email, CRM, marketing, messaging, accounting, or industry software normally remains Mustard Seed's subscription unless the final statement of work explicitly includes it. Premium data, unusual infrastructure, or high-volume messaging may be priced separately."), PageBreak()]

# Page 8
story += section_title("06 / Measurement", "Success is an operating result",
    "Final targets will be agreed during discovery after the current baseline is measured.")
metrics = [
    [P("MEASURE", TABLE_H), P("BASELINE", TABLE_H), P("INITIAL TARGET", TABLE_H)],
    [P("Median time from inquiry to first action", TABLE_CB), P("To measure", TABLE_C), P("50% reduction or agreed service level", TABLE_C)],
    [P("Qualified inquiries routed correctly", TABLE_CB), P("To measure", TABLE_C), P("90%+ after stabilization", TABLE_C)],
    [P("Inquiries with owner and next action", TABLE_CB), P("To measure", TABLE_C), P("95%+", TABLE_C)],
    [P("First-pass acceptance of prepared drafts", TABLE_CB), P("To measure", TABLE_C), P("80%+", TABLE_C)],
    [P("Follow-ups overdue beyond agreed window", TABLE_CB), P("To measure", TABLE_C), P("50% reduction", TABLE_C)],
    [P("Manual handling time per inquiry", TABLE_CB), P("To measure", TABLE_C), P("30% reduction", TABLE_C)],
    [P("Critical customer-facing errors", TABLE_CB), P("N/A", TABLE_C), P("Zero unresolved critical incidents", TABLE_C)],
]
mt = Table(metrics, colWidths=[76*mm, 32*mm, 52*mm], repeatRows=1)
mt.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), BLUE_DARK), ("ROWBACKGROUNDS", (0,1), (-1,-1), [WHITE, PALE]),
    ("GRID", (0,0), (-1,-1), 0.4, LINE), ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("LEFTPADDING", (0,0), (-1,-1), 7), ("RIGHTPADDING", (0,0), (-1,-1), 7),
    ("TOPPADDING", (0,0), (-1,-1), 8), ("BOTTOMPADDING", (0,0), (-1,-1), 8),
]))
story += [mt, Spacer(1, 8*mm), P("Acceptance criteria", H2)]
for x in [
    "Agreed normal test cases complete successfully.",
    "Duplicate, missing, sensitive, ambiguous, and unsupported cases escalate correctly.",
    "Human approval is enforced wherever required.",
    "Routing, ownership, next actions, and approved record updates are accurate and traceable.",
    "Failed actions are visible and assigned; they do not silently disappear.",
    "Designated users can review, approve, reject, and report issues.",
    "Monitoring, support, and rollback procedures are active, with no unresolved critical defect.",
]: story.append(bullet(x))
story += [Spacer(1, 6*mm), info_card("Production decision", "Mustard Seed's designated owner signs the acceptance record. The parties then decide—based on evidence—whether to continue, narrow, pause, or expand the workflow.", colors.HexColor("#FFF9E9"), GOLD), PageBreak()]

# Page 9
story += section_title("07 / Ownership", "Clear accountability on both sides")
roles = [
    [P("ARWENDIGITAL", TABLE_H), P("MUSTARD SEED SYSTEMS CORPORATION", TABLE_H)],
    [P("Lead discovery and workflow design<br/><br/>Build, connect, test, deploy, and manage the AI employee<br/><br/>Configure approvals, escalation, access, logging, monitoring, and support<br/><br/>Maintain managed technical components within scope<br/><br/>Document the operating workflow and train designated users<br/><br/>Report incidents, performance, risks, and recommended improvements", TABLE_C),
     P("Assign one accountable project owner and available process experts<br/><br/>Provide timely access to approved systems, examples, rules, templates, and policies<br/><br/>Identify authoritative information and regulated or contractual requirements<br/><br/>Review designs and outputs within agreed response times<br/><br/>Participate in testing and approve production launch<br/><br/>Notify ArwenDigital when relevant systems, policies, or workflows change", TABLE_C)]
]
rt = Table(roles, colWidths=[80*mm,80*mm])
rt.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (0,0), BLUE_DARK), ("BACKGROUND", (1,0), (1,0), BLUE),
    ("GRID", (0,0), (-1,-1), 0.5, LINE), ("VALIGN", (0,0), (-1,-1), "TOP"),
    ("LEFTPADDING", (0,0), (-1,-1), 9), ("RIGHTPADDING", (0,0), (-1,-1), 9),
    ("TOPPADDING", (0,0), (-1,-1), 9), ("BOTTOMPADDING", (0,0), (-1,-1), 9),
]))
story += [rt, Spacer(1, 8*mm), P("Governance rhythm", H2)]
gov = [
    ("During implementation", "Weekly 30-minute project review; decisions and blockers recorded; critical issues escalated immediately."),
    ("During launch", "Daily operating review while volume or authority remains limited."),
]
story.append(two_cards(gov)); story.append(Spacer(1,4*mm))
story.append(two_cards([
    ("First month", "Weekly performance, error, adoption, and improvement review."),
    ("Ongoing", "Monthly outcome review plus immediate notification for critical incidents."),
]))
story += [Spacer(1, 7*mm), P("Change control", H2), P("Configuration changes inside the approved workflow may be included within agreed managed-service limits. Material enhancements—new systems, new authority, new departments, or new responsibilities—will be estimated and approved before implementation."), PageBreak()]

# Page 10
story += section_title("08 / Managed operation", "The AI employee remains managed after launch",
    "The service is designed to prevent Mustard Seed from inheriting another technical system to assemble, monitor, and repair.")
managed = [
    ("Reliability", "Hosting, runtime administration, monitoring, troubleshooting, alerts, and incident response."),
    ("Security", "Credential maintenance, patches, dependency updates, least-privilege reviews, and controlled changes."),
    ("Quality", "Model, prompt, context, routing, workflow, and regression improvements based on observed cases."),
    ("Integration health", "Maintenance when connected services, APIs, or authentication requirements change."),
    ("Business alignment", "Usage and performance reviews with recommendations to narrow, redesign, or expand the responsibility."),
    ("User support", "Support for designated users and process owners within the agreed support level."),
]
for i in range(0,6,2):
    story.append(two_cards(managed[i:i+2])); story.append(Spacer(1,4*mm))
story += [Spacer(1, 5*mm), P("Commercial framework", H2)]
for x in [
    "The final statement of work will specify implementation fees, monthly managed-service fee, included channels, integrations, users, volume, usage limits, and support level.",
    "Existing business software remains Mustard Seed's subscription unless explicitly included.",
    "Premium third-party data, high messaging volume, or unusual infrastructure may be priced separately.",
    "Confidentiality, data-processing, service, payment, transition, and termination terms will be documented before launch.",
]: story.append(bullet(x))
story += [Spacer(1, 8*mm), P("Mustard Seed is not buying a collection of AI subscriptions. It is buying a managed business outcome.", QUOTE), PageBreak()]

# Page 11
story += section_title("09 / Next step", "Confirm the workflow and begin discovery",
    "The recommended Growth Operations AI Employee is a strong starting point, but the discovery session will verify whether it is the highest-value first responsibility.")
next_steps = [
    [P("1", NUM), P("Confirm the first workflow", H3), P("Approve the inquiry-to-follow-up workflow for discovery—or select a more valuable recurring responsibility.", BODY)],
    [P("2", NUM), P("Name the owners", H3), P("Identify the Mustard Seed project owner, sales/marketing process expert, and IT/security representative.", BODY)],
    [P("3", NUM), P("Schedule discovery", H3), P("Hold a focused 90-minute workflow session with representative examples and current performance data.", BODY)],
    [P("4", NUM), P("Finalize scope", H3), P("Approve the workflow, safeguards, success measures, implementation assumptions, and commercial proposal.", BODY)],
    [P("5", NUM), P("Begin implementation", H3), P("Start the six-week build, acceptance, and controlled-launch plan.", BODY)],
]
nt = Table(next_steps, colWidths=[14*mm, 47*mm, 99*mm])
nt.setStyle(TableStyle([
    ("ROWBACKGROUNDS", (0,0), (-1,-1), [WHITE, PALE]), ("LINEBELOW", (0,0), (-1,-2), 0.5, LINE),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"), ("LEFTPADDING", (0,0), (-1,-1), 7),
    ("RIGHTPADDING", (0,0), (-1,-1), 7), ("TOPPADDING", (0,0), (-1,-1), 8), ("BOTTOMPADDING", (0,0), (-1,-1), 8),
]))
story += [nt, Spacer(1, 8*mm), P("Discovery inputs to prepare", H2)]
questions = [
    "Highest-volume and highest-value inquiry channels",
    "Current CRM or system of record and ownership rules",
    "Solution lines that are hardest to route correctly",
    "Response-time expectations and current bottlenecks",
    "Sample normal, duplicate, incomplete, and sensitive inquiries",
    "Approved templates, solution descriptions, FAQs, and policies",
    "Actions and messages requiring human approval",
    "Data that may not be processed by the AI employee",
    "Management reports needed from the workflow",
    "The measurable outcome that would make the pilot clearly worthwhile",
]
qd = []
for i in range(0,10,2):
    qd.append([P("• " + questions[i], TABLE_C), P("• " + questions[i+1], TABLE_C)])
qt = Table(qd, colWidths=[80*mm,80*mm])
qt.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,-1), BLUE_LIGHT), ("GRID", (0,0), (-1,-1), 0.4, WHITE),
    ("VALIGN", (0,0), (-1,-1), "TOP"), ("LEFTPADDING", (0,0), (-1,-1), 8),
    ("RIGHTPADDING", (0,0), (-1,-1), 8), ("TOPPADDING", (0,0), (-1,-1), 7), ("BOTTOMPADDING", (0,0), (-1,-1), 7),
]))
story += [qt, Spacer(1, 9*mm), info_card("Proposed immediate action", "Schedule the 90-minute discovery session and nominate the three Mustard Seed representatives who can confirm business rules, technical access, and approval boundaries."), Spacer(1, 8*mm), P("Prepared by Arnold Gamboa / ArwenDigital", H2), P("Managed AI employees for clearly defined operational work.", BODY), P("Source context: public information reviewed at mseedsystems.com on 20 July 2026. Final scope is subject to discovery and written agreement.", SMALL)]

# Make first page use Cover template, then Body after PageBreak
story.insert(story.index(PageBreak()) + 1 if False else 0, Spacer(1,0))
# BaseDocTemplate uses first template until explicitly changed. Attach NextPageTemplate before first break.
from reportlab.platypus import NextPageTemplate
for idx, item in enumerate(story):
    if isinstance(item, PageBreak):
        story.insert(idx, NextPageTemplate("Body"))
        break

doc.build(story)
print(OUT)
