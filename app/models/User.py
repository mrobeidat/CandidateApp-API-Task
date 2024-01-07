from pydantic import BaseModel
import uuid


# Define a data model for user information using Pydantic BaseModel.
class user(BaseModel):
    first_name: str
    last_name: str
    email: str
    UUID: uuid.UUID


# Define a data model for user creation using Pydantic BaseModel
class UserCreate(BaseModel):
    username: str
    password: str
    first_name: str
    last_name: str
    email: str
    UUID: uuid.UUID
