import praw

reddit = praw.Reddit(client_id="g9NYrjhCNNpP7DvtLR27jA",
                     client_secret="j-hNLqMKcM4PmNPZGVQExuhtPY1rBg",
                     user_agent="Test")

subreddit = reddit.subreddit("technology")
for post in subreddit.hot(limit=10):
    print(post.title)
