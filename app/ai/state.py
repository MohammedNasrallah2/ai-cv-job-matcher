from typing import TypedDict


class MatchState(TypedDict, total=False):
    filename: str
    cv_text: str
    job_description: str
    prepared_job_description: str
    cv_skills: list[str]
    job_skills: list[str]
    matched_skills: list[str]
    missing_skills: list[str]
    match_score: float
    recommendation: str