from .base_page import BasePage
from .locators import ProductPageLocators
from selenium.common.exceptions import NoAlertPresentException


class ProductPage(BasePage):

    def add_product_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_btn.click()

    def basket_total_should_be_equal_to_product_price(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text == self.browser.find_element(
            *ProductPageLocators.BASKET_TOTAL
        ).text, "Basket total isn't equal to product price"

    def product_name_added_should_be_correct(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == self.browser.find_element(
           *ProductPageLocators.SUCCESS_MSG
        ).text, "Product name in the notification isn't fit the product name added"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MSG), \
            "Success message is presented, but should not be"

    def guest_should_not_see_success_msg(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MSG), \
            "Success message is presented, but should not be"

    def message_should_disappear_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MSG), \
            "Success message isn't disappear, but should be"


