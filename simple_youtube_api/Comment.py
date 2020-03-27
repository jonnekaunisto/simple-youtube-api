

class Comment(object):
    '''
    Class for comment resource

    Attributes
    -----------

    id
      The id of the comment

    author_display_name
      The display name of the author

    author_profile_image_url
      The url to author profile image

    author_channel_url
      The url to the author channel

    author_channel_id
      The id of the author's channel

    channel_id
        ID of the channel that the comment is posted on

    video_id
        ID of the video that the comment is posted on

    text_display
        The current content of the comment

    text_original
        The original content of the comment

    parent_id
        The id of the parent comment, will be none if the comment is a top level comment

    can_rate
        Specifies if the comment can be like or disliked

    viewer_rating
        Shows if the current account has liked this comment

    like_counter
        The amount of likes on this comment

    moderation_status
        The moderation status of the comment [heldForReview ,likelySpam, published, rejected]
    
    published_at
        The time when the comment was posted

    updated_at
        The time when the comment was updated
    
     '''
    def __init__(self):
        self.etag = None
        self.id = None
        self.author_display_name = None
        self.author_profile_image_url = None
        self.author_channel_url = None
        self.author_channel_id = None
        self.channel_id = None
        self.video_id = None
        self.text_display = None
        self.text_original = None
        self.parent_id = None
        self.can_rate = None
        self.viewer_rating = None
        self.like_counter = None
        self.moderation_status = None
        self.published_at = None
        self.updated_at = None

    def __str__(self):
        return self.text_original
