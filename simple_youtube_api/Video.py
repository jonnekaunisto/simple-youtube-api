from simple_youtube_api import youtube_api
from simple_youtube_api.decorators import (video_snippet_set, video_status_set)

#TODO add variables
class Video(object):
  
    '''
      Super class for YouTubeVideo and LocalVideo
      
      Attributes
     -----------
     
     file_path:
       The file path for the video
     
     title:
      The title for the video on YouTube
     
     description:
       The description for the video on YouTube
     
     tags:
       The list of tags that the video is going to have on YouTube
     
     category:
         The category that the video would be on YouTube
         
     '''

    def __init__(self):
        
        #snippet
        self.title = ""
        self.description = ""
        self.tags = []
        self.category = 1
        self.default_language = "English" #implement
        self.snippet_set = True

        #status
        self.embeddable = None #implement
        self.license = None #implement
        self.privacy_status = None #implement
        self.public_stats_viewable = None #implement
        self.publish_at = None #implement (YYYY-MM-DDThh:mm:ss.sZ) format
        self.status_set = False

    @video_snippet_set
    def set_title(self, title):
        if len(title) > youtube_api.MAX_YOUTUBE_TITLE_LENGTH:
            print("Title is too long: " + str(len(title)))
            return False
        else:
            self.title = title
            return True

    def get_title(self):
        return self.title

    @video_snippet_set
    def set_description(self, description):
        if len(description) > youtube_api.MAX_YOUTUBE_DESCRIPTION_LENGTH:
            print("Description is too long: " + str(len(description)))
            return False
        else:
            self.description = description
            return True

    def get_description(self):
        return self.description


    @video_snippet_set
    def set_tags(self, tags):
        """
        Sets tags to the video
        """

        if len("".join(tags)) > youtube_api.MAX_YOUTUBE_TAGS_LENGTH:
            print("Description is too long: " + str(len("".join(tags))))
            return False
        else:
            self.tags = tags
            return True

    def get_tags(self):
        return self.tags


    @video_snippet_set
    def set_category(self, category):
        cat_type = type(category)

        if cat_type == int and category in youtube_api.YOUTUBE_CATEGORIES_ID_LIST:
            self.category = category
            return True

        elif type(category) == str \
             and category.lower() in youtube_api.YOUTUBE_CATEGORIES_DICT.keys():

            self.category = youtube_api.YOUTUBE_CATEGORIES_DICT[category]
            return True
        else:
            print("Not a valid category")
            self.category = None
            return False

    def get_category(self):
        return self.category


    @video_snippet_set
    def set_default_language(self, language):
        if type(language) == str:
            self.default_language = language
            return True
        else:
            print("Not a valid language")
            return False

    def get_default_language(self):
        return self.default_language

    @video_status_set
    def set_embeddable(self, embeddable):
        if(type(embeddable) == bool):
            self.embeddable = embeddable
            return True
        else:
            print("Not valid type")
            return False

    def get_embeddable(self):
        return self.embeddable
        

    @video_status_set
    def set_license(self, license):
        if type(license) == str and license in youtube_api.YOUTUBE_LICENCES_LIST:
            self.license = license
            return True
        else:
            print("Not a valid license")
            return False

    def get_license(self):
        return self.license


    @video_status_set  
    def set_privacy_status(self, privacy_status):
        if privacy_status not in youtube_api.VALID_PRIVACY_STATUSES:
            print("Not a valid privacy status: " + privacy_status)
            return False
        else:
            self.privacy_status = privacy_status
            return True

    def get_privacy_status(self):
        return self.privacy_status


    @video_status_set
    def set_public_stats_viewable(self, boolean):
        if type(boolean) == bool:
            self.public_stats_viewable = boolean
            return True
        else:
            print("Invalid value")
            return False

    def get_public_stats_viewable(self):
        return self.public_stats_viewable


    def set_publish_at(self, time):
        if type(time) == str:
            self.publish_at = time
            return True
        else:
            print("Invalid Value")
            return False

    def get_publish_at(self):
        return self.publish_at