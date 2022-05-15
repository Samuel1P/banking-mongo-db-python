from pymongo import MongoClient

class MongoQuery():
    def __init__(self):
       self.mongo_client = MongoClient("mongodb://localhost:27017")

    def connect_db(self, db_name):
        db = self.mongo_client[db_name]
        return db

    @classmethod
    def connect_collection(cls, db, collection_name):
        collection = db[collection_name]
        return collection
