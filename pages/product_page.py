from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        basket = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        basket.click()

    def should_have_product_name_in_message(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert self.is_element_with_text_present(*ProductPageLocators.ADD_PRODUCT_NAME, product_name), "Alert has incorrect product name"
           
    def should_have_product_price_in_message(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert self.is_element_with_text_present(*ProductPageLocators.ADD_PRODUCT_PRICE, product_price), "Alert has incorrect product price"
           
    def is_element_with_text_present(self, how, what, text):
        element = self.browser.find_element(how, what)
        find = False
        if element.text==text:
            find = True
        return find