from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from agents.report_pdf import build_pdf
from models import AnalyzeRequest, AnalyzeResponse, AgentTraceItem
from agents.master import run_orchestration
from agents.report_pdf import build_pdf
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI(title="IndiCure AI Prototype API", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "https://YOUR-FRONTEND-NAME.onrender.com",
    ],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/analyze", response_model=AnalyzeResponse)
def analyze(req: AnalyzeRequest):
    trace = [
        AgentTraceItem(agent="Master Orchestration Agent", status="completed",
                       note="Parsed query, identified drug/indication/geography."),
        AgentTraceItem(agent="Clinical Trials Agent", status="completed",
                       note="Extracted endpoints and safety signals."),
        AgentTraceItem(agent="Web Intelligence Agent", status="completed",
                       note="Captured India-specific unmet need and guidance gap."),
        AgentTraceItem(agent="Patent Landscape Agent", status="completed",
                       note="Assessed patent/FTO feasibility (prototype)."),
        AgentTraceItem(agent="IQVIA Insights Agent", status="completed",
                       note="Summarized market rationale (prototype)."),
        AgentTraceItem(agent="Internal Knowledge Agent", status="completed",
                       note="Produced mechanistic rationale and differentiation."),
        AgentTraceItem(agent="Report Generator Agent", status="completed",
                       note="Assembled dashboard fields and export-ready report."),
    ]

    report = run_orchestration(req.query, req.geography)

    return {
        "normalized": report["normalized"],
        "trace": trace,
        "executive_summary": report["executive_summary"],
        "evidence": report["evidence"],
        "unmet_need": report["unmet_need"],
        "risk_feasibility": report["risk_feasibility"],
        "recommendation": report["recommendation"],
        "references": report["references"],
    }

@app.post("/export/pdf")
def export_pdf(req: AnalyzeRequest):
    report = run_orchestration(req.query, req.geography)

    if getattr(req, "analysis_mode", None):
        report["analysis_mode"] = req.analysis_mode

    pdf_bytes = build_pdf(report)

    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={"Content-Disposition": 'attachment; filename="indicure_ranolazine_report.pdf"'},
    )

@app.get("/api/report/pdf")
def report_pdf(mode: str = "General", geo: str = "India"):
    report = run_orchestration(
        "Assess repurposing potential of Ranolazine for HFpEF",
        geo,
    )

    report["analysis_mode"] = mode

    pdf_bytes = build_pdf(report)

    return Response(
        content=pdf_bytes,
        media_type="application/pdf",
        headers={
            "Content-Disposition": f'attachment; filename="IndiCure_Ranolazine_HFpEF_{geo}_{mode}.pdf"'
        },
    )

