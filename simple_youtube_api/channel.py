'''Log into YouTube Channel and query and update data'''


import time
import random
import http.client
import os
import sys
from typing import List

import progressbar
import httplib2

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

from oauth2client.client import flow_from_clientsecrets
from oauth2client.tools import run_flow
from oauth2client.file import Storage

from .local_video import LocalVideo
from .youtube_video import YouTubeVideo

from . import youtube_constants

httplib2.RETRIES = 1
# Maximum number of times to retry before giving up.
MAX_RETRIES = 10

# Always retry when these exceptions are raised.
RETRIABLE_EXCEPTIONS = (
    httplib2.HttpLib2Error,
    IOError,
    http.client.NotConnected,
    http.client.IncompleteRead,
    http.client.ImproperConnectionState,
    http.client.CannotSendRequest,
    http.client.CannotSendHeader,
    http.client.ResponseNotReady,
    http.client.BadStatusLine,
)


# Always retry when an apiclient.errors.HttpError with one of these status
# codes is raised.
RETRIABLE_STATUS_CODES = [500, 502, 503, 504]


API_SERVICE_NAME = "youtube"
API_VERSION = "v3"


class Channel():
    """
    Class for authorizing changes to channel

    channel
      login object to the channel
     """

    def __init__(self):
        self.channel = None

    def login(
        self,
        client_secret_path: str,
        storage_path: str,
        scope=youtube_constants.SCOPES,
        auth_local_webserver=True,
    ):
        """Logs into the channel with credentials

        client_secret_path
            The path to the client_secret file, which should be obtained from
            Google cloud
        storage_path
            The path where the login is stored, or if logging in for the first
            the path where the login is saved into
        scope
            Sets the scope that the login will ask for
        auth_local_webserver
            Whether login process should use local auth webserver, set this to
            false if you are not doing this locally.
        """

        storage = Storage(storage_path)
        credentials = storage.get()

        if credentials is None or credentials.invalid:
            saved_argv = []
            if auth_local_webserver is False:
                saved_argv = sys.argv
                sys.argv = [sys.argv[0], "--noauth_local_webserver"]

            flow = flow_from_clientsecrets(client_secret_path, scope=scope)
            credentials = run_flow(flow, storage, http=httplib2.Http())

            sys.argv = saved_argv

        self.channel = build(
            API_SERVICE_NAME, API_VERSION, credentials=credentials
        )

    def get_login(self):
        """ Returns the login object
        """
        return self.channel

    def fetch_uploads(self) -> List[YouTubeVideo]:
        """ Fetches uploaded videos from channel
        """
        response = (
            self.channel.channels()
            .list(mine=True, part="contentDetails")
            .execute()
        )
        content_details = response["items"][0]["contentDetails"]
        uploads_playlist_id = content_details["relatedPlaylists"]["uploads"]

        playlistitems_list_request = self.channel.playlistItems().list(
            playlistId=uploads_playlist_id, part="snippet", maxResults=5
        )

        videos = []
        while playlistitems_list_request:
            playlistitems_list_response = playlistitems_list_request.execute()
            # Print information about each video.
            for playlist_item in playlistitems_list_response.get("items", []):
                video_title = playlist_item["snippet"]["title"]
                video_id = playlist_item["snippet"]["resourceId"]["videoId"]
                video_description = playlist_item["snippet"]["description"]

                video = YouTubeVideo(video_id, channel=self.channel)
                video.title = video_title
                video.description = video_description

                videos.append(video)

                playlistitems_list_request = self.channel.playlistItems().list_next(
                    playlistitems_list_request, playlistitems_list_response
                )

        return videos

    # TODO add more metadata to returned video
    def upload_video(self, video: LocalVideo):
        """ Uploads video to authorized channel
        """
        if video.file_path is None:
            Exception("Must specify a file path")

        uploader = Uploader(self.channel, video)
        youtube_video = uploader.initialize_upload()

        youtube_video.channel = self.get_login()

        if video.thumbnail_path is not None:
            self.set_video_thumbnail(youtube_video, video.thumbnail_path)

        if video.playlist_id is not None:
            self.add_video_to_playlist(video.playlist_id, youtube_video)

        return youtube_video

    # TODO: check that thumbnail path is valid
    def set_video_thumbnail(self, video, thumbnail_path):
        """ Sets thumbnail for video

            video
              YouTubeVideo object or the string id of the video
            thumbnail_path
              Path to the thumbnail
        """
        if isinstance(video, str):
            video_id = video
        else:
            video_id = video.id

        response = self.channel.thumbnails().set(
            videoId=video_id, media_body=thumbnail_path
        ).execute()

        return response

    def add_video_to_playlist(self, playlist_id, video):
        """ Adds video to playlist

            playlist_id
                The id of the playlist to be added to
            video
                YouTubeVideo object or the string id of the video
        """

        if isinstance(video, str):
            video_id = video
        else:
            video_id = video.id

        response = self.channel.playlistItems().insert(
            part="snippet",
            body={
                "snippet": {
                    "playlistId": playlist_id,
                    "position": 0,
                    "resourceId": {
                        "kind": "youtube#video",
                        "videoId": video_id
                    }
                }
            }
        ).execute()

        return response


