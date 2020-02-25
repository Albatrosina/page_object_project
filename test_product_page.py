from .pages.product_page import ProductPage
import pytest


@pytest.mark.skip
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9", marks=pytest.mark.xfail)])
def test_guest_can_add_product_to_basket(browser, link):
    # создаём экземпляр класса ProductPage
    product_page = ProductPage(browser, link)
    # открываем страницу
    product_page.open()
    # добавляем продукт в корзину
    product_page.add_product_to_basket()
    # решение задачи на получение скидки
    product_page.solve_quiz_and_get_code()
    # проверка того, что общая стоимость - соответствует стоимости добавленного продукта
    product_page.basket_total_should_be_equal_to_product_price()
    # проверка того, что название купленного товара - соответствует названию в нотифе
    product_page.product_name_added_should_be_correct()


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
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    product_page = ProductPage(browser, link)
    # 1.Открываем страницу товара
    product_page.open()
    # 2.Проверяем, что нет сообщения об успехе
    product_page.guest_should_not_see_success_msg()


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