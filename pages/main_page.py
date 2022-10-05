from selene import have, Collection
from selene.support.shared import browser
from selenium.webdriver import ActionChains


class MainPage:

    def get_subjects(self, name: str):
        element = browser.element("//a[contains(text(),'" + name + "')]")
        action = ActionChains(self)
        action.move_to_element(element).click().perform()
        subjects = browser.elements('#Level1NavNode2 > ul li')
        return subjects

    def subjects_should_have(self, elements: Collection, values: list):
        elements.should(have.text(' '.join(values)))
        return self


