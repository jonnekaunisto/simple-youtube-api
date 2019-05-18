from simple_youtube_api.Video import Video
from simple_youtube_api import youtube_api

from pytube import YouTube as pytube_YouTube

import os.path



#TODO add more functions
class YouTubeVideo(Video):

    def __init__(self, video_id, youtube):
        Video.__init__(self)

        self.video_id = video_id
        self.youtube = youtube

    def get_video_id(self):
        return self.video_id

    #TODO Implement
    def fetch(self):
        search_response = self.youtube.videos().list(
          part='snippet',
          id=self.video_id
        ).execute()

        
        for search_result in search_response.get('items', []):
            if search_result['kind'] == 'youtube#video':
                video_id = search_result['id']
                video_title = search_result['snippet']['title']
                video_description = search_result['snippet']['description']

                self.title = video_title
                self.description = video_description
                
    #TODO Finish
    def update(self, channel, title=None):
        body = {"id": self.__video_id, "snippet": {"title": '', "categoryId": 1}}

        if title is not None:
            body["snippet"]["title"] = title
        print(body)
        response = channel.get_login().videos().update(
            body=body,
            part='snippet,status').execute()

        print(response)

    def download(self):
        pytube_YouTube('http://youtube.com/watch?v=' + self).streams.first().download()