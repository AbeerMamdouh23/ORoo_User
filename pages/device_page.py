from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DevicePage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    CONNECTED_DEVICES = (By.ID, "devicesContainerText")
    button = (By.ID, "activationItemButton")




    def get_view_devices(self):
        return self.find_element(*self.CONNECTED_DEVICES)

    def get_view(self):
        return self.find_element(*self.button)