from simple_youtube_api.YouTubeVideo import YouTubeVideo
from simple_youtube_api.YouTube import YouTube
from simple_youtube_api.Channel import Channel


import pytest
import os


CLIENT_SECRET_NAME = "credentials/client_secret.json"
CREDENTIALS = "credentials/credentials.storage"

YOUTUBE_VIDEO_ID = "_i4fVYVqLbQ"


def test_youtube_video_constructor():

    video_id = YOUTUBE_VIDEO_ID

    with open('credentials/developer_key', 'r') as myfile:
        developer_key = myfile.read().replace('\n', '')

    youtube = YouTube()
    youtube.login(developer_key)

    video = YouTubeVideo(video_id, youtube=youtube.get_login())

    video.get_video_id()

    video.set_youtube_auth(youtube)
    video.set_channel_auth(youtube)
    video.get_channel_id()

    '''
    assert video.get_video_id() == video_id
    assert video.get_title() == title
    assert video.get_description() == description
    assert video.get_tags() == tags
    #assert video.get_category() == id_category


    for privacy_status in privacy_statuses:
        video.set_privacy_status(privacy_status)
        assert video.get_privacy_status() == privacy_status
    '''


def test_youtube_video_downloading():
    video = YouTubeVideo(YOUTUBE_VIDEO_ID)
    video.download()


def test_youtube_video_rating():
    video_id = YOUTUBE_VIDEO_ID

    channel = Channel()

    assert os.path.isfile(CLIENT_SECRET_NAME), "CLIENT SECRET_NAME not valid"
    assert os.path.isfile(CREDENTIALS), "CREDENTIALS is not valid"

    channel.login(CLIENT_SECRET_NAME, CREDENTIALS)

    video = YouTubeVideo(video_id, channel=channel.get_login())

    video.dislike()
    video.remove_rating()
    video.like()

    with pytest.raises(Exception):
        video.rate_video("not_valid")


def test_youtube_video_without_credentials():
    video_id = YOUTUBE_VIDEO_ID

    video = YouTubeVideo(video_id)

    with pytest.raises(Exception):
        video.fetch()

    with pytest.raises(Exception):
        video.update()

    with pytest.raises(Exception):
        video.rate_video("like")

    with pytest.raises(Exception):
        video.like()

    with pytest.raises(Exception):
        video.dislike()

    with pytest.raises(Exception):
        video.remove_rating()


def test_youtube_video_fetch():
    video_id = YOUTUBE_VIDEO_ID

    with open('credentials/developer_key', 'r') as myfile:
        developer_key = myfile.read().replace('\n', '')

    youtube = YouTube()
    youtube.login(developer_key)

    video = YouTubeVideo(video_id, youtube=youtube.get_login())
    video.fetch(all_parts=True)


def test_youtube_video_fetch_comment_threads():
    with open('credentials/developer_key', 'r') as myfile:
        developer_key = myfile.read().replace('\n', '')

    youtube = YouTube()
    youtube.login(developer_key)

    video = YouTubeVideo(YOUTUBE_VIDEO_ID, youtube=youtube.get_login())

    video.fetch_comment_threads()


if __name__ == "__main__":
    pytest.main()
