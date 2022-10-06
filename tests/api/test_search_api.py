from helpers.url import BaseSession, requestSession


def test_search_api():
    response = requestSession().get(BaseSession.search_url, params="term=Java")
    assert response.status_code == 200