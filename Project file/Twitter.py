# fetch_tweets.py
import tweepy

def fetch_tweets(query, max_results=50):
    BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAIsM1QEAAAAAEfVyZ4WdDmydiKEhi7aA%2F3wPsoM%3DcqyUL2EoAOlUQCOkMA12xPjjcErFmqjwYI493wfIv61myl7tzf'  # Replace this!

    client = tweepy.Client(bearer_token=BEARER_TOKEN)

    tweets = client.search_recent_tweets(query=query, max_results=max_results, tweet_fields=['text', 'lang'])

    tweet_data = []
    if tweets.data:
        for tweet in tweets.data:
            if tweet.lang == 'en':  # Only English tweets
                tweet_data.append({'source': 'twitter', 'text': tweet.text})

    return tweet_data
