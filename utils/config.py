import os
import time

def take_screenshot(driver, name):
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    screenshot_name = f"{name}_{timestamp}.png"
    screenshot_path = os.path.join("test-output","screenshots", screenshot_name)
    driver.save_screenshot(screenshot_path)




class Config:
    URL = "https://user.ooro.co.uk/"  # Replace with the actual login page URL
    STAGING_URL = ""  # Replace with the actual login page URL
    USERNAME = "user"
    PASSWORD = "password"