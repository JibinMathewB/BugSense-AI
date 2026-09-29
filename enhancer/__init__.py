# enhancer/__init__.py

# Expose key functions at the package level
from .report_enhancer import enhance_bug_report, generate_summary, clean_text
from .missing_fields_detector import detect_missing_fields

__all__ = [
    "enhance_bug_report",
    "generate_summary",
    "clean_text",
    "detect_missing_fields"
]