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

        # Navigate to the login page
        self.driver.get(Config.URL)
        logger.info("page opened:" + Config.URL)

        # Initialize the LoginPage object with the driver instance
        login_page = LoginPage(self.driver)

        # Perform login actions with valid credentials
        login_page.enter_email(Config.USERNAME)
        login_page.enter_password(Config.PASSWORD)
        login_page.click_login()

        # Assert and handle screenshot on failure
        assert login_page.get_dashboard_text().is_displayed()
        take_screenshot(self.driver, "valid_login_screenshot")


    # Test case for invalid login with incorrect credentials using explicit wait
    def test_invalid_login(self, setup):
        self.driver = setup  # Assign the driver from the fixture

        # Initialize the LoginPage object with the driver instance
        login_page = LoginPage(self.driver)

        # Perform login actions with invalid credentials
        login_page.enter_email("invalid_user@example.com")
        login_page.enter_password("wrong_password")
        login_page.click_login()

        # Assert and handle screenshot on failure
        assert "Invalid credentials" in  login_page.get_error_message()
        take_screenshot(self.driver, "invalid_login_screenshot")
