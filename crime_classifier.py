# app/ai_pipeline/processing/crime_classifier.py
from typing import Dict
# naive keyword-based classifier (replace with model later)
CRIME_KEYWORDS = ["murder", "robbery", "rape", "assault", "police", "arrest", "theft", "kidnap", "shooting"]

def is_crime_article(article: Dict) -> bool:
    text = " ".join(filter(None, [article.get("title",""), article.get("content","")])).lower()
    return any(k in text for k in CRIME_KEYWORDS)
