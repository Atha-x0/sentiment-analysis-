# from fetch_tweets import fetch_tweets
from fetch_reddit import fetch_reddit_posts
from fetch_news import fetch_google_news
from fetch_youtube import fetch_youtube_comments
from fetch_social_mock import fetch_instagram, fetch_facebook

from sentiment_analysis import analyze_sentiment
import json
import os

def main():
    topic = input("🔍 Enter trending topic: ")
    
    # Step 1: Collect data from multiple platforms
    # twitter_data = fetch_tweets(topic, max_results=50)
    news_data = fetch_google_news(topic, num_articles=20)
    youtube_data = fetch_youtube_comments(topic, max_results=5)
    insta_data = fetch_instagram(topic)
    fb_data = fetch_facebook(topic)
    reddit_data = fetch_reddit_posts(topic, limit=50)
    

    # Combine all data
    all_data = reddit_data + news_data + youtube_data + insta_data + fb_data 

    # Step 2: Analyze sentiment
    for item in all_data:
        item['sentiment'] = analyze_sentiment(item['text'])

    # Step 3: Prepare data folder
    os.makedirs("data", exist_ok=True)
    file_path = "data/collected_data.json"

    # Step 4: Append new data to existing JSON
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            try:
                existing_data = json.load(f)
            except json.JSONDecodeError:
                existing_data = []
    else:
        existing_data = []

    # Combine new + old
    combined_data =  all_data #+ existing_data

    # Step 5: Save to file
    with open(file_path, "w") as f:
        json.dump(combined_data, f, indent=2)

    print(f"✅ Data collected and saved to: {file_path}")

if __name__ == "__main__":
    main()
