import os

import pytest
import yaml
import logging
from pathlib import Path
from datetime import datetime
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

import os
import logging
from datetime import datetime

# Create logs directory (if it doesn't exist)
log_dir = os.path.join(os.getcwd(), "..", "test-output", "logs")
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

# Set up logging
logging.basicConfig(
    filename=os.path.join(log_dir, f"test_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"  # Fixed format specifier
)

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

@pytest.fixture(scope="function")
def setup():
    # Set up Chrome WebDriver using WebDriverManager
    options = webdriver.ChromeOptions()
    # Add options if needed, for example:
    # options.add_argument("--headless")  # Uncomment for headless mode
    options.add_argument("--ignore-certificate-errors")
    service = ChromeService(executable_path= ChromeDriverManager().install())  # Using WebDriver Manager for Edge
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()

    yield driver  # Yield the driver to the tests
    
    driver.quit()  # Quit the driver after tests
