import pytest
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home_endpoint(client):
    response = client.get('/')
    assert response.status_code == 200

def test_create_endpoint(client):
    response = client.post('/items', json={"task": "Verify Build"})
    assert response.status_code == 201
    assert b"created" in response.data

def test_retrieve_endpoint(client):
    response = client.get('/items')
    assert response.status_code == 200
    assert b"success" in response.data

def test_update_endpoint(client):
    response = client.put('/items/1', json={"status": "Completed"})
    assert response.status_code == 200
    assert b"updated" in response.data

def test_delete_endpoint(client):
    response = client.delete('/items/1')
    assert response.status_code == 200
    assert b"deleted" in response.data

def test_health_endpoint(client):
    response = client.get('/health')
    assert response.status_code == 200