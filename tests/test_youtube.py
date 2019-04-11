from simple_youtube_api.YouTube import YouTube
import pytest
import os.path


def test_regular_function():
	yt = YouTube()

def test_youtube_search():
    print(os.path.abspath(os.curdir))
    with open('developer_key', 'r') as myfile:
        data=myfile.read().replace('\n', '')

    developer_key = data

    youtube = YouTube()
    youtube.login(developer_key)

if __name__ == "__main__":
    pytest.main()