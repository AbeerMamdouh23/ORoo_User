import allure
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


    @allure.step("Enter activation code ")
    def enter_activation_code(self, activation_code):
        self.send_text(activation_code, *self.ACTIVATION_CODE_FIELD)
        return self


    @allure.step("Click activate button")
    def click_activate_button(self):
        self.click(*self.ACTIVATE_NOW_BUTTON)
        return self


    @allure.step("Valid activation code")
    def assert_valid_code(self):
        return self.find_element(*self.SUCCESS_MESSAGE)


    @allure.step("Invalid activation code")
    def assert_invalid_code(self):
        return self.find_element(*self.ERROR_MESSAGE)


    @allure.step("Activated device founded")
    def assert_success_activation(self):
        assert self.assert_on_found_activated_devices() == True
        return self

    @allure.step("No activated devices yet")
    def assert_fail_activation(self):
        assert self.assert_on_found_activated_devices() == False
        return self


    def assert_on_found_activated_devices(self):
        try:
            return self.assert_valid_code().is_displayed()
        except Exception:
            return False