import praw
from langdetect import detect
from datetime import datetime

def fetch_reddit_posts(query, limit=100):
    reddit = praw.Reddit(
        client_id="g9NYrjhCNNpP7DvtLR27jA",
        client_secret="j-hNLqMKcM4PmNPZGVQExuhtPY1rBg",
        user_agent="Test"
    )

    posts = reddit.subreddit("all").search(query, limit=limit)
    data = []

    for post in posts:
        content = (post.title or '') + ' ' + (post.selftext or '')
        if content.strip():
            try:
                lang = detect(content)
            except:
                lang = "unknown"

            data.append({
                'source': 'reddit',
                'text': content,
                'lang': lang,
                'query': query,
                'timestamp': datetime.utcnow().isoformat(),
                'sentiment': None
            })

    return data
