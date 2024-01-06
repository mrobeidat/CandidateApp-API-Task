from fastapi import APIRouter, Query
from ..models.Candidate import candidate
from ..models.User import user
from ..schema.schemas import candidate_serialized_List
from ..setting.database import candidate_collection
from ..setting.database import users_collection
from uuid import UUID
from fastapi.responses import StreamingResponse
import pandas as pd
import io

router = APIRouter()


# Health check route
@router.get("/health")
def health_check():
    return {"status": "ok"}


# Generate a CSV file containing the candidates profiles data
@router.get("/generate-report")
async def generate_report():
    candidates_data = candidate_collection.find()
    candidates_df = pd.DataFrame(list(candidates_data))
    csv_data = candidates_df.to_csv(index=False)

    headers = {
        "Content-Disposition": "attachment; filename=candidates_report.csv",
        "Content-Type": "text/csv",
    }
    return StreamingResponse(io.StringIO(csv_data), headers=headers)


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
        candidates = candidate_serialized_List(candidate_collection.find(query))
    else:
        candidates = candidate_serialized_List(candidate_collection.find())

    return candidates


########### CRUD routes ###########
@router.get("/candidate/{id}")
async def get_candidate(id: str):
    candidate_id = UUID(id)
    candidate = candidate_collection.find_one({"_id": candidate_id}, {"_id": 0})

    if candidate:
        return candidate
    else:
        return "Candidate not found"


@router.post("/candidate")
async def Create_Candidate(Candidate: candidate):
    candidate_collection.insert_one(dict(Candidate))
    return {"message": "Candidate Created successfully"}


@router.put("/candidate/{id}")
async def update_candidate(id: str, Candidate: candidate):
    candidate_collection.find_one_and_update(
        {"_id": UUID(id)}, {"$set": dict(Candidate)}
    )
    return {"message": "Candidate updated successfully"}


@router.delete("/candidate/{id}")
async def delete_candidate(id: str):
    candidate_collection.find_one_and_delete({"_id": UUID(id)})
    return {"message": "Candidate deleted successfully"}


############# Populate the user collection to the database #############
@router.post("/user")
async def Create_User(User: user):
    users_collection.insert_one(dict(User))
    return {"message": "User Created successfully"}
