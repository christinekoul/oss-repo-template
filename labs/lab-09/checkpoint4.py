from pymongo import MongoClient
import pprint
from bson.objectid import ObjectId

if __name__ == '__main__':
    client = MongoClient('mongodb://localhost:27017/')
    db = client['mongo_db_lab']
    collection = db['mongo_db_lab.collection']
    print(db.list_collection_names())
    definitions = db.definitions

    print("------------fetch all records------------")
    for definition in definitions.find():
        pprint.pprint(definition)

    print("------------fetch one record------------")
    pprint.pprint(definitions.find_one())

    print("------------fetch a specific record------------")
    pprint.pprint(definitions.find_one({"word": "Squid"}))

    print("------------fetch a record by object id------------")
    pprint.pprint(definitions.find_one({"_id": ObjectId('56fe9e22bad6b23cde07b931')}))

    print("------------insert a new record------------")
    definition = {"word": "dog", "definition": "man's best friend"}
    definition_id = definitions.insert_one(definition).inserted_id
    pprint.pprint(definitions.find_one({"word": "dog"}))
