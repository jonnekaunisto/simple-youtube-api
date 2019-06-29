from simple_youtube_api.YouTubeVideo import YouTubeVideo
from simple_youtube_api import youtube_api

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import json

# Always retry when an apiclient.errors.HttpError with one of these status
# codes is raised.
RETRIABLE_STATUS_CODES = [500, 502, 503, 504]
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'


MAX_YOUTUBE_TITLE_LENGTH = 100
MAX_YOUTUBE_DESCRIPTION_LENGTH = 5000
MAX_YOUTUBE_TAGS_LENGTH = 500
VALID_PRIVACY_STATUSES = ('public', 'private', 'unlisted')


class YouTube(object):

    def __init__(self):
        self.youtube = None

    def login(self, developer_key):
        '''Logs into YouTube with credentials
        '''
        self.youtube = build(API_SERVICE_NAME, API_VERSION,
                             developerKey=developer_key)

    def get_login(self):
        '''Gets login object
        '''
        return self.youtube

    def search_raw(self, search_term, max_results=25):
        '''Searches YouTube and returns a JSON response
        '''
        search_response = self.youtube.search().list(
            q=search_term,
            part='snippet',
            maxResults=max_results
        ).execute()

        return search_response

    def search(self, search_term, max_results=25):
        '''Searches YouTube and returns a list of video objects
        '''
        search_response = self.search_raw(search_term, max_results=max_results)

        videos = []
        for search_result in search_response.get('items', []):
            if search_result['id']['kind'] == 'youtube#video':
                video_id = search_result['id']['videoId']
                video_title = search_result['snippet']['title']
                video_description = search_result['snippet']['description']

                video = YouTubeVideo(video_id, youtube=self.youtube)
                video.title = video_title
                video.description = video_description

                videos.append(video)

        return videos

    def search_by_video_id_raw(self, video_id):
        '''Returns a JSON of video
        '''
        search_response = self.youtube.videos().list(
          part='snippet',
          id=video_id
        ).execute()

        return search_response

    def search_by_video_id(self, video_id):
        '''Returns a video object
        '''
        video = YouTubeVideo(video_id, youtube=self.youtube)
        video.fetch()

        return video

    def fetch_categories(self):
        '''Finds all the video categories on YouTube
        '''
        response = self.youtube.videoCategories().list(
          part="snippet",
          regionCode="US"
        ).execute()
        return youtube_api.parse_categories(response)
