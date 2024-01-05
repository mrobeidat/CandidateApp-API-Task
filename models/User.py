from pydantic import BaseModel
import uuid

class user(BaseModel):
    first_name: str
    last_name: str
    email: str
    UUID: uuid.UUID
