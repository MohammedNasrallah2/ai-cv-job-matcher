import re


PRIORITY_KEYWORDS = [
    "requirements",
    "required skills",
    "qualifications",
    "preferred qualifications",
    "skills",
    "must have",
    "nice to have",
    "what you will bring",
    "what we're looking for",
    "job requirements",
    "technical skills",
]


def normalize_job_text(text: str) -> str:
    text = text.replace("\r", "\n")
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    return text.strip()


def extract_priority_sections(text: str) -> str:
    normalized = normalize_job_text(text)
    lowered = normalized.lower()

    matched_sections = []

    for keyword in PRIORITY_KEYWORDS:
        pattern = rf"{re.escape(keyword)}\s*:?(.*?)(?=\n[A-Z][^\n]{{0,80}}:|\n\n|\Z)"
        matches = re.findall(pattern, lowered, flags=re.IGNORECASE | re.DOTALL)
        matched_sections.extend(matches)

    if matched_sections:
        joined = "\n".join(section.strip() for section in matched_sections if section.strip())
        return joined.strip()

    return normalized


def prepare_job_description_for_extraction(text: str) -> str:
    return extract_priority_sections(text)