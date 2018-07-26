from pytest import fixture
from app.factory import create_app

@fixture
def client():
    return create_app().test_client()


def test_status_code(client):
    response = client.get('/')
    assert response.status_code == 200


def test_hello_world(client):
    response = client.get('/')
    assert b'Hello, Sebastian!' in response.data


def test_route_destination(client):
    response = client.get('/api/v1/countries/destination')
    assert b'United Kingdom' in response.data
    assert b'Spain' in response.data
    assert b'France' in response.data
    assert b'Ireland' in response.data


def test_route_source(client):
    response = client.get('/api/v1/countries/source')
    assert b'United Kingdom' in response.data
    assert b'Spain' not in response.data
    assert b'France' in response.data
    assert b'Ireland' not in response.data
