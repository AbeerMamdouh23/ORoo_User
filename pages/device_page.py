from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class DevicePage(BasePage):
    def __init__(self, driver):
        self.driver = driver

    MANAGE_YOUR_DEVICES_BUTTON = (By.ID, "navbarDeviceItemSelected")
    ACTIVATE_NEW_DEVICE_BUTTON = (By.ID, "devicesActivationButton")
    ACTIVATED_DEVICES = (By.ID, "devicesItemsText")
  # REMOVE_DEVICE_BUTTON = (By.ID, "")
  # REMOVE_MESSAGE = (By.ID, "")
  # ACTIVATE_CODE_FIELD=(By.ID, "")
  # ACTIVATE_BUTTON = (By.ID, "")
  # SUCCESS_MESSAGE = (By.ID, "")
  # ERROR_MESSAGE = (By.ID, "")

    def click_oroo_devices(self):
            self.click(self.MANAGE_YOUR_DEVICES_BUTTON)

    def get_no_devices(self):
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.ACTIVATE_NEW_DEVICE_BUTTON))
            return self.driver.find_element(*self.ACTIVATE_NEW_DEVICE_BUTTON)


    def get_view_devices(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.ACTIVATED_DEVICES))
        return self.driver.find_element(*self.ACTIVATED_DEVICES).text

    """
        def click_activate_new_device(self):
            self.click(self.ACTIVATE_NEW_DEVICE_BUTTON)
    
    
        def click_activated_device(self):
            self.click(self.ACTIVATED_DEVICE)
    
    
        def click_remove_device(self):
            self.click(self.REMOVE_DEVICE_BUTTON)
    
    
        def enter_activation_code(self, code):
                self.send_keys(code,self.ACTIVATE_CODE_FIELD)
    
    
        def click_activate(self):
            self.click(self.ACTIVATE_BUTTON)
    
    
        def get_error_message(self):
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.ERROR_MESSAGE))
            return self.driver.find_element(*self.ERROR_MESSAGE).text
    
    """



