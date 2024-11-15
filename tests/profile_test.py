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

        # Navigate to the
        self.driver.get(Config.URL)
        logger.info("page opened:" + Config.URL)
        # Initialize the LoginPage object with the driver instance
        login_page = LoginPage(self.driver)
        login_page.login_steps("testuser@email.com", "Testuser@1")

        # Initialize the ProfilePage object with the driver instance
        profile_page = ProfilePage(self.driver)

        # click on profile avatar icon
        profile_page.click_profile_avatar()

        # Assert and handle screenshot on failure of first name
        assert (profile_page.check_first_name_value()== "test")
        # Assert and handle screenshot on failure of last name
        assert (profile_page.check_last_name_value()== "test")
        # Assert and handle screenshot on failure of email
        assert (profile_page.check_email_value()== "testuser@email.com")

        take_screenshot(self.driver, "verify_Profile_screenshot")
