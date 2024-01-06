########################## Candidate serialization ##########################
def candidate_serialize(candidate) -> dict:
    return {
        "id": str(candidate["_id"]),
        "first_name": candidate["first_name"],
        "last_name": candidate["last_name"],
        "email": candidate["email"],
        "UUID": candidate["UUID"],
        "career_level": candidate["career_level"],
        "job_major": candidate["job_major"],
        "years_of_experience": candidate["years_of_experience"],
        "degree_type": candidate["degree_type"],
        "skills": candidate["skills"],
        "nationality": candidate["nationality"],
        "city": candidate["city"],
        "salary": candidate["salary"],
        "gender": candidate["gender"],
    }


def candidate_serialized_List(candidates) -> list:
    return [candidate_serialize(candidate) for candidate in candidates]


########################## User serialization ##########################
def user_serialize(user) -> dict:
    return {
        "first_name": user["first_name"],
        "last_name": user["last_name"],
        "email": user["email"],
        "UUID": user["UUID"],
    }


def user_serialized_List(users) -> list:
    return [user_serialize(user) for user in users]
