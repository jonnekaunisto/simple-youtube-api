from simple_youtube_api.Channel import Channel
from simple_youtube_api.Video import Video

ch = Channel()


ch.login("client_secret.json", "credentials.storage")
video = Video()
#ch.upload_video(video)
