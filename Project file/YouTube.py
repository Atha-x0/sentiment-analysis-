from googleapiclient.discovery import build

youtube = build("youtube", "v3", developerKey="AIzaSyA6-En-X4lvzlbVNRApUsFTModwFMAzNIk")
request = youtube.commentThreads().list(
    part="snippet", videoId="VIDEO_ID", maxResults=10)
response = request.execute()

for item in response["items"]:
    comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
    print(comment)
