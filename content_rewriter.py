# app/ai_pipeline/enhancement/content_rewriter.py
import os
import openai

OPENAI_KEY = os.getenv("OPENAI_API_KEY")
openai.api_key = OPENAI_KEY

def rewrite_content(text: str) -> str:
    if not OPENAI_KEY:
        return text  # no-op if no key
    prompt = (
        "Rewrite the following news excerpt into a concise, neutral, factual paragraph. "
        "Preserve facts; do not invent. Maintain 2-3 short sentences.\n\n"
        f"{text}"
    )
    try:
        resp = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # or gpt-4 if available to you
            messages=[{"role":"user","content":prompt}],
            max_tokens=256,
            temperature=0.0
        )
        return resp.choices[0].message.content.strip()
    except Exception as e:
        print("OpenAI rewrite error:", e)
        return text
