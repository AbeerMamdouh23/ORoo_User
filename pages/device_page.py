from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DevicePage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    MANAGE_YOUR_DEVICES_BUTTON = (By.ID, "navbarDeviceItemSelected")
    ACTIVATE_NEW_DEVICE_BUTTON = (By.ID, "devicesActivationButton")
    ACTIVATED_DEVICES = (By.ID, "devicesItemsText")
    VIEW_BUTTON = (By.ID,"devicesViewButton")
    DEVICE_NAME = (By.ID, "deviceItemDeviceNameLabel")
    DEVICE_TYPE = (By.ID, "deviceItemDeviceTypeLabel")
    DEVICE_ACTIVATION = (By.ID, "deviceItemDeviceActivationLabel")



    def click_manage_your_devices(self):
            self.click(*self.MANAGE_YOUR_DEVICES_BUTTON)

    def get_no_devices(self):
            return self.find_element(*self.ACTIVATE_NEW_DEVICE_BUTTON)


    def click_on_view_button(self):
        self.click(*self.VIEW_BUTTON)

    def get_view_devices(self):
        return self.get_text(*self.ACTIVATED_DEVICES)

    def get_device_name(self):
        return self.find_element(*self.DEVICE_NAME)

    def get_device_type(self):
        return self.find_element(*self.DEVICE_TYPE)

    def get_device_activation(self):
        return self.find_element(*self.DEVICE_ACTIVATION)