'''Query and update YouTube Video'''
from simple_youtube_api import youtube_api
from simple_youtube_api.decorators import (
    require_channel_auth,
    require_youtube_auth,
)

from .video import Video
from .comment_thread import CommentThread, CommentThreadSchema


# TODO add more functions
class YouTubeVideo(Video):
    ''' Class for YouTube Video

        id
          Video id

        youtube
          YouTube authentication

        channel
          Channel autentication

    '''

    def __init__(self, video_id=None, youtube=None, channel=None):
        Video.__init__(self)

        self.youtube = youtube
        self.channel = channel

        self.id = video_id

        # snippet
        self.channel_id = None

        # status
        self.made_for_kids = None

    def set_youtube_auth(self, youtube):
        """Sets authentication for video
        """
        self.youtube = youtube

    def set_channel_auth(self, channel):
        """Sets channel authenticaton for video
        """
        self.channel = channel

    # TODO add more values to be fetched
    # TODO add fetching some values that are only available to channel
    @require_youtube_auth
    def fetch(
        self,
        snippet=True,
        content_details=False,
        status=False,
        statistics=False,
        player=False,
        topic_details=False,
        recording_details=False,
        file_details=False,
        processing_details=False,
        suggestions=False,
        live_streaming_details=False,
        localizations=False,
        all_parts=False,
    ):
        """Fetches specified parts of video
        """

        parts_list = []
        youtube_perm_parts = [
            (snippet, "snippet"),
            (status, "status"),
            (statistics, "statistics"),
            (player, "player"),
            (topic_details, "topicDetails"),
            (recording_details, "recordingDetails"),
            (live_streaming_details, "liveStreamingDetails"),
            (localizations, "localizations"),
        ]
        channel_perm_parts = [
            (live_streaming_details, "liveStreamingDetails"),
            (processing_details, "processingDetails"),
            (suggestions, "suggestions"),
        ]

        # For youtube authenticated
        for part_tupple in youtube_perm_parts:
            if part_tupple[0] or all_parts:
                parts_list.append(part_tupple[1])

        # For Channel authenticated
        # if False:
        #    for part_tupple in channel_perm_parts:
        #       if part_tupple[0] or all_parts:
        #            parts_list.append(part_tupple[1])

        part = ", ".join(parts_list)
        print(part)

        search_response = (
            self.youtube.videos().list(part=part, id=self.id).execute()
        )

        for search_result in search_response.get("items", []):
            if search_result["kind"] == "youtube#video":
                youtube_api.parse_youtube_video(self, search_result)

    # TODO Finish
    @require_channel_auth
    def update(self, title=None):
        """ Updates a part of video
        """
        body = {
            "id": self.id,
            "snippet": {"title": "", "categoryId": 1},
        }

        if title is not None:
            body["snippet"]["title"] = title
        print(body)
        response = (
            self.channel.get_login()
            .videos()
            .update(body=body, part="snippet,status")
            .execute()
        )

        print(response)

    @require_channel_auth
    def rate_video(self, rating: str):
        """Rates video, valid options are like, dislike and none
        """
        if rating in ["like", "dislike", "none"]:
            request = self.channel.videos().rate(
                id="Ks-_Mh1QhMc", rating=rating
            )
            request.execute()
        else:
            raise Exception("Not a valid rating:" + str(rating))

    @require_channel_auth
    def like(self):
        """Likes video
        """
        self.rate_video("like")

    @require_channel_auth
    def dislike(self):
        """Dislikes video
        """
        self.rate_video("dislike")

    @require_channel_auth
    def remove_rating(self):
        """Removes rating
        """
        self.rate_video("none")

    def fetch_comment_threads(
        self, snippet=True, replies=True
    ) -> CommentThread:
        """Fetches comment threads for video
        """
        parts = ""
        if snippet:
            parts += "snippet"
        if replies:
            parts += ",replies"

        response = (
            self.youtube.commentThreads()
            .list(part=parts, videoId=self.id)
            .execute()
        )

        comment_threads = []
        for item in response.get("items", []):
            comment_thread = CommentThread()
            CommentThreadSchema().from_dict(comment_thread, item)
            comment_threads.append(comment_thread)

        return comment_threads
