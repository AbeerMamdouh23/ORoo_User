import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DevicesPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    CONNECTED_DEVICES = (By.ID, "devicesContainerText")



    def get_view_devices(self):
        try:
            self.find_element(*self.CONNECTED_DEVICES)
            return True
        except Exception:
            return False


    @allure.step("validate there are activated devices")
    def assert_existing_devices(self):
        assert  self.get_view_devices()==True
        return DevicesPage(self.driver)


    @allure.step("validate no activated devices")
    def assert_no_activated_devices(self):
        assert  self.get_view_devices()==False
        return DevicesPage(self.driver)
