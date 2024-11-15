import os
from logging import exception
import pytest
from selenium.common import NoSuchElementException, TimeoutException

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
    def test_devices(self, setup):
        self.driver = setup  # Assign the driver from the fixture


        # Initialize the LoginPage object with the driver instance
        login_page = LoginPage(self.driver)
        login_page.login_steps("testuser@email.com", "Testuser@1")

        # Initialize the DevicePage object with the driver instance
        device_page = DevicePage(self.driver)

        # click on manage your devices button
        device_page.click_manage_your_devices()
        try:
            device_page.click_on_view_button()
            assert device_page.get_device_name().is_displayed()
            assert device_page.get_device_type().is_displayed()
            assert device_page.get_device_activation().is_displayed()
            take_screenshot(self.driver, "Activation_devices_screenshot")

        except NoSuchElementException:
            assert device_page.get_no_devices().is_displayed()
            take_screenshot(self.driver, "No_activated_devices_screenshot")


    # Test case for there is no any device
    def test_no_devices(self, setup):
        self.driver = setup  # Assign the driver from the fixture

        # Navigate to the
        self.driver.get(Config.URL)
        logger.info("page opened:" + Config.URL)
        # Initialize the LoginPage object with the driver instance
        login_page = LoginPage(self.driver)
        login_page.login_steps("testuser2@email.com", "Testuser@2")

        # Initialize the DevicePage object with the driver instance
        device_page = DevicePage(self.driver)

        # click on manage your devices button
        device_page.click_manage_your_devices()
        try:
            device_page.click_on_view_button()
            assert device_page.get_device_name().is_displayed()
            assert device_page.get_device_type().is_displayed()
            assert device_page.get_device_activation().is_displayed()
            take_screenshot(self.driver, "Activation_devices_screenshot")

        except TimeoutException:
            assert device_page.get_no_devices().is_displayed()
            take_screenshot(self.driver, "No_activated_devices_screenshot")
