import argparse
import time
import random
import http.client
import httplib2
import pickle
import os

from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

from oauth2client.client import flow_from_clientsecrets
from oauth2client.tools import run_flow
from oauth2client.file import Storage

DATA_PATH = os.path.dirname(os.path.abspath(__file__))+os.sep + 'data' + os.sep
MAX_YOUTUBE_TITLE_LENGTH = 100
MAX_YOUTUBE_DESCRIPTION_LENGTH = 5000
MAX_YOUTUBE_TAGS_LENGTH = 500
YOUTUBE_CATEGORIES = {'film': 1, 'animation': 1,
                      'autos': 2, 'vehicles': 2,
                      'music': 10,
                      'pets': 15, 'animals': 15,
                      'sports': 17,
                      'short movies': 18,
                      'travel': 19, 'events': 19,
                      'gaming': 20,
                      'videoblogging': 21,
                      'people': 22, 'blogs': 22,
                      'comedy': 23,
                      'entertainment': 24,
                      'news': 25, 'politics': 25,
                      'howto': 26, 'style': 26,
                      'education': 27,
                      'science': 28, 'technology': 28,
                      'nonprofits': 29, 'activism': 29,
                      'movies': 30,
                      'anime': 31, 'animation': 31,
                      'action': 32, 'adventure': 32,
                      'classics': 33,
                      'comedy': 34,
                      'documentary': 35,
                      'drama': 36,
                      'family': 37,
                      'foreign': 38,
                      'horror': 39,
                      'sci-fi': 40, 'fantasy': 40,
                      'thriller': 41,
                      'shorts': 42,
                      'shows': 43,
                      'trailers': 44}

YOUTUBE_LICENCES = ['creativeCommon', 'youtube']


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
SCOPE = ['https://www.googleapis.com/auth/youtube']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
VALID_PRIVACY_STATUS = ('public', 'private', 'unlisted')


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
            status.update({"publishAt": video.embeddable})
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
def resumable_upload(request):
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
                    exit('The upload failed with an unexpected response: %s' % 
                         response)
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


def init_categories(data):
    with open(DATA_PATH + 'categories.pickle', 'rb') as handle:
        return pickle.load(handle)


def parse_categories(data):
    categories = {}
    for item in data["items"]:
        if item["snippet"]["assignable"]:
            category_name = item["snippet"]["title"]
            category_id = item["id"]
            categories[category_name.lower()] = category_id

    path = os.path.dirname(os.path.abspath(__file__)) + os.sep + 'data'
    with open(path + os.sep + 'categories.pickle', 'wb') as handle:
        pickle.dump(categories, handle, protocol=pickle.HIGHEST_PROTOCOL)

    return categories
