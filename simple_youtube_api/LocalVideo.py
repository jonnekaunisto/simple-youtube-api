from simple_youtube_api.Video import Video
import os.path


class LocalVideo(Video):


    def __init__(self, file_path, title="", description="", tags=[],
                 category=1, default_language=None):
        Video.__init__(self)

        self.set_file_path(file_path)
        self.set_title(title)
        self.set_description(description)
        self.set_tags(tags)
        self.set_category(category)
        if not default_language is None:
            self.set_default_language(default_language)

    def set_file_path(self, file_path):
        if file_path is not None and os.path.isfile(file_path):
            self.file_path = file_path
            return True
        else:
            print("File path does not exist")
            self.file_path = None
            return False

    def get_file_path(self):
        return self.file_path


