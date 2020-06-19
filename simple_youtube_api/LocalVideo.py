from simple_youtube_api.Video import Video
import os.path
import typing


class LocalVideo(Video):
    """
    Class for making a video that is uploaded to YouTube

    Attributes
    -----------
    file_path:
      Specifies which file is going to be uploaded

    title:
      The video's title. The property value has a maximum length of 100
      characters and may contain all valid UTF-8 characters except < and >.

    description:
      The video's description. The property value has a maximum length of
      5000 bytes and may contain all valid UTF-8 characters except < and >.

    tags:
      A list of keyword tags associated with the video. Tags may contain
      spaces. The property value has a maximum length of 500 characters.

    category:
      The YouTube video category associated with the video.

    publish_at:
      Specifies when the video will be published
      (the video has to be private for this) Has to be in
      (YYYY-MM-DDThh:mm:ss.sZ) format

    thumbnail_path:
      Specifies which file is going to be set as thumbnail.

    playlist_id
      Specifies which playlist the video gets added onto.
    """

    def __init__(
        self,
        file_path,
        title="",
        description="",
        tags=[],
        category=1,
        default_language=None,
    ):
        Video.__init__(self)

        self.set_file_path(file_path)
        self.set_title(title)
        self.set_description(description)
        self.set_tags(tags)
        self.set_category(category)
        self.publish_at = None
        self.thumbnail_path = None
        self.self_declared_made_for_kids = None
        self.playlist_id = None

        if default_language is not None:
            self.set_default_language(default_language)

    def set_file_path(self, file_path: str):
        """ Specifies which video file is going to be uploaded
        """
        if file_path is not None and os.path.isfile(file_path):
            self.file_path = file_path
        else:
            raise Exception("Not a valid file path: " + str(file_path))

    def set_thumbnail_path(self, thumbnail_path: str):
        """ Specifies which image file is going to be uploaded
        """
        if thumbnail_path is not None and os.path.isfile(thumbnail_path):
            self.thumbnail_path = thumbnail_path
        else:
            raise Exception("Not a valid file path: " + str(thumbnail_path))

    def set_made_for_kids(self, made_for_kids: bool):
        if type(made_for_kids):
            self.self_declared_made_for_kids = made_for_kids
        else:
            raise Exception("Must be a type bool")

    def set_playlist(self, playlist_id):
        if type(playlist_id) is str:
            self.playlist_id = playlist_id
        else:
            raise Exception("playlist_id must be a string")
