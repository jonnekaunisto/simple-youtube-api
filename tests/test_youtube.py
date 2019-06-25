from simple_youtube_api.YouTube import YouTube
import pytest
import os.path


def test_regular_function():
    with open('credentials/developer_key', 'r') as myfile:
        developer_key = myfile.read().replace('\n', '')

    yt = YouTube()
    yt.login(developer_key)
    yt.get_login()


def test_youtube_search():
    youtube = get_youtube()

    videos = youtube.search("Your Search Term")

    for video in videos:
        print(video.get_title())

    video = youtube.search_by_video_id("Ks-_Mh1QhMc")
    print(video.get_title())

    response = youtube.search_by_video_id_raw("Ks-_Mh1QhMc")
    print(response)


def test_fetch_categories():
    youtube = get_youtube()
    youtube.fetch_categories()


def get_youtube():
    with open('credentials/developer_key', 'r') as myfile:
        developer_key = myfile.read().replace('\n', '')

    youtube = YouTube()
    youtube.login(developer_key)

    return youtube

if __name__ == "__main__":
    pytest.main()
