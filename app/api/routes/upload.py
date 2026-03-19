from fastapi import APIRouter, File, HTTPException, UploadFile, status

from app.schemas.upload import UploadResponse
from app.services.file_service import save_uploaded_pdf
from app.services.pdf_service import extract_text_from_pdf
from app.services.skill_extractor import extract_skills_from_text
from app.services.text_cleaner import clean_extracted_text

router = APIRouter()


@router.post("/upload-resume", response_model=UploadResponse)
def upload_resume(file: UploadFile = File(...)) -> UploadResponse:
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only PDF files are allowed."
        )

    saved_path = save_uploaded_pdf(file)
    extracted_text = extract_text_from_pdf(saved_path)
    cleaned_text = clean_extracted_text(extracted_text)
    preview = cleaned_text[:500] if cleaned_text else ""
    extracted_skills = extract_skills_from_text(cleaned_text)

    return UploadResponse(
        filename=file.filename,
        content_type=file.content_type,
        saved_path=saved_path,
        extracted_text_preview=preview,
        extracted_skills=extracted_skills,
        message="PDF uploaded and processed successfully."
    )