class Uploader:
    """
    Internal helper class which encapsulates the upload stuff.
    """
    def __init__(self, channel, video):
        self.channel = channel
        self.video = video
        self.video_size = os.path.getsize(self.video.file_path)

    def generate_upload_body(self):
        """ Generates upload body """
        body = dict()

        snippet = dict()
        if self.video.title is not None:
            snippet.update({"title": self.video.title})
        else:
            Exception("Title is required")
        if self.video.description is not None:
            snippet.update({"description": self.video.description})
        if self.video.tags is not None:
            snippet.update({"tags": self.video.tags})
        if self.video.category is not None:
            snippet.update({"categoryId": self.video.category})
        else:
            Exception("Category is required")
        if self.video.default_language is not None:
            snippet.update({"defaultLanguage": self.video.default_language})
        body.update({"snippet": snippet})

        if self.video.status_set:
            status = dict()
            if self.video.embeddable is not None:
                status.update({"embeddable": self.video.embeddable})
            if self.video.license is not None:
                status.update({"license": self.video.license})
            if self.video.privacy_status is not None:
                status.update({"privacyStatus": self.video.privacy_status})
            if self.video.public_stats_viewable is not None:
                status.update({"publicStatsViewable": self.video.public_stats_viewable})
            if self.video.publish_at is not None:
                status.update({"publishAt": self.video.publish_at})
            if self.video.self_declared_made_for_kids is not None:
                status.update({"selfDeclaredMadeForKids": self.video.self_declared_made_for_kids})
            body.update({"status": status})

        return body

    def calculate_chunk_size(self):
        """ Calculates the chunk size for video """
        print("Video size: " + str(self.video_size) + " bytes")
        chunk_max = 1024*1024

        if self.video_size > chunk_max:
            chunk_size = chunk_max
        else:
            chunk_size = -1

        return chunk_size

    def initialize_upload(self):
        """ Initializes upload """
        body = self.generate_upload_body()
        chunk_size = self.calculate_chunk_size()
        # Call the API's videos.insert method to create and upload the video.
        insert_request = self.channel.videos().insert(
            part=",".join(list(body.keys())),
            body=body,
            media_body=MediaFileUpload(
                self.video.file_path, chunksize=chunk_size, resumable=True
            ),
        )

        return self.resumable_upload(insert_request)

    # This method implements an exponential backoff strategy to resume a
    # failed upload.
    # TODO: add more variables into video when returned
    def resumable_upload(self, request):
        """ Uploads video """
        youtube_video = None
        response = None
        error = None
        retry = 0
        while response is None:
            try:
                widgets = [
                    "Upload: ",
                    progressbar.Percentage(),
                    " ",
                    progressbar.Bar(marker=progressbar.RotatingMarker()),
                    " ",
                    progressbar.ETA(),
                    " ",
                    progressbar.FileTransferSpeed(),
                ]
                bar_object = progressbar.ProgressBar(
                    widgets=widgets, max_value=self.video_size
                ).start()

                response = None
                while response is None:
                    status, response = request.next_chunk(num_retries=4)
                    if status:
                        bar_object.update(status.resumable_progress)
                bar_object.finish()
                if "id" in response:
                    youtube_video = YouTubeVideo(response["id"])
                else:
                    raise Exception("The upload failed unexpectedly: " + response)
            except HttpError as http_error:
                if http_error.resp.status in RETRIABLE_STATUS_CODES:
                    error = "A retriable HTTP error %d occurred:\n%s" % (
                        http_error.resp.status,
                        http_error.content,
                    )
                else:
                    raise
            except RETRIABLE_EXCEPTIONS as http_error:
                error = "A retriable error occurred: %s" % http_error

            if error is not None:
                print(error)
                retry += 1
                if retry > MAX_RETRIES:
                    return youtube_video

                max_sleep = 2 ** retry
                sleep_seconds = random.random() * max_sleep
                print("Sleeping %f seconds and then retrying..." % sleep_seconds)
                time.sleep(sleep_seconds)
        return youtube_video
