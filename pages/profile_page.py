from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ProfilePage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    PROFILE_AVATAR_ICON = (By.ID, "navbarImage")
    FIRST_NAME_FIELD = (By.ID, "profileFormDataInputFirstName")
    LAST_NAME_FIELD = (By.ID, "profileFormDataInputLastName")
    EMAIL_FIELD = (By.ID, "profileFormDataInputEmailAddress")

    def click_profile_avatar(self):
        self.click(*self.PROFILE_AVATAR_ICON)

    def check_first_name_value(self):
        return self.get_text_from_input(*self.FIRST_NAME_FIELD)

    def check_last_name_value(self):
        return self.get_text_from_input(*self.LAST_NAME_FIELD)

    def check_email_value(self):
        return self.get_text_from_input(*self.EMAIL_FIELD)
