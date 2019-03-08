from simple_youtube_api.YouTubeVideo import YouTubeVideo


import pytest
import os


def test_youtube_video_regular_function():
    
    video_id = "EI"
    title = "this is a title"
    description = "this is a description"
    tags = ["this", "is" "a", "tag"]
    string_category = "film"
    id_category = 1
    privacy_statuses = ['public', 'private', 'unlisted']

    video = YouTubeVideo(video_id, title=title, description=description, tags=tags)
    

    assert video.get_video_id() == video_id
    assert video.get_title() == title
    assert video.get_description() == description
    assert video.get_tags() == tags
    #assert video.get_category() == id_category

    '''
    for privacy_status in privacy_statuses:
        video.set_privacy_status(privacy_status)
        assert video.get_privacy_status() == privacy_status
    '''


if __name__ == "__main__":
    pytest.main()

