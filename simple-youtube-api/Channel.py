import argparse
import http.client
import httplib2
import os
import random
import time
import configparser
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
SCOPE = ['https://www.googleapis.com/auth/youtube.upload']
API_SERVICE_NAME = 'youtube'
API_VERSION = 'v3'
VALID_PRIVACY_STATUSES = ('public', 'private', 'unlisted')



class Channel(object):


    def __init__(self):
        pass

    def login(self, client_secret_path, storage_path):
        STORAGE = Storage(storage_path)
        credentials = STORAGE.get()
        
        if credentials is None or credentials.invalid:
            flow = flow_from_clientsecrets(client_secret_path, scope=SCOPE)
            http = httplib2.Http()
            credentials = run_flow(flow, STORAGE, http=http)
        self.channel = build(API_SERVICE_NAME, API_VERSION, credentials = credentials)
            
