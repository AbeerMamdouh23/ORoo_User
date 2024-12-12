from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ActivationPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    ACTIVATION_CODE_FIELD = (By.ID, "activationItemCode")
    ACTIVATE_NOW_BUTTON = (By.ID, "activationItemButton")
    SUCCESS_MESSAGE = (By.ID, "activatedDeviceTextLine1")
    ERROR_MESSAGE = (By.ID, "activationErrorMessage")



    def enter_activation_code(self, activation_code):
        self.send_text(activation_code, *self.ACTIVATION_CODE_FIELD)


    def click_activate_button(self):
        self.click(*self.ACTIVATE_NOW_BUTTON)


    def get_success_message(self):
        return self.get_text(*self.SUCCESS_MESSAGE)

    def get_error_message(self):
        return self.get_text(*self.ERROR_MESSAGE)

