import os
import pytest
from pages.activation_page import ActivationPage
from pages.login_page import LoginPage
from utils.config import Config
from utils.screenshots import take_screenshot
from utils.Logger import Logger
from utils.utils import ActivationCodeManager

logger_instance = Logger()
logger = logger_instance.get_logger()


@pytest.mark.usefixtures("setup")  # Ensure this matches the fixture name
class TestActivation:

    # Test case for valid activation code
    def test_valid_activation_code(self, setup):
        self.driver = setup  # Assign the driver from the fixture

        # Initialize the LoginPage object with the driver instance
        login_page = LoginPage(self.driver)
        login_page.login_steps("testuser@email.com", "Testuser@1")

        # Initialize the ActivationPage object with the driver instance
        activation_page = ActivationPage(self.driver)

        # Perform login actions with valid credentials
        activation_page.click_manage_devices_button()
        activation_page.click_activation_button_existing_devices()
        random_code = ActivationCodeManager.get_random_activation_code('activation_codes.json')
        activation_page.enter_activation_code(random_code)
        activation_page.click_activate_button()
        print(f"Activation code '{random_code}'")
        # Assert and handle screenshot on failure
        assert "Device successfully activated" in activation_page.get_success_message()
        ActivationCodeManager.delete_activation_code('activation_codes.json',random_code)
        take_screenshot(self.driver, "valid_activation_code_screenshot")

    # Test case for invalid activation code
    def test_invalid_activation_code(self, setup):
        self.driver = setup  # Assign the driver from the fixture

        # Navigate to the
        self.driver.get(Config.URL)
        logger.info("page opened:" + Config.URL)
        # Initialize the LoginPage object with the driver instance
        login_page = LoginPage(self.driver)
        login_page.login_steps("testuser@email.com", "Testuser@1")

        # Initialize the ActivationPage object with the driver instance
        activation_page = ActivationPage(self.driver)

        # Perform login actions with valid credentials
        activation_page.click_manage_devices_button()
        activation_page.click_activation_button_existing_devices()
        activation_page.enter_activation_code("11")
        activation_page.click_activate_button()

        # Assert and handle screenshot on failure
        assert "An error has ocurred when activating a device" in activation_page.get_error_message()
        take_screenshot(self.driver, "in_valid_activation_code_screenshot")
