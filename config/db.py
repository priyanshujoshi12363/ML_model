from pymongo import MongoClient

MONGO_URL = "mongodb+srv://USERNAME:PASSWORD@cluster0.o4fk3jd.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(MONGO_URL)

db = client["test"]  # change if your DB name is different
drivers_collection = db["drivers"]