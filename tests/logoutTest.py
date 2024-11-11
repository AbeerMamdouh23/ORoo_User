import os
import pytest
from pages.logout_page import LogOutPage
from utils.config import Config
from utils.screenshots import take_screenshot
from utils.Logger import Logger
logger_instance = Logger()
logger = logger_instance.get_logger()


@pytest.mark.usefixtures("setup")  # Ensure this matches the fixture name
class TestLogout:

    def test_logout(self, setup):

        self.driver = setup  # Assign the driver from the fixture

        # Navigate to the login page
        self.driver.get(Config.URL)
        logger.info("page opened:" + Config.URL)

        # Initialize the LogOutPage object with the driver instance
        logout_page = LogOutPage(self.driver)

        # Perform logout action
        logout_page.click_logout_button()

        # Assert and handle screenshot on failure
        login_button_display = logout_page.get_login_page()
        assert login_button_display.is_displayed()
        take_screenshot(self.driver, "logout_screenshot")
