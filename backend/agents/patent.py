def run_patent_landscape_agent(drug: str, indication: str) -> dict:
    """
    Patent Landscape Agent
    ----------------------
    Inputs:
      - drug: Ranolazine
      - indication: HFpEF

    Working (prototype):
      - In production: PatentScope/Google Patents + expiry + FTO evaluation.
      - Here: deterministic, demo-safe conclusion consistent with your narrative.

    Output:
      - Patent status + FTO risk + path forward.
    """
    return {
        "status": "Off-patent / near-expiry positioning (prototype assumption for demo).",
        "hfpef_claim_density": "HFpEF-specific claims appear limited in high-level scan (prototype).",
        "fto_risk": "Low (prototype).",
        "feasibility": "Repurposing feasible via indication extension + evidence-backed labeling strategy."
    }