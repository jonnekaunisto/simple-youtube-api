from simple_youtube_api import Channel

ch = Channel()


ch.login("client_secret.json", "credentials.storage")
vid = Video.Video()
ch.upload_video(vid)
