
from pyser import JSONBase, DeserializeField
from simple_youtube_api.name_converter import u_to_c


class Comment(JSONBase):
    '''
    Class for comment resource

    Attributes
    -----------

    etag
        The Etag of this resource.
    id
      The ID that YouTube uses to uniquely identify the comment.

    author_display_name
      The display name of the user who posted the comment.

    author_profile_image_url
      The URL for the avatar of the user who posted the comment.

    author_channel_url
      The URL of the comment author's YouTube channel, if available.

    author_channel_id
      The ID of the comment author's YouTube channel, if available.

    channel_id
        The ID of the YouTube channel associated with the comment.

    video_id
        The ID of the video that the comment refers to. This property is only
        present if the comment was made on a video.
    text_display
        The comment's text. The text can be retrieved in either plain text or
        HTML.

    text_original
        The original, raw text of the comment as it was initially posted or
        last updated. The original text is only returned if it is accessible
        to the authenticated user, which is only guaranteed if the user is
        the comment's author.

    parent_id
        The unique ID of the parent comment. This property is only set if the
        comment was submitted as a reply to another comment.

    can_rate
        This setting indicates whether the current viewer can rate the comment.

    viewer_rating
        The rating the viewer has given to this comment. Note that this
        property does not currently identify dislike ratings, though this
        behavior is subject to change.

    like_counter
        The total number of likes (positive ratings) the comment has received.

    moderation_status
        The moderation status of the comment [heldForReview ,likelySpam,
        published, rejected]

    published_at
        The date and time when the comment was orignally published.

    updated_at
        The date and time when the comment was last updated.

     '''
    def __init__(self):
        super().__init__()

        self.etag = DeserializeField()
        self.id = DeserializeField()

        # snippet
        self.author_display_name = DeserializeField(name_conv=u_to_c, parent_keys=['snippet'])
        self.author_profile_image_url = DeserializeField(name_conv=u_to_c, parent_keys=['snippet'])
        self.author_channel_url = DeserializeField(name_conv=u_to_c, optional=True, parent_keys=['snippet'])
        self.author_channel_id = DeserializeField(name='value', optional=True, parent_keys=['snippet', 'authorChannelId'])

        self.channel_id = DeserializeField(name_conv=u_to_c, optional=True, parent_keys=['snippet'])
        self.video_id = DeserializeField(name_conv=u_to_c, optional=True, parent_keys=['snippet'])
        self.text_display = DeserializeField(name_conv=u_to_c, parent_keys=['snippet'])
        self.text_original = DeserializeField(name_conv=u_to_c, parent_keys=['snippet'])
        self.parent_id = DeserializeField(name_conv=u_to_c, optional=True, parent_keys=['snippet'])
        self.can_rate = DeserializeField(name_conv=u_to_c, parent_keys=['snippet'])
        self.viewer_rating = DeserializeField(name_conv=u_to_c, parent_keys=['snippet'])
        self.like_count = DeserializeField(name_conv=u_to_c, parent_keys=['snippet'])
        self.moderation_status = DeserializeField(name_conv=u_to_c, optional=True, parent_keys=['snippet'])
        self.published_at = DeserializeField(name_conv=u_to_c, parent_keys=['snippet'])
        self.updated_at = DeserializeField(name_conv=u_to_c, parent_keys=['snippet'])
        self.init_deserialize_json()

    def __str__(self):
        return self.text_original
