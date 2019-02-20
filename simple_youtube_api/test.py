import Channel, Video

ch = Channel.Channel()


ch.login("client_secret.json", "credentials.storage")
vid = Video.Video()
ch.upload_video(vid)
