# enhancer/report_enhancer.py

import re

def clean_text(text: str) -> str:
    """
    Remove extra whitespace and normalize text formatting.
    Does NOT modify meaning of the text.
    """
    if not text:
        return ""

    # Replace multiple spaces/newlines/tabs with single space
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

    # Split sentences
    sentences = re.split(r"[.!?]", description)

    # Take the first sentence if available
    summary = sentences[0] if sentences else description

    # Limit summary length to ~20 words
    words = summary.split()
    summary = " ".join(words[:20])

    return summary.strip()


def enhance_bug_report(bug_report: dict) -> dict:
    """
    Improve the structure of a bug report without inventing data.
    Returns a dictionary with title, summary, and structured_report.
    """
    title = clean_text(bug_report.get("title", ""))
    description = clean_text(bug_report.get("description", ""))
    steps = clean_text(bug_report.get("steps", ""))
    environment = clean_text(bug_report.get("environment", ""))

    summary = generate_summary(description)

    enhanced_report = {
        "title": title,
        "summary": summary,
        "structured_report": {
            "problem": title,
            "steps_to_reproduce": steps,
            "environment": environment
        }
    }

    return enhanced_report