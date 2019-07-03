from simple_youtube_api.LocalVideo import LocalVideo
from simple_youtube_api.YouTubeVideo import YouTubeVideo
from simple_youtube_api import youtube_api

import time
import random
import argparse
import http.client
import httplib2
import typing
from typing import List
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

from oauth2client.client import flow_from_clientsecrets
from oauth2client.tools import run_flow
from oauth2client.file import Storage

httplib2.RETRIES = 1
# Maximum number of times to retry before giving up.
MAX_RETRIES = 10

# Always retry when these exceptions are raised.
RETRIABLE_EXCEPTIONS = (httplib2.HttpLib2Error, IOError,
                        http.client.NotConnected, http.client.IncompleteRead,
                        http.client.ImproperConnectionState,
                        http.client.CannotSendRequest,
                        http.client.CannotSendHeader,
                        http.client.ResponseNotReady,
                        http.client.BadStatusLine)


# Always retry when an apiclient.errors.HttpError with one of these status
# codes is raised.
RETRIABLE_STATUS_CODES = [500, 502, 503, 504]


API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'


# add functions
class Channel(object):
    '''
    Class for authorizing changes to channel

    Attributes
    -----------

    channel
      login object to the channel
     '''
    def __init__(self):
        self.channel = None

    def login(self, client_secret_path: str, storage_path: str,
              scope=youtube_api.SCOPES):
        ''' Logs into the channel with credentials
        '''
        STORAGE = Storage(storage_path)
        credentials = STORAGE.get()

        if credentials is None or credentials.invalid:
            flow = flow_from_clientsecrets(client_secret_path, scope=scope)
            http = httplib2.Http()
            credentials = run_flow(flow, STORAGE, http=http)
        self.channel = build(API_SERVICE_NAME, API_VERSION,
                             credentials=credentials)

    def get_login(self):
        ''' Returns the login object
        '''
        return self.channel

    def fetch_uploads(self) -> List[YouTubeVideo]:
        ''' Fetches uploaded videos from channel
        '''
        response = self.channel.channels().list(
            mine=True,
            part='contentDetails'
        ).execute()
        content_details = response['items'][0]['contentDetails']
        uploads_playlist_id = content_details['relatedPlaylists']['uploads']

        playlistitems_list_request = self.channel.playlistItems().list(
            playlistId=uploads_playlist_id,
            part='snippet',
            maxResults=5
        )

        videos = []
        while playlistitems_list_request:
            playlistitems_list_response = playlistitems_list_request.execute()
            # Print information about each video.
            for playlist_item in playlistitems_list_response.get('items', []):
                video_title = playlist_item['snippet']['title']
                video_id = playlist_item['snippet']['resourceId']['videoId']
                video_description = playlist_item['snippet']['description']

                video = YouTubeVideo(video_id, channel=self.channel)
                video.title = video_title
                video.description = video_description

                videos.append(video)

                playlistitems_list_request = self.channel.playlistItems().\
                    list_next(playlistitems_list_request,
                              playlistitems_list_response)

        return videos

    # TODO add more metadata to returned video
    def upload_video(self, video: LocalVideo):
        ''' Uploads video to authorized channel
        '''
        youtube_video = initialize_upload(self.channel, video)

        youtube_video.channel = self.get_login()

        if video.thumbnail_path is not None:
            self.set_video_thumbnail(youtube_video, video.thumbnail_path)

        return youtube_video

    def set_video_thumbnail(self, video, thumbnail_path):
        ''' Sets thumbnail for video
        '''
        video_id = video.get_video_id()

        self.channel.thumbnails().set(
            videoId=video_id,
            media_body=thumbnail_path
        )


def generate_upload_body(video):
    body = dict()

    snippet = dict()
    if video.title is not None:
        snippet.update({"title": video.title})
    else:
        Exception("Title is required")
    if video.description is not None:
        snippet.update({"description": video.description})
    if video.tags is not None:
        snippet.update({"tags": video.tags})
    if video.category is not None:
        snippet.update({"categoryId": video.category})
    else:
        Exception("Category is required")
    if video.default_language is not None:
        snippet.update({"defaultLanguage": video.default_language})
    body.update({"snippet": snippet})

    if video.status_set:
        status = dict()
        if video.embeddable is not None:
            status.update({"embeddable": video.embeddable})
        if video.license is not None:
            status.update({"license": video.license})
        if video.privacy_status is not None:
            status.update({"privacyStatus": video.privacy_status})
        if video.public_stats_viewable is not None:
            status.update({"publicStatsViewable": video.public_stats_viewable})
        if video.publish_at is not None:
            status.update({"publishAt": video.publish_at})
        body.update({"status": status})

    return body


def initialize_upload(channel, video):
    body = generate_upload_body(video)

    # Call the API's videos.insert method to create and upload the video.
    insert_request = channel.videos().insert(
        part=','.join(list(body.keys())),
        body=body,
        media_body=MediaFileUpload(video.get_file_path(), chunksize=-1,
                                   resumable=True)
    )

    return resumable_upload(insert_request)


# This method implements an exponential backoff strategy to resume a
# failed upload.
# TODO: add more variables into video when returned
def resumable_upload(request):
    youtube_video = None
    response = None
    error = None
    retry = 0
    while response is None:
        try:
            print('Uploading file...')
            status, response = request.next_chunk()
            if response is not None:
                if 'id' in response:
                    print(str(response))
                    youtube_video = YouTubeVideo(response['id'])
                else:
                    exit('The upload failed with an unexpected response: %s' %
                         response)
        except HttpError as e:
            if e.resp.status in RETRIABLE_STATUS_CODES:
                error = 'A retriable HTTP error %d occurred:\n%s' %\
                         (e.resp.status, e.content)
            else:
                raise
        except RETRIABLE_EXCEPTIONS as e:
            error = 'A retriable error occurred: %s' % e

        if error is not None:
            print(error)
            retry += 1
            if retry > MAX_RETRIES:
                return youtube_video

            max_sleep = 2 ** retry
            sleep_seconds = random.random() * max_sleep
            print('Sleeping %f seconds and then retrying...' % sleep_seconds)
            time.sleep(sleep_seconds)
    return youtube_video
