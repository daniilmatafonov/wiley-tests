from selene import be, Element
from selene.support.shared import browser


class NavigationMenu:
    def __init__(self, element: Element):
        self.element = element

    @staticmethod
    def check_menu_item_is_visible(option: str):
        browser.element("//a[contains(text(),'" + option + "')]").should(be.visible)

