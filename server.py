from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pathlib import Path
import json

app = FastAPI(title="Crime News API")

@app.get("/api/crime-news")
def get_crime_news():
    """Serve the locally saved crime news JSON file."""
    json_path = Path(__file__).parent / "mock_data" / "crime_news_2025-10-29.json"
    if not json_path.exists():
        return JSONResponse(status_code=404, content={"error": "Crime news file not found."})

    with json_path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    return JSONResponse(content=data)

# Optional health check
@app.get("/")
def root():
    return {"message": "Crime News API running successfully 🚀"}
