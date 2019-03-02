from simple_youtube_api.Channel import Channel
from simple_youtube_api.Video import Video


import pytest
import os


def test_video_regular_function():
    file_path = os.path.dirname(os.path.abspath(__file__)) + os.sep + "test_video.py"
    title = "this is a title"
    description = "this is a description"
    tags = ["this", "is" "a", "tag"]
    string_category = "film"
    id_category = 1
    privacy_statuses = ['public', 'private', 'unlisted']


    video = Video()

    video.set_file_path(file_path)
    video.set_title(title)
    video.set_description(description)
    video.set_tags(tags)
    video.set_category(string_category)

    assert video.get_file_path() == file_path
    assert video.get_title() == title
    assert video.get_description() == description
    assert video.get_tags() == tags
    assert video.get_category() == id_category


    for privacy_status in privacy_statuses:
        video.set_privacy_status(privacy_status)
        assert video.get_privacy_status() == privacy_status


if __name__ == "__main__":
    pytest.main()

