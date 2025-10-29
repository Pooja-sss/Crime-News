# app/ai_pipeline/processing/text_cleaner.py
import re
from bs4 import BeautifulSoup

def clean_html(text: str) -> str:
    if not text:
        return ""
    # remove HTML tags
    soup = BeautifulSoup(text, "html.parser")
    cleaned = soup.get_text(separator=" ", strip=True)
    # remove extra whitespace
    cleaned = re.sub(r"\s+", " ", cleaned)
    return cleaned.strip()
