from simple_youtube_api.YouTubeVideo import YouTubeVideo
from simple_youtube_api.Channel import Channel
from simple_youtube_api.YouTube import YouTube



with open('developer_key', 'r') as myfile:
    data=myfile.read().replace('\n', '')

developer_key = data
youtube = YouTube()
youtube.login(developer_key)

video = youtube.search_by_video_id("aSw9blXxNJY")

channel = Channel()
channel.login("client_secret.json", "credentials.storage")


video.update(channel, title="hehe")