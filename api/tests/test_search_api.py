import allure
import json

from api.helpers.url import BaseSession, requestSession

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
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
    result = json.loads(response.text)
    assert len(result['suggestions']) == EXPECTED_TERMS_COUNT
