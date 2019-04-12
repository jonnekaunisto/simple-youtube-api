from simple_youtube_api.Channel import Channel
from simple_youtube_api.Video import Video

import urllib.request

import pytest
import os

VIDEO_RESOURCE_URL = "http://commondatastorage.googleapis.com/gtv-videos-bucket/sample/ForBiggerBlazes.mp4"

def download_video():
    urllib.request.urlretrieve(url_link, VIDEO_RESOURCE_URL) 

def test_channel_regular_function():
    channel = Channel()
    channel.login("credentials/client_secret.json", "credentials/credentials.storage")
    video = Video(file_path="ForBiggerBlazes.mp4")
    video.set_title("This is a title")
    video.set_description("This is a description")
    video.set_tags(["this", "tag"])
    video.set_category("film")
    video.set_privacy_status("private")

    assert channel.upload_video(video)

if __name__ == "__main__":
    pytest.main()

