import re


def fix_spaced_letters(text: str) -> str:
    pattern = r'(?:[A-Za-z]\s){3,}[A-Za-z]'
    
    def repl(match: re.Match) -> str:
        return match.group(0).replace(" ", "")

    return re.sub(pattern, repl, text)


def normalize_whitespace(text: str) -> str:
    text = text.replace("\r", "\n")
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    return text.strip()


def clean_extracted_text(text: str) -> str:
    text = fix_spaced_letters(text)
    text = normalize_whitespace(text)
    return text