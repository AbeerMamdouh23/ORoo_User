import os
import pytest
from pages.activation_page import ActivationPage
from utils.config import Config
from utils.screenshots import take_screenshot
from utils.Logger import Logger
logger_instance = Logger()
logger = logger_instance.get_logger()

@pytest.mark.usefixtures("setup")  # Ensure this matches the fixture name
class TestActivation:

    # Test case for valid activation code
    def test_valid_activation_code(self, setup):

        self.driver = setup  # Assign the driver from the fixture

        # Navigate to the
        self.driver.get(Config.URL)
        logger.info("page opened:" + Config.URL)

        # Initialize the ActivationPage object with the driver instance
        activation_page = ActivationPage(self.driver)

        # Perform login actions with valid credentials
        activation_page.click_activation_button_no_devices()
        activation_page.enter_activation_code("962455")
        activation_page.click_activate_button()

        # Assert and handle screenshot on failure
        success_message = activation_page.get_success_message()
        assert "Device successfully activated" in success_message
        take_screenshot(self.driver, "valid_activation_code_screenshot")



    # Test case for invalid activation code
    def test_invalid_activation_code(self, setup):

        self.driver = setup  # Assign the driver from the fixture

        # Navigate to the
        self.driver.get(Config.URL)
        logger.info("page opened:" + Config.URL)

        # Initialize the ActivationPage object with the driver instance
        activation_page = ActivationPage(self.driver)

        # Perform login actions with valid credentials
        activation_page.click_activation_button_no_devices()
        activation_page.enter_activation_code("11")
        activation_page.click_activate_button()

        # Assert and handle screenshot on failure
        success_message = activation_page.get_success_message()
        assert "Device successfully activated" in success_message
        take_screenshot(self.driver, "valid_activation_code_screenshot")
