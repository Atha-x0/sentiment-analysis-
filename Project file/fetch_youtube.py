from googleapiclient.discovery import build
from langdetect import detect
from datetime import datetime

def fetch_youtube_comments(query, max_results=10):
    api_key = "AIzaSyA6-En-X4lvzlbVNRApUsFTModwFMAzNIk"
    youtube = build("youtube", "v3", developerKey=api_key)

    search = youtube.search().list(q=query, part="snippet", type="video", maxResults=max_results).execute()

    data = []
    for item in search['items']:
        video_id = item['id']['videoId']
        comment_response = youtube.commentThreads().list(
            part="snippet", videoId=video_id, textFormat="plainText", maxResults=5
        ).execute()

        for comment in comment_response.get("items", []):
            text = comment["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            try:
                lang = detect(text)
            except:
                lang = "unknown"

            data.append({
                "source": "youtube",
                "text": text,
                "lang": lang,
                "query": query,
                "timestamp": datetime.utcnow().isoformat(),
                "sentiment": None
            })

    return data

