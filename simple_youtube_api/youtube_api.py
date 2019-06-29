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

SCOPE = ['https://www.googleapis.com/auth/youtube']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
VALID_PRIVACY_STATUS = ('public', 'private', 'unlisted')


# TODO: Implement
def parse_youtube_video(video):
    pass

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
