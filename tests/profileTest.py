import os
import pytest
from pages.profile_page import ProfilePage
from utils.config import Config
from utils.screenshots import take_screenshot
from utils.Logger import Logger

logger_instance = Logger()
logger = logger_instance.get_logger()


@pytest.mark.usefixtures("setup")  # Ensure this matches the fixture name
class TestProfile:

    # Test case for viewing profile page data successfully
    def view_profile_data(self, setup):

        self.driver = setup  # Assign the driver from the fixture

        # Navigate to the
        self.driver.get(Config.URL)
        logger.info("page opened:" + Config.URL)
        # Initialize the ProfilePage object with the driver instance
        profile_page = ProfilePage(self.driver)

        # click on profile avatar icon
        profile_page.click_profile_avatar()


        # Assert and handle screenshot on failure of first name
        actual_fname_value = profile_page.check_fname_value()
        self.assertEqual(actual_fname_value, "Test")

        take_screenshot(self.driver, "Correct_Fname_screenshot")


        # Assert and handle screenshot on failure of last name
        actual_lname_value = profile_page.check_lname_value()
        self.assertEqual(actual_lname_value, "User")

        take_screenshot(self.driver, "Correct_Lname_screenshot")


        # Assert and handle screenshot on failure of email
        actual_email_value = profile_page.check_email_value()
        self.assertEqual(actual_email_value, "testuser@email.com")

        take_screenshot(self.driver, "Correct_Email_screenshot")