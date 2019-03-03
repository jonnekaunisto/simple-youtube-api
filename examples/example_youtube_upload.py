from simple_youtube_api.Channel import Channel
from simple_youtube_api.Video import Video

channel = Channel()
channel.login("client_secret.json", "credentials.storage")

video = Video(file_path="test_vid.mp4")
video.set_title("This is a title")
video.set_description("This is a description")
video.set_tags(["this", "tag"])
video.set_category("film")
video.set_privacy_status("private")

channel.upload_video(video)
