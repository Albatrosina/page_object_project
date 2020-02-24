from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def add_product_to_basket(self):
        add_to_basket_btn = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET)
        add_to_basket_btn.click()
        self.solve_quiz_and_get_code()

    def basket_total_should_be_equal_to_product_price(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text == self.browser.find_element(
            *ProductPageLocators.BASKET_TOTAL
        ).text, "Basket total isn't equal to product price"

    def product_name_added_should_be_correct(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text == self.browser.find_element(
           *ProductPageLocators.BASKET_CONFIRMATION_MSG
        ).text, "Product name in the notification isn't fit the product name added"



