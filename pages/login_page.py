from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "loginButton")
    ERROR_MESSAGE = (By.ID, "errorMessage")  # Assuming the error message has this ID

    def enter_username(self, username):
        self.send_keys(username, *self.USERNAME_FIELD)

    def enter_password(self, password):
        self.send_keys(password, *self.PASSWORD_FIELD)

    def click_login(self):
        self.click(*self.LOGIN_BUTTON)

    def get_error_message(self):
        # Wait until the error message is visible
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.ERROR_MESSAGE)
        )
        return self.find_element(*self.ERROR_MESSAGE).text
