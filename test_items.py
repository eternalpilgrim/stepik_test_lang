import pytest
import time

class TestItemPage():
    def test_btn_addToBasket(self, browser):
        browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
        time.sleep(3)
        btn_addToBasket = browser.find_element_by_css_selector(".btn-add-to-basket")
        assert btn_addToBasket.is_displayed() is True, "Должна быть кнопка добавления в корзину" 