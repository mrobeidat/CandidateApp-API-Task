from fastapi import APIRouter
from models.Candidate import candidate
from schema.schemas import list_serialized
from setting.database import collection_name
from bson import ObjectId

router = APIRouter()


# Health check route
@router.get("/health")
def health_check():
    return {"status": "ok"}


# Candidates route
@router.get("/all-candidates")
async def get_Candidates():
    candidates = list_serialized(collection_name.find())
    return candidates


########### CRUD routes ###########
@router.get("/candidate/{id}")
async def get_candidate(id: str):
    candidate_id = ObjectId(id)
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
    collection_name.find_one_and_update(
        {"_id": ObjectId(id)}, {"$set": dict(Candidate)}
    )
    return {"message": "Candidate updated successfully"}


@router.delete("/candidate/{id}")
async def delete_candidate(id: str):
    collection_name.find_one_and_delete({"_id": ObjectId(id)})
    return {"message": "Candidate deleted successfully"}