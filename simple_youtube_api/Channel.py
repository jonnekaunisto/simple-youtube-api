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


SCOPE = ['https://www.googleapis.com/auth/youtube']
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

    # TODO: add scopes as option
    def login(self, client_secret_path: str, storage_path: str, scope=SCOPE):
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
        uploads_playlist_id = response['items'][0]['contentDetails']['relatedPlaylists']['uploads']

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

                playlistitems_list_request = self.channel.playlistItems().list_next(
                    playlistitems_list_request, playlistitems_list_response)

        return videos

    def upload_video(self, video: LocalVideo):
        ''' Uploads video to authorized channel
        '''
        return youtube_api.initialize_upload(self.channel, video)

    def set_video_thumbnail(self, thumbnail_path, video=None, video_id=None):
        ''' Sets thumbnail for video
        '''
        if video is not None:
            video_id = video.get_video_id()

        self.channel.thumbnails().set(
            videoId=video_id,
            media_body=thumbnail_path
        )
