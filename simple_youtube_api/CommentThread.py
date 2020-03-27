class CommentThread():
    '''
    Class for CommentThread resource which holds the top level comment and replies

    Attributes
    -----------

    id
      The id of the comment thread
    
    channel_id
        The id of the channel where the comment was posted on

    video_id
        The id of the video where the comment was posted on

    top_level_comment
        Has the comment object of the top level comment

    can_reply
        If it is possible to reply to this comment thread

    total_reply_count
        The total number of replies

    is_public
        If this comment thread is public

    replies
        The list of comment object replies
     '''
    def __init__(self):
        self.id = None
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
