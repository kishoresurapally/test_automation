from pymongo import MongoClient



def create_mongo_client(username, password, mongo_url, db):
    return MongoClient(f"mongodb+srv://{username}:{password}@{mongo_url}/{db}")
    
def get_mongo_db(client, db):
    return client[db]

def get_mongo_collection(db, collection):
    return db[collection]