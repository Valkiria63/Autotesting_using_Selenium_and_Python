from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGIST_FORM = (By.CSS_SELECTOR, "#register_form")
class ProductPageLocators():
    BUTTON_ADD = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_PRODUCT_ADD_BASKED = (By.CSS_SELECTOR, ".alert-success strong")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".product_main h1")
    PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    PRICE_ADD_BASKED = (By.CSS_SELECTOR, ".alert-info p strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success strong")