from fastapi import APIRouter

from app.schemas.analysis import JobAnalysisRequest, JobAnalysisResponse
from app.services.job_text_processor import prepare_job_description_for_extraction
from app.services.skill_extractor import extract_skills_from_text
from app.services.text_cleaner import clean_extracted_text

router = APIRouter()


@router.post("/analyze-job", response_model=JobAnalysisResponse)
def analyze_job_description(payload: JobAnalysisRequest) -> JobAnalysisResponse:
    cleaned_job_description = clean_extracted_text(payload.job_description)
    prepared_job_description = prepare_job_description_for_extraction(cleaned_job_description)
    extracted_job_skills = extract_skills_from_text(prepared_job_description)

    return JobAnalysisResponse(
        job_description=prepared_job_description,
        extracted_job_skills=extracted_job_skills
    )