"""Testing local video"""
import os

import pytest
<<<<<<< HEAD

from simple_youtube_api import LocalVideo
from simple_youtube_api.channel import generate_upload_body
from simple_youtube_api import youtube_constants

=======
>>>>>>> Added ability to pass datetime object to set_publish_at function in LocalVideo class
import os
import datetime

def test_local_video_regular_function():
    """Testing function"""
    file_path = (
        os.path.dirname(os.path.abspath(__file__))
        + os.sep
        + "test_local_video.py"
    )
    title = "this is a title"
    description = "this is a description"
    tags = ["this", "is", "a", "tag"]
    string_category = "film"
    id_category = 1
    privacy_statuses = ["public", "private", "unlisted"]
    playlist_id = "some_playlist_id"
<<<<<<< HEAD
<<<<<<< HEAD
    publish_at = datetime.datetime(datetime.date.today().year+1,5,17)
=======
    publish_at = datetime.datetime(2028, 5, 17)
>>>>>>> Added ability to pass datetime object to set_publish_at function in LocalVideo class
=======
    publish_at = datetime.datetime(datetime.date.today().year+1,5,17)
>>>>>>> added new edits

    video = LocalVideo(file_path)

    video.set_title(title)
    video.set_description(description)
    video.set_tags(tags)
    video.set_category(string_category)
    video.set_playlist(playlist_id)

    assert video.file_path == file_path
    assert video.title == title
    assert video.description == description
    assert video.tags == tags
    assert video.category == id_category
    assert video.playlist_id == playlist_id

    video.set_category(id_category)
    assert video.category == id_category

    for privacy_status in privacy_statuses:
        video.set_privacy_status(privacy_status)
        video.privacy_status == privacy_status
    video.set_privacy_status("private")
    assert video.privacy_status == "private"
    video.set_publish_at(publish_at)
    assert video.publish_at == publish_at.strftime('%G-%m-%dT%H:%M:%S.000Z')
    # TODO: add stronger check
    assert generate_upload_body(video)


def test_local_video_negative_function():
    """Testing negative cases"""
    # snippet variables
    file_path = os.path.realpath(__file__)
    bad_file_path = "not_valid"
    thumbnail_path = "not_valid"
    title = "-" * (youtube_constants.MAX_YOUTUBE_TITLE_LENGTH + 1)
    description = "-" * (youtube_constants.MAX_YOUTUBE_DESCRIPTION_LENGTH + 1)
    tags = ["-" * (youtube_constants.MAX_YOUTUBE_TAGS_LENGTH + 1)]
    string_category = "not a category"
    id_category = -1
    default_language = False

    # status variables
    embeddable = "not_valid"
    video_license = "not_valid"
    privacy_status = "not_valid"
    public_stats_viewable = "not_valid"
    publish_at = datetime.datetime(1, 1, 1)

    video = LocalVideo(file_path)

    # TODO: add stronger checks

    # misc test
    with pytest.raises(Exception):
        video.set_file_path(bad_file_path)
    with pytest.raises(Exception):
        video.set_thumbnail_path(thumbnail_path)

    # snippet test
    with pytest.raises(Exception):
        video.set_title(title)
    with pytest.raises(Exception):
        video.set_title(True)
    with pytest.raises(Exception):
        video.set_description(description)
    with pytest.raises(Exception):
        video.set_description(True)
    with pytest.raises(Exception):
        video.set_tags(tags)
    with pytest.raises(Exception):
        video.set_tags(True)
    with pytest.raises(Exception):
        video.set_category(string_category)
    with pytest.raises(Exception):
        video.set_category(id_category)
    with pytest.raises(Exception):
        video.set_default_language(default_language)

    # status test
    with pytest.raises(Exception):
        video.set_embeddable(embeddable)
    with pytest.raises(Exception):
        video.set_license(video_license)
    with pytest.raises(Exception):
        video.set_privacy_status(privacy_status)
    with pytest.raises(Exception):
        video.set_public_stats_viewable(public_stats_viewable)
    privacy_status = "private"
    with pytest.raises(Exception):
        video.set_publish_at(publish_at)
    with pytest.raises(Exception):
        video.set_publish_at(datetime.datetime(2020, 5, 17))
    with pytest.raises(Exception):
        video.set_publish_at(datetime.datetime(2028, 5, 17, 12, 32, 00))
    privacy_status = "not_valid"
    with pytest.raises(Exception):
        video.set_publish_at(datetime.datetime(2028, 5, 17, 12, 30, 00))


def test_local_video_constructor():
    """Testing constructor"""
    file_path = (
        os.path.dirname(os.path.abspath(__file__))
        + os.sep
        + "test_local_video.py"
    )
    title = "this is a title"
    description = "this is a description"
    tags = ["this", "is", "a", "tag"]
    string_category = "film"
    id_category = 1
    default_language = "english"

    # status variables
    embeddable = True
<<<<<<< HEAD
    video_license = "youtube"
    privacy_status = "public"
=======
    license = "youtube"
    privacy_status = "private"
>>>>>>> Added ability to pass datetime object to set_publish_at function in LocalVideo class
    public_stats_viewable = True
    publish_at = datetime.datetime(2021, 5, 17)

    # snippet test
    video = LocalVideo(
        file_path=file_path,
        title=title,
        description=description,
        tags=tags,
        category=string_category,
        default_language="english",
    )

    assert video.file_path == file_path, "Wrong file path: " + str(
        video.file_path
    )
    assert video.title == title, "Wrong title:" + str(video.title)
    assert video.description == description, "Wrong description: " + str(
        video.description
    )
    assert video.tags == tags, "Wrong tags: " + str(video.tags)
    assert video.category == id_category, "Wrong category: " + str(
        video.category
    )
    assert (
        video.default_language == default_language
    ), "Wrong language: " + str(video.default_language)

    assert video.snippet_set is True, "Wrong snippet set: " + str(
        video.snippet_set
    )

    # status test
    assert video.status_set is False, "Wrong status set " + str(video.status_set)

    video.set_embeddable(embeddable)
    video.set_license(video_license)
    video.set_privacy_status(privacy_status)
    video.set_public_stats_viewable(public_stats_viewable)
    video.set_publish_at(publish_at)

    assert video.embeddable == embeddable
    assert video.license == video_license
    assert (
        video.privacy_status == privacy_status
    ), "Privacy Wrong: " + str(video.privacy_status)
    assert video.public_stats_viewable == public_stats_viewable
    assert video.publish_at == publish_at.strftime('%G-%m-%dT%H:%M:%S.000Z')

    assert video.status_set is True, "Wrong video status: " + str(
        video.status_set
    )

    video.set_thumbnail_path(file_path)
    assert video.thumbnail_path == file_path

    str(video)


if __name__ == "__main__":
    pytest.main()
