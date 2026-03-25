def evaluate_rules(prompt: str):
    score = 0

    # Length check
    if len(prompt) > 20:
        score += 2

    # Role check
    if "act as" in prompt.lower():
        score += 2

    # Constraint check
    if "only" in prompt.lower() or "must" in prompt.lower():
        score += 2

    # Structure check
    if ":" in prompt:
        score += 1

    return {
        "rule_score": score,
        "max_rule_score": 7
    }