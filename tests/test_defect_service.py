import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from services.defect_service import process_new_bugs

existing_bugs = [
    "Login page crashes when clicking submit",
    "Payment gateway timeout error"
]

new_bugs = [
    "Submit button crashes login page",
    "Payment fails due to timeout",
    "UI color not loading"
]

results = process_new_bugs(new_bugs, existing_bugs)

for r in results:
    print(r)