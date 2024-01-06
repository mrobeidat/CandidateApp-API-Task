from pydantic import BaseModel
import uuid


# Defines a data model for user information with data validation using Pydantic's BaseModel.
class user(BaseModel):
    first_name: str
    last_name: str
    email: str
    UUID: uuid.UUID
