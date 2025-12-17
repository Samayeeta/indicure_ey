def run_web_intelligence_agent(geography: str, indication: str) -> dict:
    """
    Web Intelligence Agent
    ----------------------
    Inputs:
      - geography: "India"
      - indication: "HFpEF"

    Working (prototype):
      - In production, this agent would crawl guideline PDFs + trusted reviews.
      - Here, it returns the India-specific unmet need signals you already validated.

    Output:
      - Prevalence, mortality, current therapy gap, urgency.
    """
    return {
        "india_burden": [
            "HFpEF accounts for ~15–30% of HF cases in India.",
            "High burden with ~40% mortality at ~3 years in reported cohorts.",
            "Underdiagnosed and increasing prevalence."
        ],
        "guideline_gap": [
            "Only SGLT2 inhibitors have proven benefit in HFpEF.",
            "No single curative/disease-modifying drug established.",
            "Ionic dysfunction (Na⁺/Ca²⁺ handling) central to HFpEF pathophysiology."
        ],
        "implication": "Clear therapeutic gap supports mechanism-driven repurposing candidates."
    }