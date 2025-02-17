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
        (LoginPage(self.driver)
         .login_steps(Config.USERNAME, Config.PASSWORD))


        # Perform login actions with valid credentials
        activation_page = ActivationPage(self.driver).get_activation_code_using_api()
        print(activation_page.activation_code)
        (ActivationPage(self.driver)
         .get_activation_code_using_api()
         .enter_activation_code(activation_page.activation_code)
         .click_activate_button()
         .assert_success_activation())
        (ActivationPage(self.driver).get_deactivation_code_using_api())
        take_screenshot(self.driver, "valid_activation_code_screenshot")

    # Test case for invalid activation code
    def test_invalid_activation_code(self, setup):
        self.driver = setup  # Assign the driver from the fixture

        # Initialize the LoginPage object with the driver instance


        (LoginPage(self.driver)
         .login_steps(Config.USERNAME, Config.PASSWORD))

        # Perform login actions with valid credentials
        (ActivationPage(self.driver)
         .enter_activation_code("111")
         .click_activate_button()
         .assert_fail_activation())
        take_screenshot(self.driver, "in_valid_activation_code_screenshot")
