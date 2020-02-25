from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import pytest


@pytest.mark.login_guest
class TestLoginFromMainPage:

    def test_guest_can_go_to_login_page(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
        page = MainPage(browser, link)
        # открываем страницу
        page.open()
        # выполняем метод страницы - переходим на страницу логина
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()

    def test_guest_should_see_login_link(self, browser):
        link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = BasketPage(browser, link)
    # 1.Гость открывает главную страницу
    page.open()
    # 2.Переходит в корзину по кнопке в шапке сайта
    page.go_to_basket_page()
    # 3.Ожидаем, что в корзине нет товаров
    page.basket_should_not_contain_any_product()
    # 4.Ожидаем, что есть текст о том что корзина пуста
    page.basket_is_empty_text_should_be_present()



