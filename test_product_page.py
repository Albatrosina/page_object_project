from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage
import pytest


@pytest.mark.skip
@pytest.mark.xfail(reason="Success message is present right after adding the product to basket")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    # 1.Открываем страницу товара
    product_page.open()
    # 2.Добавляем товар в корзину
    product_page.add_product_to_basket()
    # 3.Проверяем, что нет сообщения об успехе
    product_page.should_not_be_success_message()


@pytest.mark.skip
@pytest.mark.xfail(reason="Success msg isn't disappear until user didn't close it")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    # 1. Открываем страницу товара
    product_page.open()
    # 2. Добавляем товар в корзину
    product_page.add_product_to_basket()
    # 3. Проверяем, что нет сообщения об успехе
    product_page.message_should_disappear_after_adding_product_to_basket()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link)
    # 1.Гость открывает страницу товара
    page.open()
    # 2.Переходит в корзину по кнопке в шапке
    page.go_to_basket_page()
    # 3.Ожидаем, что в корзине нет товаров
    page.basket_should_not_contain_any_product()
    # 4.Ожидаем, что есть текст о том что корзина пуста
    page.basket_is_empty_text_should_be_present()


@pytest.mark.test_basket_after_registration
class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.link = "http://selenium1py.pythonanywhere.com/accounts/login/"
        page = LoginPage(browser, self.link)
        page.open()
        email = page.generate_fake_email()
        password = page.generate_fake_password()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        # создаём экземпляр класса ProductPage
        product_page = ProductPage(browser, link)
        # открываем страницу
        product_page.open()
        # добавляем продукт в корзину
        product_page.add_product_to_basket()
        try:
            # решение задачи на получение скидки
            product_page.solve_quiz_and_get_code()
        except:
            # проверка того, что общая стоимость - соответствует стоимости добавленного продукта
            product_page.basket_total_should_be_equal_to_product_price()
            # проверка того, что название купленного товара - соответствует названию в нотифе
            product_page.product_name_added_should_be_correct()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        product_page = ProductPage(browser, link)
        # 1.Открываем страницу товара
        product_page.open()
        # 2.Проверяем, что нет сообщения об успехе
        product_page.guest_should_not_see_success_msg()