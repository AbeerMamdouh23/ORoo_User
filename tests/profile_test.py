import os
import pytest
from pages.activation_page import ActivationPage
from pages.login_page import LoginPage
from pages.profile_page import ProfilePage
from utils.config import Config
from utils.screenshots import take_screenshot
from utils.Logger import Logger
from utils.utils import ActivationCodeManager

logger_instance = Logger()
logger = logger_instance.get_logger()


@pytest.mark.usefixtures("setup")  # Ensure this matches the fixture name
class TestProfile:

    def test_view_profile(self, setup):
        self.driver = setup  # Assign the driver from the fixture

        # Initialize the LoginPage object with the driver instance
        (LoginPage(self.driver)
         .login_steps(Config.USERNAME, Config.PASSWORD)
         .assert_success_login())

        # Actions & assertions for Profile page
        (ProfilePage(self.driver)
         .click_profile_avatar()
         .check_full_name()
         .check_email()
         .check_phone_number()
         .check_home_address()
         .check_birth_date()
         .check_post_code()
         .check_logout_button())

        take_screenshot(self.driver, "verify_Profile_Page_screenshot")
