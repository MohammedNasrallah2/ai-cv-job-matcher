from pydantic import BaseModel


class FinalAnalysisResponse(BaseModel):
    filename: str
    cv_skills: list[str]
    job_skills: list[str]
    matched_skills: list[str]
    missing_skills: list[str]
    match_score: float
    recommendation: str