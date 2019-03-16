from simple_youtube_api.Video import Video
import os.path
from simple_youtube_api import youtube_api


#TODO add more functions
class YouTubeVideo(Video):

    def __init__(self, video_id, title="", description="", tags=[], 
                 category=None):
        Video.__init__(self)

        self.video_id = video_id
        self.title = title
        self.description = description
        self.tags = tags
        self.category = category

    def get_video_id(self):
        return self.video_id

    #TODO Implement
    def fetch(self):
        pass

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




    



