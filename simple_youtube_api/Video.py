from simple_youtube_api.youtube_api import (MAX_YOUTUBE_TITLE_LENGTH,
                                            MAX_YOUTUBE_DESCRIPTION_LENGTH,
                                            MAX_YOUTUBE_TAGS_LENGTH,
                                            YOUTUBE_CATEGORIES,
                                            YOUTUBE_LICENCES,
                                            VALID_PRIVACY_STATUS)

from simple_youtube_api.decorators import (video_snippet_set, video_status_set)

import typing
from typing import List, Union


# TODO add variables
class Video(object):

    '''
    Base class for YouTubeVideo and LocalVideo

    Attributes
    -----------

    title
      The title for the video on YouTube

    description
      The description for the video on YouTube

    tags
      The list of tags for the video on YouTube

    category
      The category for the video on YouTube

    default_langualage
      The default language for the video on YouTube WARNING MIGHT NOT WORK
     '''

    def __init__(self):

        # snippet
        self.title = ""
        self.description = ""
        self.tags = []
        self.category = 1
        self.default_language = None
        self.snippet_set = True

        # status
        self.embeddable = None
        self.license = None
        self.privacy_status = None
        self.public_stats_viewable = None
        self.status_set = False

    @video_snippet_set
    def set_title(self, title: str):
        '''Sets title for video and returns an exception if title is invalid
        '''
        if not type(title) is str:
            raise Exception("Title must be a string")
        if len(title) > MAX_YOUTUBE_TITLE_LENGTH:
            raise Exception("Title is too long: " + str(len(title)))
        else:
            self.title = title

    def get_title(self) -> str:
        ''' Returns title of the video
        '''
        return self.title

    @video_snippet_set
    def set_description(self, description: str):
        '''Sets description for video and returns an exception if description
        is invalid
        '''
        if not type(description) is str:
            raise Exception("Description must be a string")
        if len(description) > MAX_YOUTUBE_DESCRIPTION_LENGTH:
            raise Exception("Description is too long: "+str(len(description)))
        else:
            self.description = description

    def get_description(self) -> str:
        ''' Returns description of the video
        '''
        return self.description

    @video_snippet_set
    def set_tags(self, tags: List[str]):
        '''Sets tags to the video and returns an exception if tags are invalid
        '''
        if not type(tags) is list:
            raise Exception("Tags must be a list")
        if len("".join(tags)) > MAX_YOUTUBE_TAGS_LENGTH:
            raise Exception("Tags are too long: " + str(len("".join(tags))))
        else:
            self.tags = tags

    def get_tags(self) -> List[str]:
        ''' Returns tags of the video
        '''
        return self.tags

    @video_snippet_set
    def set_category(self, category: Union[int, str]):
        ''' Sets category for video

        Parameters
        ----------

        category
          Can either be the name of the category or the category id

        '''
        cat_type = type(category)

        if cat_type == int \
           and category in YOUTUBE_CATEGORIES.values():
            self.category = category

        elif type(category) == str \
             and category.lower() in YOUTUBE_CATEGORIES.keys():
            self.category = YOUTUBE_CATEGORIES[category]

        else:
            raise Exception("Not a valid category: " + str(category))

    def get_category(self) -> int:
        ''' Returns category of the video
        '''
        return self.category

    @video_snippet_set
    def set_default_language(self, language: str):
        ''' Sets default language for video
        '''
        if not type(language) is str:
            raise Exception("Language must be a string")
        else:
            self.default_language = language

    def get_default_language(self) -> str:
        ''' Returns default language of the video
        '''
        return self.default_language

    @video_status_set
    def set_embeddable(self, embeddable: bool):
        ''' Specifies if video is embeddable
        '''
        if not type(embeddable) is bool:
            raise Exception("Embeddable must be a boolean")

        else:
            self.embeddable = embeddable

    def get_embeddable(self) -> bool:
        ''' Returns if the video is embeddable
        '''
        return self.embeddable

    @video_status_set
    def set_license(self, license: str):
        ''' Specifies license for video either 'youtube' or 'creativeCommon'
        '''
        if type(license) == str \
           and license in YOUTUBE_LICENCES:
            self.license = license
        else:
            raise Exception("Not a valid license: " + str(license))

    def get_license(self) -> str:
        ''' Returns license of the video
        '''
        return self.license

    @video_status_set
    def set_privacy_status(self, privacy_status: str):
        ''' Set privacy status, either 'private', 'unlisted' or 'public
        '''
        if privacy_status not in VALID_PRIVACY_STATUS:
            raise Exception("Not valid privacy status: " + str(privacy_status))
        else:
            self.privacy_status = privacy_status

    def get_privacy_status(self) -> str:
        ''' Returns privacy status of the video
        '''
        return self.privacy_status

    @video_status_set
    def set_public_stats_viewable(self, viewable: bool):
        ''' Specifies if public stats are viewable
        '''
        if type(viewable) == bool:
            self.public_stats_viewable = viewable
        else:
            raise Exception("Not a valid status: " + str(viewable))

    def get_public_stats_viewable(self) -> bool:
        ''' Returns if the video's public statistics are viewable
        '''
        return self.public_stats_viewable
