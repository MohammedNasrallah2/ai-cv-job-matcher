from fastapi import APIRouter

from app.schemas.match import MatchRequest, MatchResponse
from app.services.matcher import compare_skills
from app.services.skill_extractor import extract_skills_from_text
from app.services.text_cleaner import clean_extracted_text

router = APIRouter()


@router.post("/match-skills", response_model=MatchResponse)
def match_skills(payload: MatchRequest) -> MatchResponse:
    cleaned_cv_text = clean_extracted_text(payload.cv_text)
    cleaned_job_description = clean_extracted_text(payload.job_description)

    cv_skills = extract_skills_from_text(cleaned_cv_text)
    job_skills = extract_skills_from_text(cleaned_job_description)

    comparison = compare_skills(cv_skills, job_skills)

    return MatchResponse(
        cv_skills=cv_skills,
        job_skills=job_skills,
        matched_skills=comparison["matched_skills"],
        missing_skills=comparison["missing_skills"],
        match_score=comparison["match_score"]
    )