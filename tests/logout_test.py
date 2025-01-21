import os
import pytest

from pages.login_page import LoginPage
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

        # Initialize the LoginPage object with the driver instance
        (LoginPage(self.driver)
         .login_steps(Config.USERNAME, Config.PASSWORD)
         .assert_success_login())

        # Initialize the LogOutPage object with the driver instance & Perform logout action
        (LogOutPage(self.driver)
         .click_profile_button()
         .click_logout_button()
         .assert_success_logout())

        take_screenshot(self.driver, "logout_screenshot")
