import os
import time

import pytest

from pages.activation_page import ActivationPage
from pages.login_page import LoginPage
from utils.config import Config
from utils.screenshots import take_screenshot
from utils.Logger import Logger

logger_instance = Logger()
logger = logger_instance.get_logger()


@pytest.mark.usefixtures("setup")  # Ensure this matches the fixture name
class TestLogin:

    def test_valid_login(self, setup):
        self.driver = setup  # Assign the driver from the fixture
        (ActivationPage(self.driver)
         .get_activation_code_using_api())





