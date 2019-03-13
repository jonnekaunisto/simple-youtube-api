Simple Youtube API
=======

.. image:: https://badge.fury.io/py/simple-youtube-api.svg
    :target: https://badge.fury.io/py/simple-youtube-api
    :alt: Simple YouTube API page on the Python Package Index


Simple Youtube API is a Youtube API wrapper for python, making it easier to search and upload your videos.


Examples
--------

In this example we log in into a YouTube channel, set the appropriate variables for a video and upload the video to the YouTube channel that we logged into:

.. code:: python

    from simple_youtube_api.Channel import Channel 
    from simple_youtube_api.Video import Video

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
Simple YouTube API needs API keys from Google in order to be able to make queries to YouTube.
**Installation by hand:** you can download the source files from PyPi or Github:

.. code:: bash

    $ (sudo) python setup.py install

**Installation with pip:** make sure that you have ``pip`` installed, type this in a terminal:

.. code:: bash

    $ (sudo) pip install simple-youtube-api



Documentation
-------------
Running Tests
-------------
References
----------
`YouTube API Documentation`_

`Python YouTube API Examples`_


Contribute
----------



Maintainers
-----------
jonnekaunisto (owner)


.. _`YouTube API Documentation`: https://developers.google.com/youtube/v3/docs/
.. _`Python YouTube API Examples`: https://github.com/youtube/api-samples/tree/master/python


