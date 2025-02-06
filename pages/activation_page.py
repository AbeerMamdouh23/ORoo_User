import os
from pathlib import Path

import allure
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class ActivationPage(BasePage):
    def __init__(self, driver):
        self.driver = driver
        self.activation_code = None  # Store the activation code as an instance variable


    ACTIVATION_CODE_FIELD = (By.ID, "activationItemCode")
    ACTIVATE_NOW_BUTTON = (By.ID, "activationItemButton")
    SUCCESS_MESSAGE = (By.ID, "activatedDeviceTextLine1")
    ERROR_MESSAGE = (By.ID, "activationErrorMessage")


    @allure.step("Enter activation code ")
    def enter_activation_code(self, activation_code):
        self.send_text(activation_code, *self.ACTIVATION_CODE_FIELD)
        return self


    @allure.step("Click activate button")
    def click_activate_button(self):
        self.click(*self.ACTIVATE_NOW_BUTTON)
        return self

    @allure.step("get device activated using API")
    def get_activation_code_using_api(self):
        # Get the project directory dynamically
        project_dir = Path(__file__).parent.parent  # Adjust based on your project structure
        cert_name = "staging.crt"
        key_name = "staging.key"

        # Construct the full paths to the certificate and key files
        cert_path = os.path.join(project_dir,'data', cert_name)
        key_path = os.path.join(project_dir,'data', key_name)

        try:
            # Make the HTTPS request
            response = requests.get(
                "https://device.staging-ooro.co.uk/activation/get_code/TEST-TEST-TEST-1234",
                cert=(cert_path, key_path),
                verify=True  # Ensure SSL verification is enabled
            )

            # Check if the request was successful
            if response.status_code == 200:
                # Parse the JSON response
                response_data = response.json()

                # Check if the response contains the expected data
                if response_data.get("is_success", True) and "data" in response_data:
                    self.activation_code = response_data["data"].get("activation_code")
                    if self.activation_code:
                        return self  # Return the ActivationPage instance
                    else:
                        raise ValueError("Activation code not found in the response data.")
                else:
                    raise ValueError("Invalid response format or unsuccessful request.")
            else:
                raise ValueError(f"Request failed with status code: {response.status_code}")

        except requests.exceptions.SSLError as e:
            print(f"SSL Error: {e}")
        except FileNotFoundError as e:
            print(f"File Not Found Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        return self  # Return the ActivationPage instance even if activation code is None

    @allure.step("get device deactivated using API")
    def get_deactivation_code_using_api(self):
        # Get the project directory dynamically
        project_dir = Path(__file__).parent.parent  # Gets the directory of the current script
        cert_name = "staging.crt"
        key_name = "staging.key"

        # Construct the full paths to the certificate and key files
        cert_path = os.path.join(project_dir,'data', cert_name)
        key_path = os.path.join(project_dir,'data', key_name)

        try:
            # Make the HTTPS request
            response = requests.get(
                "https://device.staging-ooro.co.uk/activation/deactivate/TEST-TEST-TEST-1234",
                cert=(cert_path, key_path),
                verify=True  # Ensure SSL verification is enabled
            )

            # Check if the request was successful
            if response.status_code == 200:
                # Parse the JSON response
                print(response.text)

        except requests.exceptions.SSLError as e:
            print(f"SSL Error: {e}")
        except FileNotFoundError as e:
            print(f"File Not Found Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    @allure.step("Valid activation code")
    def assert_valid_code(self):
        return self.find_element(*self.SUCCESS_MESSAGE)


    @allure.step("Invalid activation code")
    def assert_invalid_code(self):
        return self.find_element(*self.ERROR_MESSAGE)


    @allure.step("Activated device founded")
    def assert_success_activation(self):
        assert self.assert_on_found_activated_devices() == True
        return self

    @allure.step("No activated devices yet")
    def assert_fail_activation(self):
        assert self.assert_on_found_activated_devices() == False
        return self


    def assert_on_found_activated_devices(self):
        try:
            return self.assert_valid_code().is_displayed()
        except Exception:
            return False