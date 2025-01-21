import allure
from selenium.webdriver.common.by import By

from pages.activated_devices_page import DevicesPage
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    EMAIL_FIELD = (By.ID, "loginFormEmailInput")
    PASSWORD_FIELD = (By.ID, "loginFormPasswordInput")
    LOGIN_BUTTON = (By.ID, "loginFormLoginButton")
    ERROR_MESSAGE = (By.XPATH, "//p[contains(text(), 'Invalid credentials')]")
    HOME_TEXT = (By.ID, "activationLine1")

    @allure.step("Enter Email")
    def enter_email(self, email):
        self.send_text(email, *self.EMAIL_FIELD)
        return self

    @allure.step("Enter Password")
    def enter_password(self, password):
        self.send_text(password, *self.PASSWORD_FIELD)
        return self

    @allure.step("Click on login button")
    def click_login(self):
        self.click(*self.LOGIN_BUTTON)
        return self

    def login_steps(self,email,password):
        self.send_text(email, *self.EMAIL_FIELD)
        self.send_text(password, *self.PASSWORD_FIELD)
        self.click(*self.LOGIN_BUTTON)
        return self


    @allure.step("Validate success login ")
    def assert_success_login(self):
        assert  self.assert_on_login()==False
        return DevicesPage(self.driver)


    @allure.step("Validate fail login ")
    def assert_fail_login(self):
        assert  self.assert_on_login()==True
        return DevicesPage(self.driver)



    def assert_on_login(self):
        try:
            return self.get_error_message().is_displayed()
        except Exception:
            return False


    def get_error_message(self):
        return self.find_element(*self.ERROR_MESSAGE)

    def get_home_text(self):
        return self.find_element(*self.HOME_TEXT)
