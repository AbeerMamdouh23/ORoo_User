import pytest
import logging
import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Create directories for logs and screenshots
log_dir = 'logs'
screenshot_dir = 'screenshots'
for directory in [log_dir, screenshot_dir]:
    if not os.path.exists(directory):
        os.makedirs(directory)

# Set up logging
logging.basicConfig(filename=os.path.join(log_dir, 'test_log.log'),
                    level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')


@pytest.fixture(scope="function")
def setup(request):
    logging.info("Test started")
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    # Set the driver to the test class
    request.cls.driver = driver  # Assign driver to the test class

    yield driver

    # Capture screenshot if test fails
    if request.node.rep_call.failed:
        screenshot_name = os.path.join(screenshot_dir, f"{request.node.name}.png")
        driver.save_screenshot(screenshot_name)
        logging.info(f"Screenshot saved: {screenshot_name}")

    driver.quit()
    logging.info("Test finished")

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # Set the report as an attribute of the item so it can be accessed later
    setattr(item, "rep_" + rep.when, rep)
