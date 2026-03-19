from pydantic import BaseModel


class MatchRequest(BaseModel):
    cv_text: str
    job_description: str


class MatchResponse(BaseModel):
    cv_skills: list[str]
    job_skills: list[str]
    matched_skills: list[str]
    missing_skills: list[str]
    match_score: float