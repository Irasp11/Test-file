from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    # --- действия ---
    def add_product_to_basket(self):
        self.browser.find_element(
            *ProductPageLocators.ADD_TO_BASKET_BUTTON
        ).click()

    # --- геттеры ---
    def get_product_name(self):
        return self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME
        ).text

    def get_product_price(self):
        return self.browser.find_element(
            *ProductPageLocators.PRODUCT_PRICE
        ).text

    def get_message_product_name(self):
        return self.browser.find_element(
            *ProductPageLocators.MESSAGE_PRODUCT_NAME
        ).text

    def get_message_product_price(self):
        return self.browser.find_element(
            *ProductPageLocators.MESSAGE_PRODUCT_PRICE
        ).text

    # --- проверки ---
    def should_be_correct_product_name(self, expected_name):
        actual_name = self.get_message_product_name()
        assert actual_name == expected_name, \
            "Product name in basket does not match product page"

    def should_be_correct_product_price(self, expected_price):
        actual_price = self.get_message_product_price()
        assert actual_price == expected_price, \
            "Product price in basket does not match product page"
