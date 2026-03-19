from pydantic import BaseModel


class UploadResponse(BaseModel):
    filename: str
    content_type: str
    saved_path: str
    extracted_text_preview: str
    extracted_skills: list[str]
    message: str