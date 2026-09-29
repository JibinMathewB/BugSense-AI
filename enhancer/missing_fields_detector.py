# enhancer/report_enhancer.py

import re

def clean_text(text: str) -> str:
    """
    Remove extra whitespace and normalize text formatting.
    Does NOT modify meaning of the text.
    """
    if not text:
        return ""
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def generate_summary(description: str) -> str:
    """
    Create a short summary from the description.
    Uses the first sentence or first ~20 words.
    No hallucination — uses only existing text.
    """
    description = clean_text(description)
    if not description:
        return ""
    sentences = re.split(r"[.!?]", description)
    summary = sentences[0] if sentences else description
    words = summary.split()
    summary = " ".join(words[:20])
    return summary.strip()


def detect_missing_fields(bug_report: dict) -> dict:
    """
    Check which important fields are missing in the bug report.
    Returns a dictionary with field names as keys and True/False.
    """
    required_fields = ["title", "description", "steps", "environment"]
    missing = {field: not bool(bug_report.get(field, "").strip()) for field in required_fields}
    return missing


def enhance_bug_report(bug_report: dict) -> dict:
    """
    Enhance bug report: clean text, generate summary, and detect missing fields.
    Returns a structured report with title, summary, structured details, and missing_fields info.
    """
    title = clean_text(bug_report.get("title", ""))
    description = clean_text(bug_report.get("description", ""))
    steps = clean_text(bug_report.get("steps", ""))
    environment = clean_text(bug_report.get("environment", ""))

    summary = generate_summary(description)
    missing_fields = detect_missing_fields(bug_report)

    enhanced_report = {
        "title": title,
        "summary": summary,
        "structured_report": {
            "problem": title,
            "steps_to_reproduce": steps,
            "environment": environment
        },
        "missing_fields": missing_fields
    }

    return enhanced_report