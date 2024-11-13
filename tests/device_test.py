import os
from logging import exception

import pytest
from selenium.common import NoSuchElementException

from pages.device_page import DevicePage
from pages.login_page import LoginPage
from utils.config import Config
from utils.screenshots import take_screenshot
from utils.Logger import Logger

logger_instance = Logger()
logger = logger_instance.get_logger()


@pytest.mark.usefixtures("setup")  # Ensure this matches the fixture name
class TestDevice:

    # Test case for there is no any device
    def test_no_devices(self, setup):
        self.driver = setup  # Assign the driver from the fixture

        # Navigate to the
        self.driver.get(Config.URL)
        logger.info("page opened:" + Config.URL)
        # Initialize the LoginPage object with the driver instance
        login_page = LoginPage(self.driver)
        login_page.login_steps("testuser@email.com", "Testuser@1")

        # Initialize the DevicePage object with the driver instance
        device_page = DevicePage(self.driver)

        # click on oroo devices button
        device_page.click_manage_your_devices()
        try:
            device_page.click_on_view_button()
            assert device_page.get_device_name().is_displayed()
            assert device_page.get_device_type().is_displayed()
            assert device_page.get_device_activation().is_displayed()
        except NoSuchElementException:
            assert device_page.get_no_devices().is_displayed()

        take_screenshot(self.driver, "No_devices_screenshot")



"""
    # Test case for there are previous devices
    def test_Review_devices(self, setup):

        self.driver = setup  # Assign the driver from the fixture

        # Navigate to the
        self.driver.get(Config.URL)
        logger.info("page opened:" + Config.URL)
        # Initialize the DevicePage object with the driver instance
        device_page = DevicePage(self.driver)

        # click on oroo devices button
        device_page.click_manage_your_devices()

        # Assert and handle screenshot on failure
        view_devices = device_page.get_view_devices()

        assert "ACTIVATED_DEVICES " in view_devices
        take_screenshot(self.driver, "view_devices_screenshot")"""




