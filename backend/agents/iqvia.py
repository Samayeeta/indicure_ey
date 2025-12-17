def run_iqvia_insights_agent(geography: str, indication: str) -> dict:
    """
    IQVIA Insights Agent (Market)
    ----------------------------
    Inputs:
      - geography: India
      - indication: HFpEF

    Working (prototype):
      - In production: IQVIA/market datasets + CAGR + therapy adoption.
      - Here: returns directional market rationale consistent with your demo story.

    Output:
      - Market trend + patient gap + commercial rationale.
    """
    return {
        "market_trend": "Growing HF burden in India driven by aging, diabetes, and lifestyle risk factors.",
        "patient_gap": "Large underdiagnosed population suggests significant screening and treatment opportunity.",
        "commercial_rationale": "Affordable repurposed therapy could fit unmet need and resource constraints."
    }