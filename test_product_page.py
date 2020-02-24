from .pages.product_page import ProductPage
import pytest

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
    # проверка того, что общая стоимость - соответствует стоимости добавленного продукта
    product_page.basket_total_should_be_equal_to_product_price()
    # проверка того, что название купленного товара - соответствует названию в нотифе
    product_page.product_name_added_should_be_correct()