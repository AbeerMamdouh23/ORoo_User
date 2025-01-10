import os
import time

import pytest
from pages.login_page import LoginPage
from utils.config import Config
from utils.screenshots import take_screenshot
from utils.Logger import Logger

logger_instance = Logger()
logger = logger_instance.get_logger()


@pytest.mark.usefixtures("setup")  # Ensure this matches the fixture name
class TestLogin:

    def test_valid_login(self, setup):
        #Test case for valid login with correct credentials using explicit wait
        self.driver = setup  # Assign the driver from the fixture

        # Perform login actions with valid credentials
        (LoginPage(self.driver).enter_email(Config.USERNAME)
         .enter_password(Config.PASSWORD)
         .click_login()
         .assert_success_login())
        take_screenshot(self.driver, "valid_login_screenshot")


    # Test case for invalid login with incorrect credentials using explicit wait
    def test_invalid_login(self, setup):
        self.driver = setup  # Assign the driver from the fixture


        # Perform login actions with invalid credentials
        (LoginPage(self.driver).enter_email("invalid_user@example.com")
        .enter_password("wrong_password")
        .click_login()
        .assert_fail_login())

        # Assert and handle screenshot on failure
        take_screenshot(self.driver, "invalid_login_screenshot")
