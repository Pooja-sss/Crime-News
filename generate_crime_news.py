# app/ai_pipeline/mock_data/generate_crime_news.py
import json
from datetime import datetime
from pathlib import Path

OUT_DIR = Path(__file__).parent
OUT_FILE = OUT_DIR / f"crime_news_{datetime.utcnow().date()}.json"

# Example articles - replace or extend these entries
crime_articles = [
    {
        "source": {"id": "local-press", "name": "Local Press"},
        "author": "Aman Verma",
        "title": "Police arrest cyber-fraud gang targeting online shoppers",
        "description": "District police arrested four suspects linked to online payment frauds.",
        "url": "https://localpress.example.com/cyber-fraud-arrests",
        "urlToImage": "https://localpress.example.com/images/cyber-fraud.jpg",
        "publishedAt": datetime.utcnow().isoformat() + "Z",
        "content": "Police investigation uncovered a phishing ring operating across multiple states..."
    },
    {
        "source": {"id": "city-times", "name": "City Times"},
        "author": "Rita Singh",
        "title": "Spike in vehicle thefts near transit hubs — police advise precautions",
        "description": "Transit authorities and police increase patrols after rise in vehicle thefts.",
        "url": "https://citytimes.example.com/vehicle-thefts-2025",
        "urlToImage": "https://citytimes.example.com/images/vehicle-theft.jpg",
        "publishedAt": datetime.utcnow().isoformat() + "Z",
        "content": "Local police urge commuters to avoid leaving valuables visible inside parked vehicles..."
    }
]

payload = {
    "status": "ok",
    "totalResults": len(crime_articles),
    "articles": crime_articles
}

def main():
    with OUT_FILE.open("w", encoding="utf-8") as f:
        json.dump(payload, f, indent=2, ensure_ascii=False)
    print(f"✅ Created fallback file: {OUT_FILE}")

if __name__ == "__main__":
    main()
