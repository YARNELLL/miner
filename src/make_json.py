import constants
import json


category_dict = {"pad": 0, "unk": 1}

with open("../data/train/news.tsv", "r") as train_news:
    lines = train_news.readlines()
    for line in lines:
        category = line.split('\t')[constants.CATEGORY].strip()
        if category not in category_dict:
            category_dict[category] = len(category_dict)

# with open("../data/valid/news.tsv", "r") as train_news:
#     lines = train_news.readlines
#     for line in lines:
#         category = line.split('\t')[constants.CATEGORY].strip()
#         if category not in category_dict:
#             category_dict[category] = len(category_dict)

# with open("../data/test/news.tsv", "r") as train_news:
#     lines = train_news.readlines
#     for line in lines:
#         category = line.split('\t')[constants.CATEGORY].strip()
#         if category not in category_dict:
#             category_dict[category] = len(category_dict)

with open("../data/category2id.json", "w") as category2id:
    json.dump(category_dict, category2id)

print("category2id.json生成完毕!")

user_dict = {"pad": 0, "unk": 1}

with open("../data/train/behaviors.tsv", "r") as train_user:
    lines = train_user.readlines()
    for line in lines:
        user = line.split('\t')[constants.USER_ID].strip()
        if user not in user_dict:
            user_dict[user] = len(user_dict)

with open("../data/user2id.json", "w") as user2id:
    json.dump(user_dict, user2id)

print("user2id.json生成完毕!")
