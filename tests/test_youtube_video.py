from simple_youtube_api.YouTubeVideo import YouTubeVideo
from simple_youtube_api.YouTube import YouTube
from simple_youtube_api.Channel import Channel


import pytest
import os


CLIENT_SECRET_NAME = "credentials/client_secret.json"
CREDENTIALS = "credentials/credentials.storage"


def test_youtube_video_constructor():
    
    video_id = "_i4fVYVqLbQ"
    '''
    title = "this is a title"
    description = "this is a description"
    tags = ["this", "is" "a", "tag"]
    string_category = "film"
    id_category = 1
    privacy_statuses = ['public', 'private', 'unlisted']
    '''

    with open('credentials/developer_key', 'r') as myfile:
        developer_key=myfile.read().replace('\n', '')

    youtube = YouTube()
    youtube.login(developer_key)

    video = YouTubeVideo(video_id, youtube=youtube)
    
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

def test_youtube_video_rating():
    video_id = "_i4fVYVqLbQ"

    channel = Channel()

    assert os.path.isfile(CLIENT_SECRET_NAME), "CLIENT SECRET_NAME is not valid"
    assert os.path.isfile(CREDENTIALS), "CREDENTIALS is not valid"

    channel.login(CLIENT_SECRET_NAME, CREDENTIALS)

    video = YouTubeVideo(video_id, channel=channel.get_login())

    video.dislike()
    video.remove_rating()
    video.like()

    
    

if __name__ == "__main__":
    pytest.main()

