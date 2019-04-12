from simple_youtube_api.Video import Video
from simple_youtube_api.YouTubeVideo import YouTubeVideo
import argparse
import http.client
import httplib2
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
RETRIABLE_EXCEPTIONS = (httplib2.HttpLib2Error, IOError, http.client.NotConnected,
                        http.client.IncompleteRead, http.client.ImproperConnectionState,
                        http.client.CannotSendRequest, http.client.CannotSendHeader,
                        http.client.ResponseNotReady, http.client.BadStatusLine)


# Always retry when an apiclient.errors.HttpError with one of these status
# codes is raised.
RETRIABLE_STATUS_CODES = [500, 502, 503, 504]
SCOPE = ['https://www.googleapis.com/auth/youtube']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
VALID_PRIVACY_STATUSES = ('public', 'private', 'unlisted')


#add functions
class Channel(object):


    def __init__(self):
        self.channel = None

    def login(self, client_secret_path, storage_path):
        STORAGE = Storage(storage_path)
        credentials = STORAGE.get()
        
        if credentials is None or credentials.invalid:
            flow = flow_from_clientsecrets(client_secret_path, scope=SCOPE)
            http = httplib2.Http()
            credentials = run_flow(flow, STORAGE, http=http)
        self.channel = build(API_SERVICE_NAME, API_VERSION, credentials = credentials)

    def get_login(self):
        return self.channel

    def upload_video(self, video):
        return self.initialize_upload(video)

    def initialize_upload(self, video):
        body = dict(
            snippet=dict(
                title=video.get_title(),
                description=video.get_description(),
                tags=video.get_tags(),
                categoryId=video.get_category()
            ),
            status=dict(
                privacyStatus=video.get_privacy_status()
            )
        )

        # Call the API's videos.insert method to create and upload the video.
        insert_request = self.channel.videos().insert(
            part=','.join(list(body.keys())),
            body=body,
            media_body=MediaFileUpload(video.get_file_path(), chunksize=-1, resumable=True)
        )

        return self.resumable_upload(insert_request)


    # This method implements an exponential backoff strategy to resume a
    # failed upload.
    def resumable_upload(self, request):
        response = None
        error = None
        retry = 0
        while response is None:
            try:
                print('Uploading file...')
                status, response = request.next_chunk()
                if response is not None:
                    if 'id' in response:
                        print(('Video https://www.youtube.com/watch?v=%s was successfully uploaded.' %
                               response['id']))
                        UPLOAD_STATUS = True
                    else:
                        exit('The upload failed with an unexpected response: %s' % response)
            except HttpError as e:
                if e.resp.status in RETRIABLE_STATUS_CODES:
                    error = 'A retriable HTTP error %d occurred:\n%s' % (e.resp.status,
                                                                         e.content)
                else:
                    raise
            except RETRIABLE_EXCEPTIONS as e:
                error = 'A retriable error occurred: %s' % e

            if error is not None:
                print(error)
                retry += 1
                if retry > MAX_RETRIES:
                    return False

                max_sleep = 2 ** retry
                sleep_seconds = random.random() * max_sleep
                print('Sleeping %f seconds and then retrying...' % sleep_seconds)
                time.sleep(sleep_seconds)
        return True

    def set_video_thumbnail(self, thumbnail_path, video=None, video_id=None):
        if video is not None:
            video_id = video.get_video_id()

        self.channel.thumbnails().set(
            videoId=video_id,
            media_body=thumbnail_path
            )

                
