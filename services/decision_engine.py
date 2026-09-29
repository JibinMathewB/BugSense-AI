def classify_bug(score: float):
    """
    Convert similarity score into bug classification.

    Args:
        score (float): similarity score from FAISS search

    Returns:
        tuple:
            decision (str)
            confidence (str)
    """

    if score is None:
        return "new_defect", "low"

    try:
        score = float(score)
    except (TypeError, ValueError):
        return "new_defect", "low"

    if score >= 0.90:
        return "duplicate", "high"

    elif score >= 0.75:
        return "possible_duplicate", "medium"

    else:
        return "new_defect", "low"