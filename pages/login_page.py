from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    EMAIL_FIELD = (By.ID, "loginFormEmailAddress")
    PASSWORD_FIELD = (By.ID, "loginFormPassword")
    LOGIN_BUTTON = (By.CLASS_NAME, "login_formButtons__3UJaC")
    ERROR_MESSAGE = (By.ID, "loginFormErrorMessage")
    DASHBOARD_TEXT = (By.ID, "navbarContainerTitle")

    def enter_email(self, email):
        self.send_text(email, *self.EMAIL_FIELD)

    def enter_password(self, password):
        self.send_text(password, *self.PASSWORD_FIELD)

    def click_login(self):
        self.click(*self.LOGIN_BUTTON)

    def login_steps(self,email,password):
        self.send_text(email, *self.EMAIL_FIELD)
        self.send_text(password, *self.PASSWORD_FIELD)
        self.click(*self.LOGIN_BUTTON)

    def get_error_message(self):
        return self.get_text(*self.ERROR_MESSAGE)

    def get_dashboard_text(self):
        return self.find_element(*self.DASHBOARD_TEXT)
