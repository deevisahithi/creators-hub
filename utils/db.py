from pymongo import MongoClient
from config import Config

client = MongoClient(Config.MONGO_URI)

db = client[Config.DATABASE_NAME]

users_collection = db["users"]

profiles_collection = db["profiles"]

posts_collection = db["posts"]

requests_collection = db["requests"]

notifications_collection = db["notifications"]