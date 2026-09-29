import sys
import os

# Ensure project root is available for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from enhancer.report_enhancer import enhance_bug_report


def test_enhance_bug_report():
    bug_report = {
        "title": "Login button not                       working",
        "description": "User cannot login after         clicking submit button. Page refreshes.",
        "steps": "Enter username and password then click login",
        "environment": "Chrome Windows 11"
    }

    result = enhance_bug_report(bug_report)

    print("\nEnhanced Report:\n")
    print(result)

    # Basic structure checks
    assert "title" in result
    assert "summary" in result
    assert "structured_report" in result

    assert "problem" in result["structured_report"]
    assert "steps_to_reproduce" in result["structured_report"]
    assert "environment" in result["structured_report"]

    print("\nTest Passed ✅")


if __name__ == "__main__":
    test_enhance_bug_report()