from simple_youtube_api.Video import Video
from simple_youtube_api.CommentThread import CommentThread
from simple_youtube_api import youtube_api
from simple_youtube_api.decorators import (require_channel_auth,
                                           require_youtube_auth,
                                           require_channel_or_youtube_auth)

from pytube import YouTube as pytube_YouTube

import os.path


# TODO add more functions
class YouTubeVideo(Video):

    def __init__(self, video_id, youtube=None, channel=None):
        Video.__init__(self)

        self.video_id = video_id
        self.youtube = youtube
        self.channel = channel

        # snippet
        self.channel_id = None

    def set_youtube_auth(self, youtube):
        '''Sets authentication for video
        '''
        self.youtube = youtube

    def set_channel_auth(self, channel):
        '''Sets channel authenticaton for video
        '''
        self.channel = channel

    def get_video_id(self):
        '''Returns video id
        '''
        return self.video_id

    def get_channel_id(self):
        '''Returns channel id
        '''
        return self.channel_id

    # TODO add more values to be fetched
    # TODO add fetching some values that are only available to channel
    @require_youtube_auth
    def fetch(self, snippet=True, content_details=False, status=False,
              statistics=False, player=False, topic_details=False,
              recording_details=False, file_details=False,
              processing_details=False, suggestions=False,
              live_streaming_details=False, localizations=False,
              all_parts=False):
        '''Fetches specified parts of video
        '''

        parts_list = []
        youtube_perm_parts = [(snippet, 'snippet'), (status, 'status'),
                              (statistics, 'statistics'), (player, 'player'),
                              (topic_details, 'topicDetails'),
                              (recording_details, 'recordingDetails'),
                              (live_streaming_details, 'liveStreamingDetails'),
                              (localizations, 'localizations')]
        channel_perm_parts = [(live_streaming_details, 'liveStreamingDetails'),
                              (processing_details, 'processingDetails'),
                              (suggestions, 'suggestions')]

        # For youtube authenticated
        for part_tupple in youtube_perm_parts:
            if part_tupple[0] or all_parts:
                parts_list.append(part_tupple[1])

        # For Channel authenticated
        if False:
            for part_tupple in channel_perm_parts:
                if part_tupple[0] or all_parts:
                    parts_list.append(part_tupple[1])

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
                    # self.default_language = snippet_result['defaultLanguage']

                if status or all_parts:
                    status_result = search_result['status']
                    self.embeddable = status_result['embeddable']
                    self.license = status_result['license']
                    self.privacy_status = status_result['privacyStatus']
                    self.public_stats_viewable = \
                        status_result['publicStatsViewable']

    # TODO Finish
    @require_channel_auth
    def update(self, title=None):
        '''updates a part of video
        '''
        body = {"id": self.__video_id,
                "snippet": {"title": '', "categoryId": 1}}

        if title is not None:
            body["snippet"]["title"] = title
        print(body)
        response = channel.get_login().videos().update(
            body=body,
            part='snippet,status').execute()

        print(response)

    @require_channel_auth
    def rate_video(self, rating):
        '''Rates video
        '''
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
        '''Likes video
        '''
        self.rate_video("like")

    @require_channel_auth
    def dislike(self):
        '''Dislikes video
        '''
        self.rate_video("dislike")

    @require_channel_auth
    def remove_rating(self):
        '''Removes rating
        '''
        self.rate_video("none")

    def fetch_comment_threads(self, snippet=True, replies=True):
        parts = ''
        if snippet:
            parts += 'snippet'
        if replies:
            parts += ',replies'

        response = self.youtube.commentThreads().list(
            part=parts,
            videoId='_VB39Jo8mAQ'
        ).execute()

        comment_threads = []
        for item in response.get('items', []):
            comment_thread = CommentThread()
            comment_thread = youtube_api.parse_comment_thread(comment_thread,
                                                              item)
            comment_threads.append(comment_thread)

        return comment_threads

    def download(self):
        '''Downloads video
        '''
        video_url = 'https://youtube.com/watch?v=' + self.video_id
        pytube_YouTube(video_url).streams.first().download()
