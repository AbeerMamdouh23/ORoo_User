from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ActivationPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    ACTIVATE_YOUR_DEVICE_BUTTON_NO_DEVICES = (By.ID, "mainItemsButton")
    ACTIVATE_YOUR_DEVICE_BUTTON_EXISTING_DEVICES = (By.ID, "devicesActivateButton")
    ACTIVATION_CODE_FIELD = (By.ID, "activationItemCode"),
    ACTIVATION_BUTTON = (By.ID, "activationItemButton")
    SUCCESS_MESSAGE = (By.ID, "activationMessage")
    #ERROR_MESSAGE = (By.ID, "")


    def click_activation_button_no_devices(self):
        self.click(self.ACTIVATE_YOUR_DEVICE_BUTTON_NO_DEVICES)


    def click_activation_button_existing_devices(self):
        self.click(self.ACTIVATE_YOUR_DEVICE_BUTTON_EXISTING_DEVICES)


    def enter_activation_code(self, activation_code):
        self.send_keys(activation_code, self.ACTIVATION_CODE_FIELD)


    def click_activate_button(self):
        self.click(self.ACTIVATION_BUTTON)


    def get_success_message(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.SUCCESS_MESSAGE))
        return self.driver.find_element(*self.SUCCESS_MESSAGE).text

'''
    def get_error_message(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.ERROR_MESSAGE))
        return self.driver.find_element(*self.ERROR_MESSAGE).text
'''
