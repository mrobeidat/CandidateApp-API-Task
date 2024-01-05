from pydantic import BaseModel
from typing import Literal

class candidate(BaseModel):
    first_name: str
    last_name: str
    email: str
    UUID: str
    career_level: str
    job_major: str
    years_of_experience: int
    degree_type: str
    skills: list[str]
    nationality: str
    city: str
    salary: int
    gender: Literal["Male", "Female", "Not Specified"]
