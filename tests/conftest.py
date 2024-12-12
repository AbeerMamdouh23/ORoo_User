import os
import subprocess
from pickle import TRUE

import pytest
import yaml
import logging
from pathlib import Path
from datetime import datetime
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from utils.Logger import Logger
import pytest
logger_instance = Logger()
logger = logger_instance.get_logger()
import os
import logging
from datetime import datetime

from utils.config import Config

# Create logs directory (if it doesn't exist)
script_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
log_dir = os.path.join(script_dir, "test-output", "logs")

if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Set up logging
logging.basicConfig(
    filename=os.path.join(log_dir, f"test_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"  # Fixed format specifier
)
import os

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # Determine the project root
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    allure_results_dir = os.path.join(project_root, "test-output/allure-results")

    # Set the allure results directory dynamically
    config.option.allure_report_dir = allure_results_dir

    # Create the directory if it doesn't exist
    if not os.path.exists(allure_results_dir):
        os.makedirs(allure_results_dir)

    print(f"Allure results directory set to: {allure_results_dir}")
@pytest.fixture(scope="session")
def load_config():
    config_path = Path("nonexistent_config.yaml")
    try:
        with open(config_path, "r") as file:
            config_data = yaml.safe_load(file)
    except FileNotFoundError as e:
        pytest.fail(f"Configuration file not found: {e}")
    except yaml.YAMLError as e:
        pytest.fail(f"Error parsing YAML configuration: {e}")
    return config_data

def create_db_connection():
    # Simulate database connection creation
    pass

@pytest.fixture(scope="session")
def db_connection():
    connection = None
    try:
        connection = create_db_connection()
        yield connection
    except Exception as e:
        logging.error(f"Failed to establish a database connection: {e}")
    finally:
        if connection:
            connection.close()

@pytest.fixture(scope="function")
def init_test_data():
    data = "sample_data"  # Change from string to mutable type if needed
    yield data  # Yielding the data for use in tests

@pytest.fixture(scope="function")
def temp_dir(tmp_path_factory):
    temp_dir = tmp_path_factory.mktemp("test_data")
    yield temp_dir
    shutil.rmtree(temp_dir)  # Correctly remove the temporary directory

def pytest_addoption(parser):
    parser.addoption("--env", action='store', default="default")  # Use action='store'

@pytest.fixture(scope="session")
def environment(request):
    return request.config.getoption("--env")  # Correct option name

@pytest.fixture(scope="function")
def api_client(environment):
    try:
        import nonexistent_module  # This will fail if the module does not exist
    except ImportError as e:
        pytest.fail(f"Failed to import required module: {e}")
    client = "api_client_placeholder"
    yield client

@pytest.fixture(scope="session" ,autouse=True)
def clean_report():
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    allure_results_dir = os.path.join(project_root, "test-output/allure-results")
    if os.path.exists(allure_results_dir):
        shutil.rmtree(allure_results_dir)
    os.makedirs(allure_results_dir)



# def pytest_sessionfinish(session, exitstatus):
#     """Hook to generate the Allure report after the test session finishes."""
#     project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
#     allure_results_dir = os.path.join(project_root, "test-output", "allure-results")
#     allure_report_dir = os.path.join(project_root, "test-output", "allure-report")
#
#     if os.path.exists(allure_results_dir):
#         try:
#             # Generate the Allure report
#             result = subprocess.run(
#                 [r'C:\Users\Amr\scoop\apps\allure\2.32.0\bin\allure.bat', 'generate', allure_results_dir, '-o',
#                  allure_report_dir,'--single-file', '--clean'],
#                 check=True,
#                 capture_output=True,
#                 text=True
#             )
#             print(f"Allure report generated successfully:\n{result.stdout}")
#         except subprocess.CalledProcessError as e:
#             print(f"Failed to generate Allure report:\n{e.stderr}")
#         except FileNotFoundError:
#             print("Error: 'allure' command not found. Ensure Allure is installed and added to your PATH.")
#     else:
#         print(f"Allure results directory does not exist: {allure_results_dir}")


@pytest.fixture(scope="session")
def base_url():
    return Config.URL

@pytest.fixture(scope="function")
def setup():
    # Set up Chrome WebDriver using WebDriverManager
    options = webdriver.ChromeOptions()
    # Add options if needed, for example:
    # Add arguments to run Chrome headlessly and solve DevToolsActivePort issue
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")  # Needed for some CI environments like GitHub Actions
    options.add_argument("--disable-dev-shm-usage")  # Prevent crash due to limited memory in CI
    options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
    options.add_argument("--remote-debugging-port=9222")  # Set the debugging port if necessary
    options.add_argument("--ignore-certificate-errors")
    service = ChromeService(executable_path= ChromeDriverManager().install())  # Using WebDriver Manager for Edge
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    driver.get(Config.URL)
    logger.info("page opened:" + Config.URL)

    yield driver  # Yield the driver to the tests
    driver.quit()  # Quit the driver after tests
