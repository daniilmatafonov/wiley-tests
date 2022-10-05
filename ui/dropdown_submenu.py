from selene.support.shared import browser


class DropdownSubMenu:

    @staticmethod
    def get_all_submenu():
        browser.all('#main-header-navbar > ul.navigation-menu-items li.dropdown-submenu')

