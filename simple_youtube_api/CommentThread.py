from pyser import JSONBase, DeserializeField, DeserializeObjectField
from simple_youtube_api.name_converter import u_to_c
from simple_youtube_api.Comment import Comment


class CommentThread(JSONBase):
    '''
    Class for CommentThread resource which holds the top level comment and
    replies

    Attributes
    -----------

    etag
        The Etag of this resource.

    id
      The ID that YouTube uses to uniquely identify the comment thread.

    channel_id
        The YouTube channel that is associated with the comments in the thread.

    video_id
        The ID of the video that the comments refer to, if any. If this
        property is not present or does not have a value, then the thread
        applies to the channel and not to a specific video.

    top_level_comment
        Has the comment object of the top level comment

    can_reply
        This setting indicates whether the current viewer can reply to the
        thread.

    total_reply_count
        The total number of replies that have been submitted in response to the
        top-level comment.

    is_public
        This setting indicates whether the thread, including all of its
        comments and comment replies, is visible to all YouTube users.

    replies
        The list of comment object replies
     '''
    def __init__(self):
        super().__init__()
        self.etag = DeserializeField()
        self.id = DeserializeField()

        # snippet
        self.channel_id = DeserializeField(name_conv=u_to_c, optional=True, parent_keys=['snippet'])
        self.video_id = DeserializeField(name_conv=u_to_c, optional=True, parent_keys=['snippet'])
        self.top_level_comment = DeserializeObjectField(name_conv=u_to_c, kind=Comment, parent_keys=['snippet'])
        self.can_reply = DeserializeField(name_conv=u_to_c, parent_keys=['snippet'])
        self.total_reply_count = DeserializeField(name_conv=u_to_c, parent_keys=['snippet'])
        self.is_public = DeserializeField(name_conv=u_to_c, parent_keys=['snippet'])
        self.replies = DeserializeObjectField(name='comments', optional=True, kind=Comment, parent_keys=['replies'], repeated=True)

        self.init_deserialize_json()

    def __str__(self):
        if self.top_level_comment is not None:
            return self.top_level_comment.text_original
        else:
            return "None"
