import json
f = open("languages.json")

data = json.load(f)

languages = []

for item in data["items"]:
    language = item["snippet"]["name"]
    languages.append(language)

o = open("youtube_supported_languages.txt", "w")
o.write(str(languages))
