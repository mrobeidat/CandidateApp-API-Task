from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()
DB_URL = os.getenv("DB_URL")

# Connect to MongoDB using DB_URL
client = MongoClient(
    DB_URL,
    uuidRepresentation="standard",
)

# Initialize collections for candidates and users within the "Candidates_db" database
db = client.Candidates_db
candidate_collection = db["Candidates_collection"]
users_collection = db["Users_collection"]
