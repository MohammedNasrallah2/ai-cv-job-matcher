from pydantic import BaseModel


class JobAnalysisRequest(BaseModel):
    job_description: str


class JobAnalysisResponse(BaseModel):
    job_description: str
    extracted_job_skills: list[str]