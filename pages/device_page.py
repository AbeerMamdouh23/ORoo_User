from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DevicePage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    CONNECTED_DEVICES = (By.ID, "devicesContainerText")



    def get_view_devices(self):
        try:
            self.find_element(*self.CONNECTED_DEVICES)
            return True
        except Exception:
            return False

