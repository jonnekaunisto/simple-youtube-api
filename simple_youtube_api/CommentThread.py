class CommentThread():

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
