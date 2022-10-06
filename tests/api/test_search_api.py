from helpers.url import BaseSession, requestSession


def test_search_api():
    headers = {'User-Agent': 'PostmanRuntime/7.28.4'}
    response = requestSession().get(BaseSession.search_url, headers=headers, params="term=Java")
    assert response.status_code == 200