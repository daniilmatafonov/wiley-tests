import time

import allure
import pytest
from dotenv import load_dotenv
from selene.support.shared import browser

BASE_BROWSER_TIMEOUT=10
SELENE_TIMEOUT=3


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@allure.step('Open page: {path}')
def open_page(path: str):
    browser.open(path)
    time.sleep(1)
