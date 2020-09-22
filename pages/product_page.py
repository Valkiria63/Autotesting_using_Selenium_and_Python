from . import base_page
from .base_page import BasePage
from .locators import ProductPageLocators
import time
import math

class ProductPage(BasePage):
    def should_add_product_page(self):
        self.should_add_product_to_basket()
        self.solve_quiz_and_get_code()
        self.should_check_name_product_to_basket()
        self.should_check_price_product_to_basket()

    def should_add_product_to_basket(self):
        button_add_product = self.browser.find_element(*ProductPageLocators.BUTTON_ADD)
        button_add_product.click()

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
        time.sleep(1)

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

