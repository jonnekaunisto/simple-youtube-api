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

        #snippet
        self.channel_id = None

    def set_youtube_auth(self, youtube):
        self.youtube = youtube

    def set_channel_auth(self, channel):
        self.channel = channel

    def get_video_id(self):
        return self.video_id
    
    def get_channel_id(self):
        return self.channel_id

    #TODO add more values to be fetched
    #TODO add fetching some values that are only available to channel
    @require_youtube_auth
    def fetch(self, snippet=True, content_details=False, status=False,
                    statistics=False, player=False, topic_details= False,
                    recording_details=False, file_details=False, processing_details=False,
                    suggestions=False, live_streaming_details=False, localizations=False,
                    all_parts=False):

        parts_list = []

        if snippet or all_parts:
            parts_list.append('snippet')
        if status or all_parts:
            parts_list.append('status')
        if statistics or all_parts:
            parts_list.append('statistics')
        if player or all_parts:
            parts_list.append('player')
        if topic_details or all_parts:
            parts_list.append('topicDetails')
        if recording_details or all_parts:
            parts_list.append('recordingDetails')
        if file_details or all_parts:
            #parts_list.append('fileDetails')
            pass
        if processing_details or all_parts:
            #parts_list.append('processingDetails')
            pass
        if suggestions or all_parts:
            #parts_list.append('suggestions')
            pass
        if live_streaming_details or all_parts:
            parts_list.append('liveStreamingDetails')
        if localizations or all_parts:
            parts_list.append('localizations')

        part = ', '.join(parts_list)
        print(part)

        search_response = self.youtube.videos().list(
          part=part,
          id=self.video_id
        ).execute()

        
        for search_result in search_response.get('items', []):
            if search_result['kind'] == 'youtube#video':
                video_id = search_result['id']
                if snippet or all_parts:
                    snippet_result = search_result['snippet']
                    self.channel_id = snippet_result['channelId']
                    self.title = snippet_result['title']
                    self.description = snippet_result['description']
                    self.tags = snippet_result['tags']
                    self.category = snippet_result['categoryId']
                    #self.default_language = snippet_result['defaultLanguage']
                
                if status or all_parts:
                    status_result = search_result['status']
                    self.embeddable = status_result['embeddable']
                    self.license = status_result['license']
                    self.privacy_status = status_result['privacyStatus']
                    self.public_stats_viewable = status_result['publicStatsViewable']

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