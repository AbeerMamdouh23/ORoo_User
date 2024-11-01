import os
import pytest
from pages.login_page import LoginPage
from utils.config import Config
from utils.screenshots import take_screenshot
from utils.Logger import Logger
logger_instance = Logger()
logger = logger_instance.get_logger()

@pytest.mark.usefixtures("setup")  # Ensure this matches the fixture name
class TestLogin:


    def test_invalid_login(self, setup):
        """Test case for invalid login with incorrect credentials using explicit wait"""

        self.driver = setup  # Assign the driver from the fixture

        # Navigate to the login page
        self.driver.get(Config.URL)
        logger.info("page opened:" + Config.URL)
        # Initialize the LoginPage object with the driver instance
        login_page = LoginPage(self.driver)

        # Perform login actions with invalid credentials
        login_page.enter_email("invalid_user@example.com")
        login_page.enter_password("wrong_password")
        login_page.click_login()

        # Assert and handle screenshot on failure
        error_message = login_page.get_error_message()
        assert "Invalid credentials" in error_message
        take_screenshot(self.driver,"invalid_login_screenshot")



    