from GoogleNews import GoogleNews

def fetch_google_news(query, num_articles=10):
    googlenews = GoogleNews(lang='en')
    googlenews.search(query)
    results = googlenews.result()[:num_articles]

    data = [{"source": "google_news", "text": item["title"]} for item in results]
    
    return data
