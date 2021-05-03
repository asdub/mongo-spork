import os
import pymongo
if os.path.exists("env.py"):
    import env


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "dbOne"
COLLECTION = "celebrities"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected.")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not conncet to MongoDB: %s") % e


conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]

# coll.update_one({'first': 'rocky'}, {"$set": {"last": "hellothere"}})
# coll.delete({'first': 'douglas'})
# coll.update_many({'nationality': 'american'}, {"$set": {"hair_color": "pink"}})

documents = coll.find({'nationality': 'american'})

for doc in documents:
    print(doc)