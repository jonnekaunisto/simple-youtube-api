from simple_youtube_api.Channel import Channel
from simple_youtube_api.LocalVideo import LocalVideo

channel = Channel()
channel.login("client_secret.json", "credentials.storage")

video = LocalVideo(file_path="test_vid.mp4")
print(video.default_language)
#snippet
video.set_title("My Title")
video.set_description("This is a description")
video.set_tags(["this", "tag"])
video.set_category("gaming")
#video.set_default_language("english")

#status
video.set_embeddable(True)
video.set_license("creativeCommon")
video.set_privacy_status("private")
video.set_public_stats_viewable(True)

print(video.default_language)


channel.upload_video(video)