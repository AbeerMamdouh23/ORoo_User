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
    ERROR_MESSAGE = (By.ID, "loginFormErrorMessage")  # Assuming error message appears here

    def enter_email(self, email):
            self.send_keys(email,self.EMAIL_FIELD)

    def enter_password(self, password):
        self.send_keys(password,self.PASSWORD_FIELD)

    def click_login(self):
        self.click(self.LOGIN_BUTTON)

    def get_error_message(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.ERROR_MESSAGE))
        return self.driver.find_element(*self.ERROR_MESSAGE).text
