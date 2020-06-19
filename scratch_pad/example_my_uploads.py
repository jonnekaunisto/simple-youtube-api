from simple_youtube_api.Channel import Channel
from simple_youtube_api.YouTubeVideo import YouTubeVideo


channel = Channel()
channel.login("client_secret.json", "credentials.storage")
videos = channel.fetch_uploads()

for video in videos:
    print(video.title)
