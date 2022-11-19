import pytest
from dotenv import load_dotenv

BASE_BROWSER_TIMEOUT=10
SELENE_TIMEOUT=3


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()
