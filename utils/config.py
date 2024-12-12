import os
import time

def take_screenshot(driver, name):
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    screenshot_name = f"{name}_{timestamp}.png"
    screenshot_path = os.path.join("test-output","screenshots", screenshot_name)
    driver.save_screenshot(screenshot_path)




class Config:
    URL = os.getenv("BASE_URL","https://user.dev-ooro.co.uk/")
    USERNAME = "testuser@email.com"
    PASSWORD = "Testuser@1"