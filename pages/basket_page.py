from .locators import BasketPageLocators
from .base_page import BasePage


class BasketPage(BasePage):

    def basket_is_empty_text_should_be_present(self):
        assert "Your basket is empty." in self.browser.find_element(*BasketPageLocators.BASKET_PAGE_STATUS).text, \
            "Seems like basket isn't empty"

    def basket_should_not_contain_any_product(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "There are items in the basket!"
