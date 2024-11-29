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
        #Test case for valid login with correct credentials

        self.driver = setup  # Assign the driver from the fixture

        # Navigate to the login page
        self.driver.get("https://www.google.com")
        logger.info("page opened: https://www.google.com")
        take_screenshot(self.driver, "dummy_screenshot")





