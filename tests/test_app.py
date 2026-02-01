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
    assert response.json() == {'Hello': 'World'}
