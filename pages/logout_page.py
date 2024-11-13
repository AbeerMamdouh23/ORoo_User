from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LogOutPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    LOG_OUT_BUTTON = (By.ID, "navbarLogOutButton")
    LOGIN_BUTTON = (By.ID, "loginFormLoginButton")



    def click_logout_button(self):
        self.click(*self.LOG_OUT_BUTTON)


    def get_login_page(self):
        return self.find_element(*self.LOGIN_BUTTON)






