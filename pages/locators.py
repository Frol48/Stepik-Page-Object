from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form") 
    
class ProductPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")
    ADD_TO_BASKET_BUTTON  = ( By . CSS_SELECTOR , "#add_to_basket_form" )
    ADD_PRODUCT_NAME = (By.CSS_SELECTOR, "#messages .alert:nth-child(1) .alertinner strong")
    ADD_PRODUCT_PRICE = ( By . CSS_SELECTOR , "#messages .alertinner p strong")