import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200


def test_create_task():
    response = client.post("/tasks", json={"title": "Buy groceries"})
    assert response.status_code == 201
    data = response.json()
    assert data["title"] == "Buy groceries"
    assert data["done"] is False


def test_get_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)


def test_get_task_not_found():
    response = client.get("/tasks/9999")
    assert response.status_code == 404


def test_update_task():
    # Create first
    res = client.post("/tasks", json={"title": "Fix bug"})
    task_id = res.json()["id"]
    # Update it
    response = client.put(f"/tasks/{task_id}", json={"done": True})
    assert response.status_code == 200
    assert response.json()["done"] is True


def test_delete_task():
    res = client.post("/tasks", json={"title": "To delete"})
    task_id = res.json()["id"]
    response = client.delete(f"/tasks/{task_id}")
    assert response.status_code == 204
