from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class DevicePage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    ACTIVATED_DEVICE = (By.XPATH, "(//*[@id='devicesItemDataName'])[1]")
    DEVICE_NAME_FIELD = (By.ID, "deviceDeviceName")
    DEVICE_TYPE_FIELD = (By.ID, "deviceDeviceType")
    DEVICE_ACCOUNT_FIELD = (By.ID, "deviceDeviceAccount")
    DEVICE_ACTIVATION_FIELD = (By.ID, "deviceDeviceActivation")



    def click_activated_device(self):
        self.click(*self.ACTIVATED_DEVICE)

    def check_device_name(self):
        return self.find_element(*self.DEVICE_NAME_FIELD)

    def check_device_type(self):
        return self.find_element(*self.DEVICE_TYPE_FIELD)

    def check_device_account(self):
        return self.find_element(*self.DEVICE_ACCOUNT_FIELD)

    def check_device_activation(self):
        return self.find_element(*self.DEVICE_ACTIVATION_FIELD)

