"""Test youtube"""
import pytest


from simple_youtube_api import YouTube


def test_regular_function():
    """Test constructor"""
    with open("credentials/developer_key", "r") as myfile:
        developer_key = myfile.read().replace("\n", "")

    youtube = YouTube()
    youtube.login(developer_key)
    youtube.get_login()


def test_youtube_search():
    """Test youtube search"""
    youtube = get_youtube()

    videos = youtube.search("Your Search Term")

    for video in videos:
        print(video.title)

    video = youtube.search_by_video_id("Ks-_Mh1QhMc")
    print(video.title)

    response = youtube.search_by_video_id_raw("Ks-_Mh1QhMc")
    print(response)


def test_fetch_categories():
    """Test fetching categories"""
    youtube = get_youtube()
    youtube.fetch_categories()


def get_youtube():
    """Makes youtube object"""
    with open("credentials/developer_key", "r") as myfile:
        developer_key = myfile.read().replace("\n", "")

    youtube = YouTube()
    youtube.login(developer_key)

    return youtube


if __name__ == "__main__":
    pytest.main()
