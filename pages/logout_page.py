from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class LogOutPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    LOG_OUT_BUTTON = (By.ID, "navbarLogOutButton")
    LOGIN_BUTTON = (By.ID, "loginFormLoginButton")



def click_logout_button(self):
    self.click(self.LOG_OUT_BUTTON)


def get_login_page(self):
    WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.LOGIN_BUTTON))
    return self.driver.find_element(*self.LOGIN_BUTTON)






