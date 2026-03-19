from pathlib import Path

from pypdf import PdfReader


def extract_text_from_pdf(file_path: str) -> str:
    path = Path(file_path)

    reader = PdfReader(path)
    extracted_text_parts = []

    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            extracted_text_parts.append(page_text)

    return "\n".join(extracted_text_parts).strip()