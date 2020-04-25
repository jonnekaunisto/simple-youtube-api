import json
import pickle

f = open("categories.json")

data = json.load(f)

categories = {}

for item in data["items"]:
    if item["snippet"]["assignable"]:
        category_name = item["snippet"]["title"]
        category_id = item["id"]
        categories[category_name.lower()] = category_id


with open("categories.pickle", "wb") as handle:
    pickle.dump(categories, handle, protocol=pickle.HIGHEST_PROTOCOL)


with open("categories.pickle", "rb") as handle:
    b = pickle.load(handle)
