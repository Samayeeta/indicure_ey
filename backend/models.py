from pydantic import BaseModel, Field
from typing import Dict, Any, List, Literal, Optional

Mode = Literal["General", "Clinical", "Patent", "Market"]
OutputFormat = Literal["Summary + Risks + Recommendation"]
Geography = Literal["India"]

class AnalyzeRequest(BaseModel):
    query: str = Field(min_length=10)
    mode: Mode = "General"
    output_format: OutputFormat = "Summary + Risks + Recommendation"
    geography: Geography = "India"

class AgentTraceItem(BaseModel):
    agent: str
    status: Literal["queued", "running", "completed"]
    note: str

class AnalyzeResponse(BaseModel):
    normalized: Dict[str, Any]
    trace: List[AgentTraceItem]
    executive_summary: str
    evidence: Dict[str, Any]
    unmet_need: Dict[str, Any]
    risk_feasibility: Dict[str, Any]
    recommendation: str
    references: List[Dict[str, str]]