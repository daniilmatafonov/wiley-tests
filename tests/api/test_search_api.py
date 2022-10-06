import allure
import json

from helpers.url import BaseSession, requestSession

headers = {'User-Agent': 'PostmanRuntime/7.28.4'}
EXPECTED_TERMS_COUNT = 4


@allure.description('Search')
@allure.tag('api')
def test_search_api():
    response = requestSession().get(BaseSession.search_url, headers=headers, params="term=Java")
    assert response.status_code == 200


@allure.description('Check terms count')
@allure.tag('api')
def test_check_terms_count():
    response = requestSession().get(BaseSession.search_url, headers=headers, params="term=Java")
    assert response.status_code == 200
    result = json.loads(response.text)
    assert len(result['suggestions']) == EXPECTED_TERMS_COUNT
