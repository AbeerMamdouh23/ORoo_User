import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class LogOutPage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    PROFILE_AVATAR = (By.ID, "headerImagesAvatar")
    LOG_OUT_BUTTON = (By.ID, "profileProfileLogOutButton")
    LOGIN_BUTTON = (By.ID, "loginFormLoginButton")



    @allure.step("Click profile avatar")
    def click_profile_button(self):
        self.click(*self.PROFILE_AVATAR)
        return self


    @allure.step("Click logout button")
    def click_logout_button(self):
        self.click(*self.LOG_OUT_BUTTON)
        return self


    @allure.step("Successfully logout")
    def get_login_page(self):
        return self.find_element(*self.LOGIN_BUTTON)


    @allure.step("Success logout ")
    def assert_success_logout(self):
        assert self.assert_on_logout()==True
        return self


    @allure.step("Fail logout ")
    def assert_fail_logout(self):
        assert self.assert_on_logout()==False
        return self


    def assert_on_logout(self):
        try:
            return self.get_login_page().is_displayed()
        except Exception:
            return False





