def generate_confidence(score: float) -> str:
    """
    Convert similarity score into confidence level.

    Args:
        score: similarity score from FAISS (0 to 1)

    Returns:
        confidence level: high / medium / low
    """

    if score is None:
        return "low"

    try:
        score = float(score)
    except (TypeError, ValueError):
        return "low"

    if score >= 0.90:
        return "high"

    elif score >= 0.75:
        return "medium"

    else:
        return "low"