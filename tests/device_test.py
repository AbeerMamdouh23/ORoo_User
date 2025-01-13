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
        (LoginPage(self.driver)
         .login_steps(Config.USERNAME, Config.PASSWORD))

        # Initialize the DevicePage object with the driver instance
        (DevicePage(self.driver)
         .click_activated_device()
         .assert_device_name()
         .assert_device_type()
         .assert_device_account()
         .assert_device_activation())

        take_screenshot(self.driver, "Activated_devices_screenshot")


