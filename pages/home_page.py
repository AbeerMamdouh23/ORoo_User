from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "loginButton")

    def enter_username(self, username):
        self.send_keys(username, *self.USERNAME_FIELD)

    def enter_password(self, password):
        self.send_keys(password, *self.PASSWORD_FIELD)

    def click_login(self):
        self.click(*self.LOGIN_BUTTON)