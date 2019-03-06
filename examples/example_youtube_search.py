from simple_youtube_api.YouTube import YouTube

with open('developer_key', 'r') as myfile:
    data=myfile.read().replace('\n', '')

developer_key = data

youtube = YouTube()
youtube.login(developer_key)

videos = youtube.search("Your Search Term")

for video in videos:
	print(video.get_title())

print()


video = youtube.search_by_video_id("Ks-_Mh1QhMc")
print(video.get_title())


