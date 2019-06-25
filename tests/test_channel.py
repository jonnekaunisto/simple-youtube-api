from simple_youtube_api.Channel import Channel
from simple_youtube_api.LocalVideo import LocalVideo

import urllib
import pytest
import os
import datetime

VIDEO_RESOURCE_URL = "http://commondatastorage.googleapis.com/ \
                      gtv-videos-bucket/sample/ForBiggerBlazes.mp4"
VIDEO_NAME = "test_video.mp4"
CLIENT_SECRET_NAME = "credentials/client_secret.json"
CREDENTIALS = "credentials/credentials.storage"


def download_video():
    urllib.request.urlretrieve(VIDEO_RESOURCE_URL, VIDEO_NAME) 


def test_channel_regular_function():
    channel = Channel()


def test_channel_fetch_uploads():
    channel = Channel()

    assert os.path.isfile(CLIENT_SECRET_NAME), "CLIENT SECRET_NAME not valid"

    assert os.path.isfile(CREDENTIALS), "CREDENTIALS is not valid"

    channel.login(CLIENT_SECRET_NAME, CREDENTIALS)

    videos = channel.fetch_uploads()

    for video in videos:
        print(video.get_title())


def not_working_channel_upload_video():
    channel = Channel()
    '''
    testing this will make too many requests to google which will go over the
    query quota
    '''

    assert os.path.isfile(CLIENT_SECRET_NAME), "CLIENT SECRET_NAME not valid"
    assert os.path.isfile(CREDENTIALS), "CREDENTIALS is not valid"

    title = "Time: " + str(datetime.datetime.now())
    download_video()

    channel.login(CLIENT_SECRET_NAME, CREDENTIALS)
    video = LocalVideo(file_path=VIDEO_NAME)
    video.set_title(title)
    video.set_description("This is a description")
    video.set_tags(["this", "tag"])
    video.set_category("film")
    video.set_privacy_status("private")

    assert channel.upload_video(video)

if __name__ == "__main__":
    pytest.main()
