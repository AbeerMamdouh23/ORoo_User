import os
import time

def take_screenshot(driver, name):
    # Create the 'screenshots' directory if it doesn't exist
    screenshots_dir = os.path.join("reports", "screenshots")
    if not os.path.exists(screenshots_dir):
        os.makedirs(screenshots_dir)

    # Create a unique screenshot name with a timestamp
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    screenshot_name = f"{name}_{timestamp}.png"
    screenshot_path = os.path.join(screenshots_dir, screenshot_name)

    # Save the screenshot to the path
    driver.save_screenshot(
        r"C:\Users\EGYPT_LAPTOP\PycharmProjects\pythonProject\reporter\screenshots")
