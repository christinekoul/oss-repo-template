from pymongo import MongoClient
import datetime
import random
import copy
from pprint import pprint
from bson.objectid import ObjectId

client = MongoClient()
db = client.mongo_db_lab
collection = db.definitions


def random_word_requester():
    definition_list = []
    for definition in collection.find():
        definition_list.append(definition)

    word = random.choice(definition_list)
    timestamp = str(datetime.datetime.isoformat(datetime.datetime.utcnow()))

    collection.update_one({"_id": word["_id"]}, {"$push": {"dates": timestamp}})
    return collection.find_one({"_id": word["_id"]})

if __name__ == '__main__':
    print(random_word_requester())
