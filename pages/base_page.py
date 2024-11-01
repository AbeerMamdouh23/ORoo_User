from utils.Logger import  Logger
log = Logger()
logger = log.get_logger()
class BasePage:
    def init(self, driver):
        self.driver = driver

    def find_element(self, locator):
         return self.driver.find_element(*locator)

    def click(self, locator):
        logger.info( f"{locator} clicked")
        self.find_element(locator).click()

    def send_keys(self, text, *locator):
        logger.info(text + f" sent to {locator} "  )
        self.find_element(*locator).send_keys(text)

    def get_title(self):
        title = self.driver.title
        logger.info( "page title is " + title)
        return title