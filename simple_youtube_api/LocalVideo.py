from simple_youtube_api.Video import Video
import os.path
import typing


class LocalVideo(Video):
    '''
    Class for making a video that is uploaded to YouTube

    Attributes
    -----------
    file_path:
      Specifies which file is going to be uploaded

    title:
      Specifies the title for the video

    description:
      Specifies the description for the video

    tags:
      Specifies the tags for the video

    categories:
      Specifies the category for the video

    publish_at:
      Specifies when the video will be published
      (the video has to be private for this) Has to be in
      (YYYY-MM-DDThh:mm:ss.sZ) format

    thumbnail_path:
      Specifies which file is going to be set as thumbnail

    '''
    def __init__(self, file_path, title="", description="", tags=[],
                 category=1, default_language=None):
        Video.__init__(self)

        self.set_file_path(file_path)
        self.set_title(title)
        self.set_description(description)
        self.set_tags(tags)
        self.set_category(category)
        self.publish_at = None
        self.thumbnail_path = None

        if default_language is not None:
            self.set_default_language(default_language)

    def set_file_path(self, file_path: str):
        ''' Specifies which video file is going to be uploaded
        '''
        if file_path is not None and os.path.isfile(file_path):
            self.file_path = file_path
        else:
            raise Exception('Not a valid file path: ' + str(file_path))

    def get_file_path(self) -> str:
        ''' Retuns which video will be uploaded
        '''
        return self.file_path

    def set_thumbnail_path(self, thumbnail_path: str):
        ''' Specifies which image file is going to be uploaded
        '''
        if thumbnail_path is not None and os.path.isfile(thumbnail_path):
            self.thumbnail_path = thumbnail_path
        else:
            raise Exception('Not a valid file path: ' + str(thumbnail_path))

    def get_thumbnail_path(self) -> str:
        ''' Returns the thumbnail path
        '''
        return self.thumbnail_path
