from pydantic import BaseModel
from typing import Literal
import uuid


# Defines a data model for candidate information with data validation using Pydantic's BaseModel.
class candidate(BaseModel):
    first_name: str
    last_name: str
    email: str
    UUID: uuid.UUID
    career_level: str
    job_major: str
    years_of_experience: int
    degree_type: str
    skills: list[str]
    nationality: str
    city: str
    salary: int
    gender: Literal["Male", "Female", "Not Specified"]
