from fastapi.testclient import TestClient
from main import app

client = TestClient(app)
import uuid

# TDD: Test cases for all endpoints

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_generate_report():
    response = client.get("/generate-report")
    assert response.status_code == 200
    assert (
        response.headers["Content-Disposition"]
        == "attachment; filename=candidates_report.csv"
    )


def test_get_candidates():
    response = client.get("/all-candidates")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_candidate():
    # Generate a valid UUID
    candidate_id = str(uuid.uuid4())

    response = client.get(f"/candidate/{candidate_id}")
    assert response.status_code == 200
    # assert "email" in response.json()


def test_create_candidate():
    candidate_data = {
        "first_name": "Samer",
        "last_name": "mohammed",
        "email": "samer@gmail.com",
        "UUID": str(uuid.uuid4()),  # we generate a random uuid here for testing
        "career_level": "Junior",
        "job_major": "Frontend Engineer",
        "years_of_experience": 2,
        "degree_type": "Bachelor's",
        "skills": ["Python", "JavaScript", "SQL"],
        "nationality": "US",
        "city": "New York",
        "salary": 80000,
        "gender": "Male",
    }
    response = client.post("/candidate", json=candidate_data)
    assert response.status_code == 200
    assert response.json() == {"message": "Candidate Created successfully"}


def test_update_candidate():
    candidate_id = str(uuid.uuid4())  # we generate a random uuid here for testing
    updated_candidate_data = {
        "first_name": "Yousef_Updated",
        "last_name": "Obeidat_Updated",
        "email": "yousef_Updated@gmail.com",
        "UUID": str(uuid.uuid4()),
        "career_level": "Senior",
        "job_major": "Backend Engineer",
        "years_of_experience": 3,
        "degree_type": "Bachelor's",
        "skills": ["Python", "JavaScript", "SQL", "MongoDB"],
        "nationality": "Jordanian",
        "city": "Amman",
        "salary": 10000,
        "gender": "Male",
    }
    response = client.put(f"/candidate/{candidate_id}", json=updated_candidate_data)
    assert response.status_code == 200
    assert response.json() == {"message": "Candidate updated successfully"}


def test_delete_candidate():
    candidate_id = str(uuid.uuid4())  # we generate a random uuid here for testing
    response = client.delete(f"/candidate/{candidate_id}")
    assert response.status_code == 200
    assert response.json() == {"message": "Candidate deleted successfully"}
