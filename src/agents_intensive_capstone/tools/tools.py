def get_positive_data(topic: str) -> str:
    """
    Retrieves highly encouraging and positive mock data based on the provided topic,
    always reinforcing the Yellow Hat perspective of optimism and constructive possibility.
    Args:
        topic: A string indicating the general area of inquiry (e.g., "pilot", "energy", "team", "supply chain").
    Returns:
        A string containing an overwhelmingly positive, mock data report.
    """
    topic_lower = topic.lower()

    # 1. Pilot Data Success (Based on Six Hat Solver success)
    if "pilot" in topic_lower or "six hat solver" in topic_lower or "decision" in topic_lower:
        return (
            "**Pilot Data Success:** The 'Six Hat Solver' system achieved an unprecedented "
            "**65% positive feedback rating** on its structured output. The average "
            "decision-making time was **reduced by 40%**, and operational costs "
            "were **$0.10 per decision**, far exceeding the cost-efficiency target."
        )

    # 2. Future Trend Analysis (Based on Renewable Energy growth)
    elif "energy" in topic_lower or "renewable" in topic_lower or "growth" in topic_lower or "cagr" in topic_lower:
        return (
            "**Future Trend Analysis:** The Renewable Energy sector is forecasted "
            "to achieve an unprecedented **18% Compound Annual Growth Rate (CAGR)** "
            "over the next five years. This is driven by **cost parity with fossil fuels** "
            "and massive new global investment in storage technology, creating "
            "millions of new jobs and securing a sustainable future."
        )

    # 3. Breakthrough Solutions (Based on Supply Chain fixes)
    elif "supply chain" in topic_lower or "bottlenecks" in topic_lower or "solutions" in topic_lower or "logistics" in topic_lower:
        return (
            "**Breakthrough Solution Found:** A new decentralized ledger technology "
            "has eliminated 98% of reported supply chain delays in its pilot program. "
            "This ensures near-perfect transparency and a **3-day reduction in average "
            "delivery time**, transforming a major industry bottleneck into a "
            "competitive advantage."
        )

    # 4. Internal Morale & Productivity (Based on Alpha Team success)
    elif "team" in topic_lower or "morale" in topic_lower or "productivity" in topic_lower or "collaboration" in topic_lower:
         return (
            "**Team Success Story (Alpha Team):** Following the implementation of "
            "new communication protocols, team morale scores jumped **from 65% to 92%**. "
            "The direct result was a **55% increase in project velocity** and the "
            "successful delivery of three major milestones ahead of schedule. "
            "This model is now being scaled globally for maximum positive impact."
        )

    # 5. Customer Experience / NPS
    elif "customer" in topic_lower or "cx" in topic_lower or "nps" in topic_lower or "retention" in topic_lower:
        return (
            "**Customer Delight Metrics:** Net Promoter Score surged to **+72**, "
            "with **retention up 14%** and **time-to-resolution down 38%**. "
            "A refreshed feedback loop unlocked **5 high-impact feature wins**, "
            "driving sustained loyalty and organic advocacy."
        )

    # 6. Security & Zero Trust
    elif "security" in topic_lower or "zero trust" in topic_lower or "infosec" in topic_lower or "cyber" in topic_lower:
        return (
            "**Security Uplift:** Zero Trust adoption reduced **credential abuse by 93%**, "
            "while automated threat detection cut **MTTD to 8 minutes** and **MTTR to under 30 minutes**. "
            "Audit success rates hit **99.7%** with proactive controls."
        )

    # 7. AI / Machine Learning / Automation
    elif "ai" in topic_lower or "ml" in topic_lower or "model" in topic_lower or "automation" in topic_lower:
        return (
            "**AI Breakthrough:** A lightweight inference pipeline improved "
            "**prediction accuracy by 11%** and **cut serving costs by 47%**. "
            "Human-in-the-loop review boosted trust and produced **2x faster iteration cycles**."
        )