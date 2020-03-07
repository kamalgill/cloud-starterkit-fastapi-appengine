"""
Tests for API handlers

"""
import pytest
from fastapi.testclient import TestClient
from requests import Response

from app.main import application


@pytest.fixture(scope='module', autouse=True)
def client():
    return TestClient(application)


def test_not_found(client):
    response: Response = client.get('/noexist')
    assert response.status_code == 404


def test_root_path_redirects_to_docs(client):
    response: Response = client.get('/', allow_redirects=False)
    assert response.status_code == 307  # Temporary redirect status code


def test_swagger_ui_docs(client):
    response: Response = client.get('/docs')
    assert response.status_code == 200


def test_redoc_docs(client):
    response: Response = client.get('/redoc')
    assert response.status_code == 200


def test_hello_world(client):
    response: Response = client.get('/hello/world')
    parsed_data = response.json()
    assert response.status_code == 200
    assert parsed_data.get('hello') == 'world'
