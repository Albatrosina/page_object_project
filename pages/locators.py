from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM_ID = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM_ID = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_TO_BASKET = (By.CSS_SELECTOR, "#add_to_basket_form > button")
    SUCCESS_MSG = (By.CSS_SELECTOR, "#messages > div:nth-child(1) > div > strong")
    PROMO_MSG = (By.CSS_SELECTOR, "#messages > div:nth-child(2) > div")
    BASKET_TOTAL = (By.CSS_SELECTOR, "#messages > div.alert.alert-safe.alert-noicon.alert-info.fade.in > div > p:nth-child(1) > strong")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > p.price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, "#content_inner > article > div.row > div.col-sm-6.product_main > h1")


class BasketPageLocators():
    BASKET_PAGE_STATUS = (By.CSS_SELECTOR, "#content_inner > p")
    BASKET_PAGE_LINK = (By.XPATH,
                        '//*[@id="default"]/header/div[1]/div/div[2]/span/a')
    BASKET_ITEMS = (By.CSS_SELECTOR, "#basket_formset > div")