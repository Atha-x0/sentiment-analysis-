from langdetect import detect
from datetime import datetime

def fetch_instagram(query):
    posts = [
        f"{query} is lit 🔥🔥🔥",
        f"Mixed feelings about {query}."
    ]

    data = []
    for text in posts:
        try:
            lang = detect(text)
        except:
            lang = "unknown"

        data.append({
            "source": "instagram",
            "text": text,
            "lang": lang,
            "query": query,
            "timestamp": datetime.utcnow().isoformat(),
            "sentiment": None
        })

    return data

def fetch_facebook(query):
    posts = [
        f"{query} memories from last year!",
        f"Not enjoying {query} this time."
    ]

    data = []
    for text in posts:
        try:
            lang = detect(text)
        except:
            lang = "unknown"

        data.append({
            "source": "facebook",
            "text": text,
            "lang": lang,
            "query": query,
            "timestamp": datetime.utcnow().isoformat(),
            "sentiment": None
        })

    return data
