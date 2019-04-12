from simple_youtube_api.Channel import Channel
from simple_youtube_api.LocalVideo import LocalVideo

import urllib
import pytest
import os
import datetime

VIDEO_RESOURCE_URL = "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4"
VIDEO_NAME = "test_video.mp4"

def download_video():
    urllib.request.urlretrieve(VIDEO_RESOURCE_URL, VIDEO_NAME) 

def test_channel_regular_function():
    title = "Time: " + datetime.datetime.now()
    download_video()

    channel = Channel()
    channel.login("credentials/client_secret.json", "credentials/credentials.storage")
    video = LocalVideo(file_path=VIDEO_NAME)
    video.set_title(title)
    video.set_description("This is a description")
    video.set_tags(["this", "tag"])
    video.set_category("film")
    video.set_privacy_status("private")

    assert channel.upload_video(video)

if __name__ == "__main__":
    pytest.main()

