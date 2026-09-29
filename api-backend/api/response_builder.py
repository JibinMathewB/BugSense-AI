def build_response(result):
    """
    Convert internal service result into API response format
    expected by the frontend.
    """

    response = {
        "decision": result.get("decision", "new_defect"),
        "confidence": result.get("confidence", "low"),
        "cluster_id": result.get("cluster_id", "cluster_new"),
        "top_matches": result.get("top_matches", []),
        "improved_report": {
            "title": result.get("improved_title", ""),
            "summary": result.get("improved_summary", "")
        }
    }

    return response