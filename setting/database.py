from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://mrobeidat:yousef9611@cluster0.1pdhgc5.mongodb.net/?retryWrites=true&w=majority",
    uuidRepresentation="standard",
)

db = client.Candidates_db

collection_name = db["Candidates_collection"]
