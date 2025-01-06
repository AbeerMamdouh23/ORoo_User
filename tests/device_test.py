import os
import pytest
from pages.device_page import DevicePage
from pages.login_page import LoginPage
from utils.config import Config
from utils.screenshots import take_screenshot
from utils.Logger import Logger

logger_instance = Logger()
logger = logger_instance.get_logger()


@pytest.mark.usefixtures("setup")  # Ensure this matches the fixture name
class TestDevice:

    # Test case for device data
    def test_device_data(self, setup):
        self.driver = setup  # Assign the driver from the fixture


        # Initialize the LoginPage object with the driver instance
        login_page = LoginPage(self.driver)
        login_page.login_steps(Config.USERNAME, Config.PASSWORD)

        # Initialize the DevicePage object with the driver instance
        device_page = DevicePage(self.driver)
        device_page.click_activated_device()

        # click on manage your devices button
        assert device_page.check_device_name().is_displayed()
        assert device_page.check_device_type().is_displayed()
        assert device_page.check_device_account().is_displayed()
        assert device_page.check_device_activation().is_displayed()

        take_screenshot(self.driver, "Activated_devices_screenshot")


