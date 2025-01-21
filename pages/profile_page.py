import allure
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



    @allure.step("Click profile avatar")
    def click_profile_avatar(self):
        self.click(*self.PROFILE_AVATAR)
        return self

    @allure.step("Full Name Field")
    def check_full_name(self):
        assert self.find_element(*self.FULL_NAME_FIELD).is_displayed()
        return self

    @allure.step("Email Field")
    def check_email(self):
        assert self.find_element(*self.EMAIL_FIELD).is_displayed()
        return self

    @allure.step("Phone Number Field")
    def check_phone_number(self):
        assert self.find_element(*self.PHONE_NUMBER_FIELD).is_displayed()
        return self

    @allure.step("Home Address Field")
    def check_home_address(self):
        assert self.find_element(*self.HOME_ADDRESS_FIELD).is_displayed()
        return self

    @allure.step("Birth Date Field")
    def check_birth_date(self):
        assert self.find_element(*self.BIRTH_DATE_FIELD).is_displayed()
        return self

    @allure.step("Post Code Field")
    def check_post_code(self):
        assert self.find_element(*self.POST_CODE_FIELD).is_displayed()
        return self

    @allure.step("Logout Button")
    def check_logout_button(self):
        assert self.find_element(*self.LOG_OUT_BUTTON).is_displayed()
        return self

    #def check_first_name_value(self):
    #    return self.get_text_from_input(*self.FIRST_NAME_FIELD)

