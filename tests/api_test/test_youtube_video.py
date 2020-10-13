""" Testing youtube video """
import os
import pytest

from simple_youtube_api import YouTubeVideo, YouTube, Channel

CLIENT_SECRET_NAME = "credentials/client_secret.json"
CREDENTIALS = "credentials/credentials.storage"

YOUTUBE_VIDEO_ID = "_i4fVYVqLbQ"


def test_youtube_video_constructor():
    """Test video constructor"""

    video_id = YOUTUBE_VIDEO_ID

    with open("credentials/developer_key", "r") as myfile:
        developer_key = myfile.read().replace("\n", "")

    youtube = YouTube()
    youtube.login(developer_key)

    video = YouTubeVideo(video_id=video_id, youtube=youtube.get_login())

    video.set_youtube_auth(youtube)
    video.set_channel_auth(youtube)

    # assert video.video_id == video_id
    # assert video.title == title
    # assert video.description == description
    # assert video.tags == tags
    #assert video.category == id_category


    # for privacy_status in privacy_statuses:
    #    video.set_privacy_status(privacy_status)
    #    assert video.privacy_status == privacy_status



def test_youtube_video_rating():
    """Test rating youtube video"""
    video_id = YOUTUBE_VIDEO_ID

    channel = Channel()

    assert os.path.isfile(CLIENT_SECRET_NAME), "CLIENT SECRET_NAME not valid"
    assert os.path.isfile(CREDENTIALS), "CREDENTIALS is not valid"

    channel.login(CLIENT_SECRET_NAME, CREDENTIALS)

    video = YouTubeVideo(video_id=video_id, channel=channel.get_login())

    video.dislike()
    video.remove_rating()
    video.like()

    with pytest.raises(Exception):
        video.rate_video("not_valid")


def test_youtube_video_without_credentials():
    """Test video without credentials"""
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
    """Test fetching video"""
    video_id = YOUTUBE_VIDEO_ID

    with open("credentials/developer_key", "r") as myfile:
        developer_key = myfile.read().replace("\n", "")

    youtube = YouTube()
    youtube.login(developer_key)

    video = YouTubeVideo(video_id=video_id, youtube=youtube.get_login())
    video.fetch(all_parts=True)


def test_youtube_video_fetch_comment_threads():
    """Test fetching comment thread"""
    with open("credentials/developer_key", "r") as myfile:
        developer_key = myfile.read().replace("\n", "")

    youtube = YouTube()
    youtube.login(developer_key)

    video = YouTubeVideo(video_id=YOUTUBE_VIDEO_ID, youtube=youtube.get_login())

    video.fetch_comment_threads()


if __name__ == "__main__":
    pytest.main()
