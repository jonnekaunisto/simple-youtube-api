Simple Youtube API
==================

.. image:: https://badge.fury.io/py/simple-youtube-api.svg
    :target: https://badge.fury.io/py/simple-youtube-api
    :alt: Simple YouTube API page on the Python Package Index
.. image:: https://travis-ci.org/jonnekaunisto/simple-youtube-api.svg?branch=master
    :target: https://travis-ci.org/jonnekaunisto/simple-youtube-api
    :alt: Build status on travis
.. image:: https://coveralls.io/repos/github/jonnekaunisto/simple-youtube-api/badge.svg?branch=master
    :target: https://coveralls.io/github/jonnekaunisto/simple-youtube-api?branch=master
    :alt: Coverage on coveralls



Simple Youtube API is a Youtube API wrapper for python, making it easier to search and upload your videos.


Examples
--------

In this example we log in into a YouTube channel, set the appropriate variables for a video and upload the video to the YouTube channel that we logged into:

.. code:: python

    from simple_youtube_api.Channel import Channel
    from simple_youtube_api.LocalVideo import LocalVideo

    # loggin into the channel
    channel = Channel()
    channel.login("client_secret.json", "credentials.storage")

    # setting up the video that is going to be uploaded
    video = LocalVideo(file_path="test_vid.mp4")

    # setting snippet
    video.set_title("My Title")
    video.set_description("This is a description")
    video.set_tags(["this", "tag"])
    video.set_category("gaming")
    video.set_default_language("english")

    # setting status
    video.set_embeddable(True)
    video.set_license("creativeCommon")
    video.set_privacy_status("private")
    video.set_public_stats_viewable(True)

    # setting thumbnail
    video.set_thumbnail_path('test_thumb.png')

    # uploading video and printing the results
    video = channel.upload_video(video)
    print(video.get_video_id())
    print(video)

    # liking video
    video.like()



Installation
------------
Simple YouTube API needs API keys from Google in order to be able to make queries to YouTube.

**Installation by hand:** you can download the source files from PyPi or Github:

.. code:: bash

    $ (sudo) python setup.py install

**Installation with pip:** make sure that you have ``pip`` installed, type this in a terminal:

.. code:: bash

    $ (sudo) pip install simple-youtube-api
    
  
Generating YouTube API Keys
---------------------------
1. Log into https://console.cloud.google.com
2. Create a new Project
3. Search for "YouTube Data API V3"
4. Click Credentials
5. Click Create Credentials
6. Select that you will call API from "Web Server"
7. Select "Public Data" if you want to not get private data and "User Data" if you do
8. Download or copy your API key from the Credentials tab

Documentation
-------------
Running Tests
-------------
Run the python command

.. code:: bash 

   python setup.py test

References
----------
`YouTube API Documentation`_

`Python YouTube API Examples`_


Contribute
----------
1. Fork the repository from Github
2. Clone your fork 

.. code:: bash 

   git clone https://github.com/yourname/simple-youtube-api.git

3. Add the main repository as a remote

.. code:: bash

    git remote add upstream https://github.com/jonnekaunisto/simple-youtube-api.git

4. Create a pull request and follow the guidelines


Maintainers
-----------
jonnekaunisto (owner)


.. _`YouTube API Documentation`: https://developers.google.com/youtube/v3/docs/
.. _`Python YouTube API Examples`: https://github.com/youtube/api-samples/tree/master/python


