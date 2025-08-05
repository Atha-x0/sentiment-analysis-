# fetch_tweets.py
import tweepy
from datetime import datetime
from langdetect import detect

def fetch_tweets(query, max_results=50):
    BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAIsM1QEAAAAAEfVyZ4WdDmydiKEhi7aA%2F3wPsoM%3DcqyUL2EoAOlUQCOkMA12xPjjcErFmqjwYI493wfIv61myl7tzf'  # Replace if necessary

    client = tweepy.Client(bearer_token=BEARER_TOKEN)

    response = client.search_recent_tweets(
        query=query,
        max_results=max_results,
        tweet_fields=['text', 'lang', 'created_at']
    )

    data = []
    if response.data:
        for tweet in response.data:
            text = tweet.text
            try:
                lang = tweet.lang if tweet.lang else detect(text)
            except:
                lang = "unknown"

            data.append({
                "source": "twitter",
                "text": text,
                "lang": lang,
                "query": query,
                "timestamp": tweet.created_at.isoformat() if tweet.created_at else datetime.utcnow().isoformat(),
                "sentiment": None
            })

    return data
