import praw

def fetch_reddit_posts(query, limit=100):
    reddit = praw.Reddit(
        client_id="g9NYrjhCNNpP7DvtLR27jA",
        client_secret="j-hNLqMKcM4PmNPZGVQExuhtPY1rBg",
        user_agent="Test"
    )

    posts = reddit.subreddit("all").search(query, limit=limit)
    data = []

    for post in posts:
        content = post.title + ' ' + post.selftext
        if content:
            data.append({'source': 'reddit', 'text': content})

    return data
