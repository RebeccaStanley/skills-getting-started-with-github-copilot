from fastapi.testclient import TestClient

from src.app import app


client = TestClient(app)


def test_unregister_participant_removes_email_from_activity():
    response = client.post("/activities/Chess Club/unregister?email=michael@mergington.edu")

    assert response.status_code == 200
    assert "michael@mergington.edu" not in response.json()["participants"]


def test_unregister_participant_returns_404_for_unknown_activity():
    response = client.post("/activities/Unknown/unregister?email=test@example.com")

    assert response.status_code == 404
