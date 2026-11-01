import allure
from pages.base_page import BasePage
from locators.login_locators import LoginLocators

class BurgerLoginPage(BasePage):
    @allure.step("Авторизация в системе")
    def login_with_credentials(self, email, password):
        email_input = self.find_element_with_waiting(LoginLocators.EMAIL_FIELD)
        email_input.clear()
        email_input.send_keys(email)
        
        password_input = self.find_element_with_waiting(LoginLocators.PASSWORD_FIELD)
        password_input.clear()
        password_input.send_keys(password)
        
        self.click_via_js(LoginLocators.SUBMIT_LOGIN_BUTTON)
