import pytest
from fastapi import status
from fastapi.testclient import TestClient

from fastapi_study.app import app


@pytest.fixture
def client():
    return TestClient(app)


def test_read_root(client):
    response = client.get('/')

    assert response.status_code == status.HTTP_200_OK
    assert response.json() == {'message': 'Hello World'}


def test_create_user_return_success(client):
    user_data = {
        'username': 'John Doe',
        'email': 'john.doe@example.com',
        'password': 'securepassword',
    }
    response = client.post('/users', json=user_data)

    assert response.status_code == status.HTTP_201_CREATED
    assert response.json() == {'id': 1, 'username': 'John Doe', 'email': 'john.doe@example.com'}
