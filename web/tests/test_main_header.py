import allure

from web.conftest import open_page
from model import application

url = 'https://wiley.com/en-ie'
expectedSubjects = ["Accounting", "Agriculture"],


@allure.description('Who We Serve')
@allure.tag('web')
def test_who_we_serve_menu_is_visible():
    open_page(url)
    application.mainPage.item_should_be_visible('WHO WE SERVE')


@allure.description('Subjects')
@allure.tag('web')
def test_subjects_menu_is_visible():
    open_page(url)
    application.mainPage.item_should_be_visible('SUBJECTS')


@allure.description('The Wiley Network')
@allure.tag('web')
def test_wiley_network_menu_is_visible():
    open_page(url)
    application.mainPage.item_should_be_visible('THE WILEY NETWORK')


@allure.description('About')
@allure.tag('web')
def test_about_menu_is_visible():
    open_page(url)
    application.mainPage.item_should_be_visible('ABOUT')
