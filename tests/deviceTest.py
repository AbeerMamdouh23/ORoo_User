import os
import pytest
from pages.device_page import DevicePage
from utils.config import Config
from utils.screenshots import take_screenshot
from utils.Logger import Logger

logger_instance = Logger()
logger = logger_instance.get_logger()


@pytest.mark.usefixtures("setup")  # Ensure this matches the fixture name
class TestDevice:

    # Test case for there is no any device
    def test_No_devices(self, setup):

        self.driver = setup  # Assign the driver from the fixture

        # Navigate to the
        self.driver.get(Config.URL)
        logger.info("page opened:" + Config.URL)
        # Initialize the DevicePage object with the driver instance
        device_page = DevicePage(self.driver)

        # click on oroo devices button
        device_page.click_oroo_devices()

        # Assert and handle screenshot on failure
        no_devices = device_page.get_no_devices()

        assert "ACTIVATE_NEW_DEVICE_BUTTON" in no_devices
        take_screenshot(self.driver, "No_devices_screenshot")




    # Test case for there are previous devices
    def test_Review_devices(self, setup):

        self.driver = setup  # Assign the driver from the fixture

        # Navigate to the
        self.driver.get(Config.URL)
        logger.info("page opened:" + Config.URL)
        # Initialize the DevicePage object with the driver instance
        device_page = DevicePage(self.driver)

        # click on oroo devices button
        device_page.click_oroo_devices()

        # Assert and handle screenshot on failure
        view_devices = device_page.get_view_devices()

        assert "ACTIVATED_DEVICES " in view_devices
        take_screenshot(self.driver, "view_devices_screenshot")




