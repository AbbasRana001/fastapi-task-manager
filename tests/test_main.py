import pytest
from fastapi.testclient import TestClient
from task_manager_starter import app, tasks_db

client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_db():
    """Clears in-memory storage before every test so tests can't
    leak state into each other or depend on run order."""
    tasks_db.clear()
    yield
    tasks_db.clear()


def test_create_task():
    response = client.post("/tasks", json={"id": 1, "title": "Write tests", "done": False})
    assert response.status_code == 200
    assert response.json()["title"] == "Write tests"


def test_create_duplicate_task_returns_400():
    client.post("/tasks", json={"id": 1, "title": "First"})
    response = client.post("/tasks", json={"id": 1, "title": "Duplicate"})
    assert response.status_code == 400


def test_list_tasks_returns_all():
    client.post("/tasks", json={"id": 1, "title": "Task A"})
    client.post("/tasks", json={"id": 2, "title": "Task B"})
    response = client.get("/tasks")
    assert response.status_code == 200
    assert len(response.json()) == 2


def test_get_missing_task_returns_404():
    response = client.get("/tasks/999")
    assert response.status_code == 404


def test_update_task_changes_only_given_fields():
    client.post("/tasks", json={"id": 1, "title": "Original", "done": False})
    response = client.put("/tasks/1", json={"done": True})
    assert response.status_code == 200
    body = response.json()
    assert body["done"] is True
    assert body["title"] == "Original"  # untouched field stayed the same


def test_delete_task_removes_it():
    client.post("/tasks", json={"id": 1, "title": "To delete"})
    delete_response = client.delete("/tasks/1")
    assert delete_response.status_code == 200
    get_response = client.get("/tasks/1")
    assert get_response.status_code == 404