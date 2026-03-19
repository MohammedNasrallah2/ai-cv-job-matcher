import re

from app.utils.skills_catalog import SKILLS_CATALOG


SPECIAL_SKILL_PATTERNS = {
    "c": r"(?<![\w+#])c(?![\w+#])",
    "c++": r"(?<!\w)c\+\+(?!\w)",
    "c#": r"(?<!\w)c#(?!\w)",
    "r": r"(?<![\w+#.])r(?![\w+#.])",
    "node.js": r"(?<!\w)node\.js(?!\w)",
    "next.js": r"(?<!\w)next\.js(?!\w)",
    "asp.net": r"(?<!\w)asp\.net(?!\w)",
    "scikit-learn": r"(?<!\w)scikit[-\s]*learn(?!\w)",
    "sklearn": r"(?<!\w)sklearn(?!\w)",
    "tailwind css": r"(?<!\w)tailwind\s+css(?!\w)",
    "oracle database": r"(?<!\w)oracle\s+database(?!\w)",
    "jupyter notebook": r"(?<!\w)jupyter\s+notebook(?!\w)",
    "amazon web services": r"(?<!\w)amazon\s+web\s+services(?!\w)",
    "aws": r"(?<!\w)aws(?!\w)",
    "google cloud": r"(?<!\w)google\s+cloud(?!\w)",
    "gcp": r"(?<!\w)gcp(?!\w)",
    "microsoft azure": r"(?<!\w)microsoft\s+azure(?!\w)",
    "azure": r"(?<!\w)azure(?!\w)",
    "red hat enterprise linux": r"(?<!\w)red\s+hat\s+enterprise\s+linux(?!\w)",
    "linux command line": r"(?<!\w)linux\s+command\s+line(?!\w)",
    "shell scripting": r"(?<!\w)shell\s+scripting(?!\w)",
    "system administration": r"(?<!\w)system\s+administration(?!\w)",
    "data structures": r"(?<!\w)data\s+structures(?!\w)",
    "design patterns": r"(?<!\w)design\s+patterns(?!\w)",
    "api development": r"(?<!\w)api\s+development(?!\w)",
    "restful services": r"(?<!\w)restful\s+services(?!\w)",
    "microservices": r"(?<!\w)microservices(?!\w)",
    "performance optimization": r"(?<!\w)performance\s+optimization(?!\w)",
    "etl pipelines": r"(?<!\w)etl\s+pipelines?(?!\w)",
    "data warehousing": r"(?<!\w)data\s+warehousing(?!\w)",
    "big data processing": r"(?<!\w)big\s+data\s+processing(?!\w)",
    "feature engineering": r"(?<!\w)feature\s+engineering(?!\w)",
    "data cleaning": r"(?<!\w)data\s+cleaning(?!\w)",
    "batch processing": r"(?<!\w)batch\s+processing(?!\w)",
    "streaming systems": r"(?<!\w)streaming\s+systems(?!\w)",
    "apache spark": r"(?<!\w)apache\s+spark(?!\w)",
    "apache hadoop": r"(?<!\w)apache\s+hadoop(?!\w)",
    "apache kafka": r"(?<!\w)apache\s+kafka(?!\w)",
    "secure coding": r"(?<!\w)secure\s+coding(?!\w)",
    "oauth": r"(?<!\w)oauth(?!\w)",
    "jwt": r"(?<!\w)jwt(?!\w)",
    "oop": r"(?<!\w)(oop|object[-\s]*oriented\s+programming)(?!\w)",
    "sql": r"(?<!\w)sql(?!\w)",
    "php": r"(?<!\w)php(?!\w)",
    "go": r"(?<![\w.+#-])go(?![\w.+#-])",
    "git": r"(?<!\w)git(?!\w)",
    "github": r"(?<!\w)github(?!\w)",
    "gitlab": r"(?<!\w)gitlab(?!\w)",
    "jwt": r"(?<!\w)jwt(?!\w)",
}


def normalize_text(text: str) -> str:
    text = text.lower()
    text = text.replace("’", "'")
    text = text.replace("–", "-")
    text = text.replace("—", "-")
    return text


def build_skill_pattern(skill: str) -> str:
    if skill in SPECIAL_SKILL_PATTERNS:
        return SPECIAL_SKILL_PATTERNS[skill]

    escaped_skill = re.escape(skill)
    escaped_skill = escaped_skill.replace(r"\ ", r"\s+")

    return rf"(?<!\w){escaped_skill}(?!\w)"


def cleanup_overlaps(found_skills: set[str]) -> set[str]:
    # remove weaker aliases if stronger canonical names exist
    if "scikit-learn" in found_skills and "sklearn" in found_skills:
        found_skills.discard("sklearn")

    if "amazon web services" in found_skills and "aws" in found_skills:
        found_skills.discard("aws")

    if "google cloud" in found_skills and "gcp" in found_skills:
        found_skills.discard("gcp")

    if "microsoft azure" in found_skills and "azure" in found_skills:
        found_skills.discard("azure")

    return found_skills


def extract_skills_from_text(text: str) -> list[str]:
    normalized_text = normalize_text(text)
    found_skills = []

    for skill in SKILLS_CATALOG:
        pattern = build_skill_pattern(skill)
        if re.search(pattern, normalized_text, flags=re.IGNORECASE):
            found_skills.append(skill)

    normalized_skills = cleanup_overlaps(set(found_skills))

    return sorted(normalized_skills)