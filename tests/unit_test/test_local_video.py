from simple_youtube_api.Channel import Channel
from simple_youtube_api.Channel import generate_upload_body
from simple_youtube_api.LocalVideo import LocalVideo
from simple_youtube_api import youtube_api


import pytest
import os


def test_local_video_regular_function():
    file_path = (
        os.path.dirname(os.path.abspath(__file__))
        + os.sep
        + "test_local_video.py"
    )
    title = "this is a title"
    description = "this is a description"
    tags = ["this", "is" "a", "tag"]
    string_category = "film"
    id_category = 1
    privacy_statuses = ["public", "private", "unlisted"]
    playlist_id = "some_playlist_id"

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

    # TODO: add stronger check
    assert generate_upload_body(video)


def test_local_video_negative_function():
    # snippet variables
    file_path = os.path.realpath(__file__)
    bad_file_path = "not_valid"
    thumbnail_path = "not_valid"
    title = "-" * (youtube_api.MAX_YOUTUBE_TITLE_LENGTH + 1)
    description = "-" * (youtube_api.MAX_YOUTUBE_DESCRIPTION_LENGTH + 1)
    tags = ["-" * (youtube_api.MAX_YOUTUBE_TAGS_LENGTH + 1)]
    string_category = "not a category"
    id_category = -1
    default_language = False

    # status variables
    embeddable = "not_valid"
    license = "not_valid"
    privacy_status = "not_valid"
    public_stats_viewable = "not_valid"
    publish_at = False

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
        video.set_license(license)
    with pytest.raises(Exception):
        video.set_privacy_status(privacy_status)
    with pytest.raises(Exception):
        video.set_public_stats_viewable(public_stats_viewable)
    with pytest.raises(Exception):
        video.set_publish_at(publish_at)


def test_local_video_constructor():
    file_path = (
        os.path.dirname(os.path.abspath(__file__))
        + os.sep
        + "test_local_video.py"
    )
    title = "this is a title"
    description = "this is a description"
    tags = ["this", "is" "a", "tag"]
    string_category = "film"
    id_category = 1
    default_language = "english"

    # status variables
    embeddable = True
    license = "youtube"
    privacy_status = "public"
    public_stats_viewable = True
    publish_at = "9"

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
    video.set_license(license)
    video.set_privacy_status(privacy_status)
    video.set_public_stats_viewable(public_stats_viewable)
    video.set_publish_at(publish_at)

    assert video.embeddable == embeddable
    assert video.license == license
    assert (
        video.privacy_status == privacy_status
    ), "Privacy Wrong: " + str(video.privacy_status)
    assert video.public_stats_viewable == public_stats_viewable
    assert video.publish_at == publish_at

    assert video.status_set is True, "Wrong video status: " + str(
        video.status_set
    )

    video.set_thumbnail_path(file_path)
    assert video.thumbnail_path == file_path

    str(video)


if __name__ == "__main__":
    pytest.main()
