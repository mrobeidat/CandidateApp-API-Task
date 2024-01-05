from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
DB_URL = os.getenv("DB_URL")

client = MongoClient(
    DB_URL,
    uuidRepresentation="standard",
)

db = client.Candidates_db

candidate_collection = db["Candidates_collection"]

users_collection = db["Users_collection"]
