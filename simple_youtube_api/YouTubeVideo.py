from simple_youtube_api.Video import Video
from simple_youtube_api import youtube_api
from simple_youtube_api.decorators import (require_channel_auth, require_youtube_auth, require_channel_or_youtube_auth)

from pytube import YouTube as pytube_YouTube

import os.path



#TODO add more functions
class YouTubeVideo(Video):

    def __init__(self, video_id, youtube=None, channel=None):
        Video.__init__(self)

        self.video_id = video_id
        self.youtube = youtube
        self.channel = channel

    def get_video_id(self):
        return self.video_id

    def set_youtube_auth(self, youtube):
        self.youtube = youtube

    def set_channel_auth(self, channel):
        self.channel = channel

    #TODO add more values
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
    @require_channel_auth
    def update(self, title=None):
        body = {"id": self.__video_id, "snippet": {"title": '', "categoryId": 1}}

        if title is not None:
            body["snippet"]["title"] = title
        print(body)
        response = channel.get_login().videos().update(
            body=body,
            part='snippet,status').execute()

        print(response)

    @require_channel_auth
    def rate_video(self, rating):
        if rating in ["like", "dislike", "none"]:
            request = self.channel.videos().rate(
                id="Ks-_Mh1QhMc",
                rating=rating
            )
            request.execute()
        else:
            raise Exception("Not a valid rating:" + str(rating))

    @require_channel_auth
    def like(self):
        self.rate_video("like")

    @require_channel_auth
    def dislike(self):
        self.rate_video("dislike")

    @require_channel_auth
    def remove_rating(self):
        self.rate_video("none")

    def download(self):
        pytube_YouTube('http://youtube.com/watch?v=' + self).streams.first().download()