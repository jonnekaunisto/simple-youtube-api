from simple_youtube_api.YouTube import YouTube

with open('developer_key', 'r') as myfile:
    data = myfile.read().replace('\n', '')

developer_key = data

youtube = YouTube()
youtube.login(developer_key)

youtube.fetch_categories()
