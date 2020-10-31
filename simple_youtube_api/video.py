'''Parent class for all Video objects'''

from typing import List, Union

from simple_youtube_api.youtube_constants import (
    MAX_YOUTUBE_TITLE_LENGTH,
    MAX_YOUTUBE_DESCRIPTION_LENGTH,
    MAX_YOUTUBE_TAGS_LENGTH,
    YOUTUBE_CATEGORIES,
    YOUTUBE_LICENCES,
    VALID_PRIVACY_STATUS,
)
from simple_youtube_api.decorators import video_snippet_set, video_status_set


class Video():

    """
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
     """

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
        self.publish_at = None
        self.status_set = False

    @video_snippet_set
    def set_title(self, title: str):
        """Sets title for video and returns an exception if title is invalid
        """
        if not isinstance(title, str):
            raise Exception("Title must be a string")
        if len(title) > MAX_YOUTUBE_TITLE_LENGTH:
            raise Exception("Title is too long: " + str(len(title)))

        self.title = title

    @video_snippet_set
    def set_description(self, description: str):
        """Sets description for video and returns an exception if description
        is invalid
        """
        if not isinstance(description, str):
            raise Exception("Description must be a string")
        if len(description) > MAX_YOUTUBE_DESCRIPTION_LENGTH:
            raise Exception("Description is too long: " + str(len(description)))

        self.description = description

    @video_snippet_set
    def set_tags(self, tags: List[str]):
        """Sets tags to the video and returns an exception if tags are invalid
        """
        if not isinstance(tags, list):
            raise Exception("Tags must be a list")
        if len("".join(tags)) > MAX_YOUTUBE_TAGS_LENGTH:
            raise Exception("Tags are too long: " + str(len("".join(tags))))

        self.tags = tags

    @video_snippet_set
    def set_category(self, category: Union[int, str]):
        """ Sets category for video
        Parameters
        ----------
        category
          Can either be the name of the category or the category id
        """
        cat_type = type(category)

        if cat_type == int and category in YOUTUBE_CATEGORIES.values():
            self.category = category

        elif cat_type == str and category.lower() in YOUTUBE_CATEGORIES.keys():
            self.category = YOUTUBE_CATEGORIES[category]
        else:
            raise Exception("Not a valid category: " + str(category))

    @video_snippet_set
    def set_default_language(self, language: str):
        """ Sets default language for video
        """
        if not isinstance(language, str):
            raise Exception("Language must be a string")

        self.default_language = language

    @video_status_set
    def set_embeddable(self, embeddable: bool):
        """ Specifies if video is embeddable
        """
        if not isinstance(embeddable, bool):
            raise Exception("Embeddable must be a boolean")

        self.embeddable = embeddable

    @video_status_set
    def set_license(self, video_license: str):
        """ Specifies license for video either 'youtube' or 'creativeCommon'
        """
        if isinstance(video_license, str) and video_license in YOUTUBE_LICENCES:
            self.license = video_license
        else:
            raise Exception("Not a valid license: " + str(video_license))

    @video_status_set
    def set_privacy_status(self, privacy_status: str):
        """ Set privacy status, either 'private', 'unlisted' or 'public
        """
        if privacy_status not in VALID_PRIVACY_STATUS:
            raise Exception("Not valid privacy status: " + str(privacy_status))

        self.privacy_status = privacy_status

    @video_status_set
    def set_public_stats_viewable(self, viewable: bool):
        """ Specifies if public stats are viewable
        """
        if isinstance(viewable, bool):
            self.public_stats_viewable = viewable
        else:
            raise Exception("Not a valid status: " + str(viewable))

    #@video_status_set
    def set_publish_at(self, publish_at: Union[datetime.datetime, str]):
        """ Sets time that video is going to be published at in
        (YYYY-MM-DDThh:mm:ss.sZ) format
        """
        if (not isinstance(publish_at, datetime.datetime) and not isinstance(publish_at, str)):
            raise Exception("publish_at must be a datetime object or a string")
        if (self.privacy_status != 'private'):
            raise Exception("In order to be scheduled, the privacy has to be private")
        
        if (isinstance(publish_at, str)):
            publish_at = datetime.date.strptime(publish_at, '%G-%m-%dT%H:%M:%S.000Z')
            if (publish_at >= datetime.datetime.utcnow() and (publish_at.minute == 0 or publish_at.minute == 30)):
                self.publish_at = publish_at
                #print(publish_at)
            else:
                raise Exception("Datetime is in the past or it is not an hour or 30 minute (ex 12:00 or 12:30)")
        else:
            if (publish_at >= datetime.datetime.utcnow() and (publish_at.minute == 0 or publish_at.minute == 30)):
                self.publish_at = publish_at.strftime('%G-%m-%dT%H:%M:%S.000Z')
                #print(publish_at.strftime('%G-%m-%dT%H:%M:%S.000Z'))
            else:
                raise Exception("Datetime is in the past or it is not an hour or 30 minute (ex 12:00 or 12:30)")

    def __str__(self):
        form = "Title: {0}\nDescription: {1}\n Tags:{2}"
        return form.format(self.title, self.description, self.tags)
