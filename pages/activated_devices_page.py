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


    @allure.step("validate success activation ")
    def assert_success_activation(self):
        assert  self.get_view_devices()==True
        return DevicesPage(self.driver)


    @allure.step("validate fail activation ")
    def assert_fail_activation(self):
        assert  self.get_view_devices()==False
        return DevicesPage(self.driver)
