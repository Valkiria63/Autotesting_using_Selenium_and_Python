from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_add_product_page(self):
        self.should_add_product_to_basket()
        self.should_check_name_product_to_basket()
        self.should_check_price_product_to_basket()


    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_add_product_to_basket(self):
        button_add_product = self.browser.find_element(*ProductPageLocators.BUTTON_ADD)
        button_add_product.click()


    def should_check_name_product_to_basket(self):
        product_text_elt = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT)
        product_text = product_text_elt.text
        product_text_add_basked_elt = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT_ADD_BASKED)
        product_add_basked_text = product_text_add_basked_elt.text
        assert product_text == product_add_basked_text, "The wrong product was added to the cart"

    def should_check_price_product_to_basket(self):
        price_text_elt = self.browser.find_element(*ProductPageLocators.PRICE)
        price_text = price_text_elt.text
        price_text_add_basked_elt = self.browser.find_element(*ProductPageLocators.PRICE_ADD_BASKED)
        price_add_basked_text = price_text_add_basked_elt.text
        assert price_text == price_add_basked_text, "The wrong price was added to the cart"

    def should_is_disappeared_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "The success message didn't disappear"

