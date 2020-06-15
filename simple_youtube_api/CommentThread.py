from pyser import SchemaJSON, DeserField, DeserObjectField
from simple_youtube_api.name_converter import u_to_c
from simple_youtube_api.Comment import Comment, CommentSchema


class CommentThreadSchema(SchemaJSON):
    def __init__(self):
        self.etag = DeserField()
        self.id = DeserField()

        # snippet
        self.channel_id = DeserField(
            name_conv=u_to_c, optional=True, parent_keys=["snippet"]
        )
        self.video_id = DeserField(
            name_conv=u_to_c, optional=True, parent_keys=["snippet"]
        )
        self.top_level_comment = DeserObjectField(
            name_conv=u_to_c, kind=Comment, schema=CommentSchema,
            parent_keys=["snippet"]
        )
        self.can_reply = DeserField(
            name_conv=u_to_c, parent_keys=["snippet"]
        )
        self.total_reply_count = DeserField(
            name_conv=u_to_c, parent_keys=["snippet"]
        )
        self.is_public = DeserField(
            name_conv=u_to_c, parent_keys=["snippet"]
        )
        self.replies = DeserObjectField(
            name="comments",
            optional=True,
            kind=Comment,
            schema=CommentSchema,
            parent_keys=["replies"],
            repeated=True,
        )


class CommentThread():
    """
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
     """

    def __init__(self):
        self.etag = None
        self.id = None

        # snippet
        self.channel_id = None
        self.video_id = None
        self.top_level_comment = None
        self.can_reply = None
        self.total_reply_count = None
        self.is_public = None
        self.replies = None

    def __str__(self):
        if self.top_level_comment is not None:
            return self.top_level_comment.text_original
        else:
            return "None"
