from simple_youtube_api.YouTube import YouTube

with open("developer_key", "r") as myfile:
    data = myfile.read().replace("\n", "")

developer_key = data

# logging into youtube
youtube = YouTube()
youtube.login(developer_key)

# searching videos with the term
videos = youtube.search("Your Search Term")

# printing results
for video in videos:
    print(video)

# search a specific video
video = youtube.search_by_video_id("Ks-_Mh1QhMc")
print(video)
