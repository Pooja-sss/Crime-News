# app/ai_pipeline/processing/impact_scorer.py
from datetime import datetime
def score_article(article: dict) -> float:
    # simple heuristic: longer content + presence of key tokens + recency
    content = article.get("content", "") or ""
    title = article.get("title","")
    score = len(content.split()) / 100.0
    for token in ["murder","multiple","dead","attack","police"]:
        if token in (title+content).lower():
            score += 1.0
    # recency boost (published_at expected ISO)
    try:
        pub = datetime.fromisoformat(article.get("published_at").replace("Z","+00:00"))
        age_days = (datetime.utcnow() - pub).days
        score += max(0, 3 - age_days) * 0.5
    except Exception:
        pass
    return round(score, 3)
