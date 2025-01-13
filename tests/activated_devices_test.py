import os
from logging import exception
import pytest
from selenium.common import NoSuchElementException, TimeoutException

from pages.activated_devices_page import DevicesPage
from pages.login_page import LoginPage
from utils.config import Config
from utils.screenshots import take_screenshot
from utils.Logger import Logger

logger_instance = Logger()
logger = logger_instance.get_logger()


@pytest.mark.usefixtures("setup")  # Ensure this matches the fixture name
class TestDevice:

    # Test case for there is no any device
    def test_devices(self, setup):
        self.driver = setup  # Assign the driver from the fixture


        # Initialize the LoginPage object with the driver instance & assertion
        (LoginPage(self.driver)
         .login_steps(Config.USERNAME, Config.PASSWORD)
         .assert_success_login()
         .assert_existing_devices())
        take_screenshot(self.driver, "Activated_devices_screenshot")



    # Test case for there is no any device
    def test_no_devices(self, setup):
        self.driver = setup  # Assign the driver from the fixture

        # Initialize the LoginPage object with the driver instance
        (LoginPage(self.driver)
         .login_steps("testuser2@email.com", "Testuser@2")
         .assert_success_login()
         .assert_no_activated_devices())
        take_screenshot(self.driver, "No_activated_devices_screenshot")
