import re
from agents.clinical import run_clinical_trials_agent
from agents.web import run_web_intelligence_agent
from agents.patent import run_patent_landscape_agent
from agents.iqvia import run_iqvia_insights_agent
from agents.internal import run_internal_knowledge_agent

def normalize_query(query: str) -> dict:
    """
    Master Orchestration Agent — parsing/normalization.
    Extracts: drug, current use, target indication, geography.
    For the prototype, we default to Ranolazine/HFpEF/India unless clearly overridden.
    """
    q = query.lower()
    drug = "Ranolazine" if "ranolazine" in q else "Ranolazine"  # demo locked
    indication = "HFpEF" if ("hfpef" in q or "preserved ejection" in q or "diastolic" in q) else "HFpEF"
    geography = "India" if ("india" in q or "indian" in q) else "India"
    current_use = "Chronic stable angina / ischaemic heart disease"
    return {
        "drug": drug,
        "current_use": current_use,
        "repurposing_target": indication,
        "geography": geography
    }

def run_orchestration(query: str, geography: str) -> dict:
    """
    Master Orchestration Agent — delegation + aggregation.
    Calls 5 worker agents and aggregates outputs into a report-ready structure.
    """
    norm = normalize_query(query)
    drug = norm["drug"]
    indication = norm["repurposing_target"]

    clinical = run_clinical_trials_agent(drug, indication)
    web = run_web_intelligence_agent(geography, indication)
    patent = run_patent_landscape_agent(drug, indication)
    market = run_iqvia_insights_agent(geography, indication)
    internal = run_internal_knowledge_agent(drug, indication)

    executive_summary = (
        "Ranolazine, approved for chronic angina, demonstrates strong mechanistic and clinical potential "
        "for repurposing in HFpEF: a major, undertreated cardiac condition in India. "
        "Clinical evidence shows statistically significant improvement in diastolic indices without "
        "hemodynamic compromise. Given the therapy gap in Indian HFpEF guidance and Ranolazine’s favorable "
        "safety and cost profile, it is a viable mechanism-driven repurposing candidate."
    )

    risk_feasibility = {
        "patent_risk": patent["fto_risk"],
        "patent_notes": patent["status"],
        "regulatory_path": "Supplemental indication pathway (conceptual; depends on regulator and evidence).",
        "cost_profile": "Favorable (repurposed small molecule).",
        "market_notes": market
    }

    recommendation = (
        "Proceed with targeted Phase II/III Indian clinical trials evaluating Ranolazine as an adjunct therapy "
        "for HFpEF, prioritizing diastolic function endpoints (E/E′, LVEDV), symptoms/quality of life, and "
        "hospitalization reduction; stratify patients by phenotype and comorbidities."
    )

    references = [
        {"title": "HFpEF Guidelines (JAPI 2022)", "url": "https://heartfailure.org.in/assets/Uploads/guidelines/HFPEF_Guidelines_JAPI_2022.pdf"},
        {"title": "HFpEF India Review (2025)", "url": "https://journals.lww.com/jicc/fulltext/2025/04000/heart_failure_with_preserved_ejection_fraction_in.2.aspx"},
        {"title": "Clinical evidence summary (HFpEF/Ranolazine meta-analysis)", "url": "https://pmc.ncbi.nlm.nih.gov/articles/PMC9947928/"},
        {"title": "Ranolazine mechanism overview (AJC abstract)", "url": "https://www.ajconline.org/article/S0002-9149(23)01060-3/abstract"},
        {"title": "RALI-DHF proof-of-concept (JACC HF 2013)", "url": "https://www.sciencedirect.com/science/article/pii/S2213177913000383"}
    ]

    return {
        "normalized": norm,
        "agents": {
            "Clinical Trials Agent": clinical,
            "Web Intelligence Agent": web,
            "Patent Landscape Agent": patent,
            "IQVIA Insights Agent": market,
            "Internal Knowledge Agent": internal
        },
        "executive_summary": executive_summary,
        "evidence": {
            "clinical": clinical,
            "mechanism": internal
        },
        "unmet_need": web,
        "risk_feasibility": risk_feasibility,
        "recommendation": recommendation,
        "references": references
    }