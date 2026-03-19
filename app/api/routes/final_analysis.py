from fastapi import APIRouter, File, Form, HTTPException, UploadFile, status

from app.ai.graph import match_graph
from app.schemas.final_analysis import FinalAnalysisResponse
from app.services.file_service import save_uploaded_pdf
from app.services.pdf_service import extract_text_from_pdf

router = APIRouter()


@router.post("/analyze-resume-match", response_model=FinalAnalysisResponse)
def analyze_resume_match(
    file: UploadFile = File(...),
    job_description: str = Form(...)
) -> FinalAnalysisResponse:
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only PDF files are allowed."
        )

    saved_path = save_uploaded_pdf(file)
    extracted_text = extract_text_from_pdf(saved_path)

    result = match_graph.invoke({
        "filename": file.filename,
        "cv_text": extracted_text,
        "job_description": job_description,
    })

    return FinalAnalysisResponse(
        filename=result["filename"],
        cv_skills=result["cv_skills"],
        job_skills=result["job_skills"],
        matched_skills=result["matched_skills"],
        missing_skills=result["missing_skills"],
        match_score=result["match_score"],
        recommendation=result["recommendation"],
    )