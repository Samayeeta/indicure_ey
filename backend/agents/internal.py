def run_internal_knowledge_agent(drug: str, indication: str) -> dict:
    """
    Internal Knowledge Agent (Mechanism)
    -----------------------------------
    Inputs:
      - drug: Ranolazine
      - indication: HFpEF

    Working (prototype):
      - In production: internal decks + knowledge graph + mechanistic literature.
      - Here: returns the precise mechanistic rationale you validated.

    Output:
      - Mechanism bullet points + differentiation.
    """
    return {
        "mechanism": [
            "Inhibits late sodium current (INaL) → reduces intracellular Na⁺.",
            "Reduces Ca²⁺ overload → improves diastolic relaxation and filling.",
            "Addresses ionic dysfunction central to HFpEF pathophysiology.",
            "Evidence supports improvements in diastolic indices without BP/HR compromise."
        ],
        "differentiation": "Mechanistically distinct from SGLT2 inhibitors / ARNIs; complements existing therapy."
    }