from .pages.product_page import ProductPage
import time


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
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