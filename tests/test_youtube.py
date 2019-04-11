from simple_youtube_api.YouTube import YouTube
import pytest
import os.path


def test_regular_function():
	yt = YouTube()

def test_youtube_search():
    print(os.path.abspath(os.curdir))
    with open('developer_key', 'r') as myfile:
        developer_key=myfile.read().replace('\n', '')

    youtube = YouTube()
    youtube.login(developer_key)

    youtube.search()

    videos = youtube.search("Your Search Term")

    for video in videos:
        print(video.get_title())

    video = youtube.search_by_video_id("Ks-_Mh1QhMc")
    print(video.get_title())

if __name__ == "__main__":
    pytest.main()