import os
import pytest
from pages.login_page import LoginPage
from utils.config import Config

@pytest.mark.usefixtures("setup")
class TestLogin:

    def test_invalid_login(self):
        # Navigate to the login page
        self.driver.get(Config.URL)

        # Perform login actions with invalid credentials
        login_page = LoginPage(self.driver)
        login_page.enter_username("invalid_user@example.com")
        login_page.enter_password("wrong_password")
        login_page.click_login()

        # Assert and handle screenshot on failure
        assert "Invalid login" in self.driver.page_source, self.save_screenshot("invalid_login_screenshot.png")

    def save_screenshot(self, filename):
        # Create the directory for screenshots if it doesn't exist
        screenshot_dir = r"C:\Users\EGYPT_LAPTOP\PycharmProjects\pythonProject\reporter\screenshots"
        if not os.path.exists(screenshot_dir):
            os.makedirs(screenshot_dir)

        # Save the screenshot
        screenshot_path = os.path.join(screenshot_dir, filename)
        self.driver.save_screenshot(screenshot_path)
        print(f"Screenshot saved at {screenshot_path}")
        return f"Screenshot saved at {screenshot_path}"
