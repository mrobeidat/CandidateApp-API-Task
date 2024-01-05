from fastapi import APIRouter, Query
from models.Candidate import candidate
from schema.schemas import list_serialized
from setting.database import collection_name
from uuid import UUID

router = APIRouter()


# Health check route
@router.get("/health")
def health_check():
    return {"status": "ok"}


# Candidates route
@router.get("/all-candidates")
async def get_candidates(
    search: str = Query(None, title="Search", description="Search candidates by email")
):
    # Search by field value + global search using keywords.
    if search:
        try:
            search_for_int = int(search)
            query = {
                "$or": [
                    {"salary": search_for_int},
                    {"years_of_experience": search_for_int},
                ]
            }
        except ValueError:
            query = {
                "$or": [
                    {"first_name": {"$regex": search, "$options": "i"}},
                    {"last_name": {"$regex": search, "$options": "i"}},
                    {"email": {"$regex": search, "$options": "i"}},
                    {"UUID": {"$regex": search, "$options": "i"}},
                    {"career_level": {"$regex": search, "$options": "i"}},
                    {"job_major": {"$regex": search, "$options": "i"}},
                    {"degree_type": {"$regex": search, "$options": "i"}},
                    {"skills": {"$regex": search, "$options": "i"}},
                    {"nationality": {"$regex": search, "$options": "i"}},
                    {"city": {"$regex": search, "$options": "i"}},
                    {"salary": {"$regex": search, "$options": "i"}},
                    {"gender": {"$regex": search, "$options": "i"}},
                ]
            }
        candidates = list_serialized(collection_name.find(query))
    else:
        candidates = list_serialized(collection_name.find())

    return candidates


########### CRUD routes ###########
@router.get("/candidate/{id}")
async def get_candidate(id: str):
    candidate_id = UUID(id)
    candidate = collection_name.find_one({"_id": candidate_id}, {"_id": 0})

    if candidate:
        return candidate
    else:
        return "Candidate not found"


@router.post("/candidate")
async def Create_Candidate(Candidate: candidate):
    collection_name.insert_one(dict(Candidate))
    return {"message": "Candidate Created successfully"}


@router.put("/candidate/{id}")
async def update_candidate(id: str, Candidate: candidate):
    collection_name.find_one_and_update({"_id": UUID(id)}, {"$set": dict(Candidate)})
    return {"message": "Candidate updated successfully"}


@router.delete("/candidate/{id}")
async def delete_candidate(id: str):
    collection_name.find_one_and_delete({"_id": UUID(id)})
    return {"message": "Candidate deleted successfully"}
