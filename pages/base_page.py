from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from utils.Logger import  Logger
log = Logger()
logger = log.get_logger()
class BasePage:
    def init(self, driver):
        self.driver = driver

    def find_element(self, *locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    def click(self, *locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator)).click()
        logger.info( f"{locator} clicked")

    def send_text(self, text, *locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).send_keys(text)
        logger.info(text + f" sent to {locator} "  )

    def get_text(self, *locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).text

    def get_text_from_input(self, *locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).get_attribute("value")

    def get_title(self):
        title = self.driver.title
        logger.info( "page title is " + title)
        return title