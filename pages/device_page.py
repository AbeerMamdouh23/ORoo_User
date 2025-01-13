import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.activated_devices_page import DevicesPage
from pages.base_page import BasePage


class DevicePage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    ACTIVATED_DEVICE = (By.XPATH, "(//*[@id='devicesItemDataName'])[1]")
    DEVICE_NAME_FIELD = (By.ID, "deviceDeviceName")
    DEVICE_TYPE_FIELD = (By.ID, "deviceDeviceType")
    DEVICE_ACCOUNT_FIELD = (By.ID, "deviceDeviceAccount")
    DEVICE_ACTIVATION_FIELD = (By.ID, "deviceDeviceActivation")


    @allure.step("Click on activated device")
    def click_activated_device(self):
        self.click(*self.ACTIVATED_DEVICE)
        return self

    @allure.step("This is name of device")
    def assert_device_name(self):
        assert self.find_element(*self.DEVICE_NAME_FIELD)
        return self

    @allure.step("This is type of device")
    def assert_device_type(self):
        assert self.find_element(*self.DEVICE_TYPE_FIELD)
        return self

    @allure.step("This is account of device")
    def assert_device_account(self):
        assert self.find_element(*self.DEVICE_ACCOUNT_FIELD)
        return self

    @allure.step("This is activation of device")
    def assert_device_activation(self):
        assert self.find_element(*self.DEVICE_ACTIVATION_FIELD)
        return self

