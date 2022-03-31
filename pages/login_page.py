from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login url is not presented"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Login register form is not presented"
        
    def register_new_user(self, email, password):
        imput_email_adress = self.browser.find_element(*LoginPageLocators.INPUT_EMAIL_ADRESS)
        imput_email_adress.send_keys(email)
        imput_password1 = self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD1)
        imput_password1.send_keys(password)
        imput_password2 = self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD2)
        imput_password2.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()