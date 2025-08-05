from GoogleNews import GoogleNews
from datetime import datetime

def fetch_google_news(query, num_articles=10, languages=['en']):
    all_results = []

    for lang in languages:
        googlenews = GoogleNews(lang=lang)
        googlenews.search(query)
        results = googlenews.result()[:num_articles]

        for item in results:
            all_results.append({
                "source": f"google_news_{lang}",
                "text": item.get("title", ""),
                "lang": lang,
                "query": query,
                "timestamp": datetime.utcnow().isoformat(),
                "sentiment": None
            })

    return all_results
