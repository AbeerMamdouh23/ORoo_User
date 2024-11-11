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
        self.click(self.PROFILE_AVATAR_ICON)

    def check_fname_value(self):
        self.find_element(self.FIRST_NAME_FIELD).text

    def check_lname_value(self):
        self.find_element(self.LAST_NAME_FIELD).text

    def check_email_value(self):
        self.find_element(self.EMAIL_FIELD).text
