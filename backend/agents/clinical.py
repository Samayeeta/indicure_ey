def run_clinical_trials_agent(drug: str, indication: str) -> dict:
    """
    Clinical Trials Agent
    --------------------
    Inputs:
      - drug: "Ranolazine"
      - indication: "HFpEF"

    Working (prototype):
      - In production, this agent would query: CTRI/NIH ClinicalTrials + PubMed.
      - Here, we return curated evidence for Ranolazine → HFpEF, aligned with your validated notes.

    Output:
      - Key endpoints + statistical significance + safety summary.
    """
    return {
        "key_findings": [
            "Improved diastolic performance (↑ LVEDV, ↓ E/E′).",
            "No significant adverse hemodynamic changes (BP/HR/QT).",
            "Likely symptom/quality-of-life benefit in HFpEF context."
        ],
        "endpoints": [
            {"metric": "LVEDV", "result": "↑ (mean diff ~33.34 ml)", "significance": "p < 0.001"},
            {"metric": "E/E′", "result": "↓ (mean diff ~0.45)", "significance": "p = 0.05"},
            {"metric": "Peak O₂", "result": "trend ↑", "significance": "p = 0.09 (NS)"},
            {"metric": "Exercise duration", "result": "trend ↑", "significance": "p = 0.18 (NS)"},
            {"metric": "BP/HR", "result": "no difference", "significance": "p > 0.05"},
            {"metric": "QT interval", "result": "no difference", "significance": "p = 0.27"}
        ],
        "safety": "Favorable safety profile; adverse effects mild and comparable to placebo."
    }