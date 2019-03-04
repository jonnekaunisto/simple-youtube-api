import os.path


MAX_YOUTUBE_TITLE_LENGTH = 100
MAX_YOUTUBE_DESCRIPTION_LENGTH = 5000
MAX_YOUTUBE_TAGS_LENGTH = 500

#see list of categories in categories.txt
YOUTUBE_CATEGORIES_ID_LIST = (1, 2, 10, 15, 17, 18, 19, 20, 21, 22, 23, 24, 25,
                               26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37,
                               38, 39, 40, 41, 42, 43, 44)

YOUTUBE_CATEGORIES_DICT = {"film": 1, "animation": 1,
                           "autos": 2, "vehicles": 2,
                           "music": 10,
                           "pets": 15, "animals":15,
                           "sports": 17,
                           "short movies": 18,
                           "travel": 19, "events": 19,
                           "gaming": 20,
                           "videoblogging": 21,
                           "people": 22, "blogs":22,
                           "comedy": 23,
                           "entertainment": 24,
                           "news": 25, "politics": 25,
                           "howto": 26, "style": 26,
                           "education": 27,
                           "science": 28, "technology": 28,
                           "nonprofits": 29, "activism": 29,
                           "movies": 30,
                           "anime": 31, "animation":31,
                           "action": 32, "adventure": 32,
                           "classics": 33,
                           "comedy": 34,
                           "documentary": 35,
                           "drama":36,
                           "family": 37,
                           "foreign": 38,
                           "horror": 39,
                           "sci-fi": 40, "fantasy": 40,
                           "thriller": 41,
                           "shorts": 42,
                           "shows": 43,
                           "trailers": 44}

VALID_PRIVACY_STATUSES = ('public', 'private', 'unlisted')


class YouTubeVideo(object):

    def __init__(self, id, title="", description="", tags=[], category=None):
        self.__id = id
        self.__title = title
        self.__description = description
        self.__tags = tags
        self.__category = category
        self.__privacy_status = "public"


    def get_id(self):
        return self.__id

    def get_title(self):
        return self.__title

    def get_description(self):
        return self.__description

    def get_tags(self):
        return self.__tags

    def get_category(self):
        return self.__category

    def get_privacy_status(self):
        return self.privacy_status

