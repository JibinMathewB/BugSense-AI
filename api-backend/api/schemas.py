from pydantic import BaseModel, Field
from typing import List


class BugRequest(BaseModel):
    title: str = Field(..., description="Bug title")
    description: str = Field(..., description="Detailed bug description")
    steps: str = Field(..., description="Steps to reproduce the issue")
    environment: str = Field(..., description="Browser/OS/environment information")


class Match(BaseModel):
    bug_id: int = Field(..., description="ID of similar bug")
    score: float = Field(..., description="Similarity score with query bug")


class ImprovedReport(BaseModel):
    title: str = Field(..., description="Improved bug title")
    summary: str = Field(..., description="AI-generated bug summary")


class BugResponse(BaseModel):
    decision: str = Field(..., description="duplicate | possible_duplicate | new_defect")
    confidence: str = Field(..., description="high | medium | low confidence")
    cluster_id: str = Field(..., description="Cluster identifier for related bugs")
    top_matches: List[Match] = Field(..., description="Top similar bugs retrieved from vector search")
    improved_report: ImprovedReport = Field(..., description="Enhanced bug report structure")