from ui.dropdown_submenu import DropdownSubMenu
from ui.navigation_menu import NavigationMenu


# noinspection PyMethodMayBeStatic
class MainPage:

    def get_header_menu(self):
        menus = DropdownSubMenu().get_all_submenu()

    def item_should_be_visible(self, name: str):
        NavigationMenu(self).check_menu_item_is_visible(name)


