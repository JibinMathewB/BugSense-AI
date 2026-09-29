import os
import importlib.util

# Load the sibling `services/defect_service.py` explicitly by file path
# to avoid ambiguous top-level `services` packages in the workspace.
parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
service_path = os.path.join(parent_dir, "services", "defect_service.py")
spec = importlib.util.spec_from_file_location("api_backend_defect_service", service_path)
_svc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(_svc)
# expose the analyze_bug function from the loaded module
analyze_bug = getattr(_svc, "analyze_bug")

from fastapi import APIRouter, HTTPException
from .schemas import BugRequest, BugResponse
from .response_builder import build_response

router = APIRouter()


@router.get("/health")
def health():
    """
    Health check endpoint to verify API is running.
    """
    return {"status": "ok"}


@router.post("/check-defect", response_model=BugResponse)
def check_defect(request: BugRequest):
    """
    Analyze a new bug report and determine if it is
    a duplicate, possible duplicate, or new defect.
    """

    try:
        # Run bug analysis
        result = analyze_bug(request)

        # Build structured API response
        response = build_response(result)

        return response

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))