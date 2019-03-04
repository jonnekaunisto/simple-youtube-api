import json

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Always retry when an apiclient.errors.HttpError with one of these status
# codes is raised.
RETRIABLE_STATUS_CODES = [500, 502, 503, 504]
SCOPE = ['https://www.googleapis.com/auth/youtube.upload']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'


MAX_YOUTUBE_TITLE_LENGTH = 100
MAX_YOUTUBE_DESCRIPTION_LENGTH = 5000
MAX_YOUTUBE_TAGS_LENGTH = 500



VALID_PRIVACY_STATUSES = ('public', 'private', 'unlisted')



class YouTube(object):


   def __init__(self):
      pass

   def login(self, developer_key):
      print(developer_key)

      youtube = build(API_SERVICE_NAME, API_VERSION,
                      cdeveloperKey=developer_key)
