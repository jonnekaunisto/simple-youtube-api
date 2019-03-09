Simple Youtube API
=======

.. image:: https://badge.fury.io/py/simple-youtube-api.svg
    :target: https://badge.fury.io/py/simple-youtube-api
    :alt: Simple YouTube API page on the Python Package Index


Simple Youtube API is a Youtube API wrapper for python, making it easier to search and upload your videos.


Examples
--------

In this example we open a video file, select the subclip between t=50s and t=60s, add a title at the center of the screen, and write the result to a new file:

.. code:: python

    from simple_youtube_api.Channel import Channel from simple_youtube_api.Video import Video

    channel = Channel() channel.login("client_secret.json", "credentials.storage")

    video = Video(file_path="test_vid.mp4") 
    video.set_title("This is a title") 
    video.set_description("This is a description")
    video.set_tags(["this", "tag"]) 
    video.set_category("film") 
    video.set_privacy_status("private")

    channel.upload_video(video)


Installation
------------



Documentation
-------------


Running Tests
-------------



Contribute
----------


Maintainers
-----------
jonnekaunisto (owner)
