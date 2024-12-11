from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ProfilePage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    PROFILE_AVATAR = (By.ID, "headerImagesAvatar")
    FULL_NAME_FIELD = (By.ID, "profileProfileName")
    EMAIL_FIELD = (By.ID, "profileProfileEmail")
    PHONE_NUMBER_FIELD = (By.ID, "profileProfilePhone")
    HOME_ADDRESS_FIELD = (By.ID, "profileProfileHome")
    BIRTH_DATE_FIELD = (By.ID, "profileProfileBirth")
    POST_CODE_FIELD = (By.ID, "profileProfilePostcode")
    LOG_OUT_BUTTON = (By.ID, "profileProfileLogOutButton")



    def click_profile_avatar(self):
        self.click(*self.PROFILE_AVATAR)

    def check_full_name(self):
        return self.find_element(*self.FULL_NAME_FIELD)

    def check_email(self):
        return self.find_element(*self.EMAIL_FIELD)

    def check_phone_number(self):
        return self.find_element(*self.PHONE_NUMBER_FIELD)

    def check_home_address(self):
        return self.find_element(*self.HOME_ADDRESS_FIELD)

    def check_birth_date(self):
        return self.find_element(*self.BIRTH_DATE_FIELD)

    def check_post_code(self):
        return self.find_element(*self.POST_CODE_FIELD)

    def check_logout_button(self):
        return self.find_element(*self.LOG_OUT_BUTTON)

    #def check_first_name_value(self):
    #    return self.get_text_from_input(*self.FIRST_NAME_FIELD)

