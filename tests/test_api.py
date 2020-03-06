"""
Tests for API handlers

"""
import pytest
from fastapi.testclient import TestClient
from requests import Response

from app.application import app


@pytest.fixture(scope='module', autouse=True)
def client():
    return TestClient(app)


def test_not_found(client):
    response: Response = client.get('/noexist')
    assert response.status_code == 404


def test_hello_world(client):
    response: Response = client.get('/hello/world')
    parsed_data = response.json()
    assert response.status_code == 200
    assert parsed_data.get('hello') == 'world'
