from simple_youtube_api.Channel import Channel
from simple_youtube_api.LocalVideo import LocalVideo
from simple_youtube_api import youtube_api


import pytest
import os


def test_local_video_regular_function():
    file_path = os.path.dirname(os.path.abspath(__file__)) + os.sep + "test_local_video.py"
    title = "this is a title"
    description = "this is a description"
    tags = ["this", "is" "a", "tag"]
    string_category = "film"
    id_category = 1
    privacy_statuses = ['public', 'private', 'unlisted']


    video = LocalVideo(file_path)

    assert video.set_title(title)
    assert video.set_description(description)
    assert video.set_tags(tags)
    assert video.set_category(string_category)

    assert video.get_file_path() == file_path
    assert video.get_title() == title
    assert video.get_description() == description
    assert video.get_tags() == tags
    assert video.get_category() == id_category

    assert video.set_category(id_category)
    assert video.get_category() == id_category


    for privacy_status in privacy_statuses:
        assert video.set_privacy_status(privacy_status)
        assert video.get_privacy_status() == privacy_status

def test_local_video_negative_function():
    file_path = "not_valid"
    title = "-" * (youtube_api.MAX_YOUTUBE_TITLE_LENGTH + 1)
    description = "-" * (youtube_api.MAX_YOUTUBE_DESCRIPTION_LENGTH + 1)
    tags = ["-" * (youtube_api.MAX_YOUTUBE_TAGS_LENGTH + 1)]
    string_category = "not a category"
    id_category = -1
    privacy_status = "not_valid"


    video = LocalVideo(file_path)

    assert not video.set_title(title)
    assert not video.set_description(description)
    assert not video.set_tags(tags)
    assert not video.set_category(string_category)
    assert not video.set_category(id_category)
    assert not video.set_privacy_status(privacy_status)

def test_local_video_constructor():
    file_path = os.path.dirname(os.path.abspath(__file__)) + os.sep + "test_local_video.py"
    title = "this is a title"
    description = "this is a description"
    tags = ["this", "is" "a", "tag"]
    string_category = "film"
    id_category = 1
    privacy_status = "public"


    video = LocalVideo(file_path=file_path, title=title, description=description,
                  tags=tags, category=string_category, privacy_status=privacy_status)

    assert video.get_file_path() == file_path
    assert video.get_title() == title
    assert video.get_description() == description
    assert video.get_tags() == tags
    assert video.get_category() == id_category
    assert video.get_privacy_status() == privacy_status



if __name__ == "__main__":
    pytest.main()

