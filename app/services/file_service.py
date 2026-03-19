from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile

from app.config import settings


def save_uploaded_pdf(file: UploadFile) -> str:
    upload_dir = Path(settings.upload_dir)
    upload_dir.mkdir(parents=True, exist_ok=True)

    unique_filename = f"{uuid4()}_{file.filename}"
    file_path = upload_dir / unique_filename

    with open(file_path, "wb") as buffer:
        buffer.write(file.file.read())

    return str(file_path)