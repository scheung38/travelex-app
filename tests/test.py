import pytest
from splinter import Browser
from src.app import hello_world, returnCountries

# browser = Browser()
# url = 'http://localhost'
url = 'http://127.0.0.1:5000'
# browser.visit(url)
# assert browser.is_text_present("Hello, World Sebastian!")


# @pytest.fixture
def test_query1(client):
    mimetype = 'application/json'
    headers = {
        'Content-Type': mimetype,
        'Accept': mimetype
    }
    # data = {
    #
    # }
    # url = 'localhost'

    response = client.get(url, headers=headers)
    assert response.content_type == mimetype
    assert response.json['Result'] == {'message': 'Hello, World Sebastian!'}
    # assert browser.is_text_present("Hello, World Sebastian!")
    # assert hello_world() == {"message": "Hello, World!"}


# def test_query2():
#     assert returnCountries() == {"message": "Hello, World!"}