class BasePage:
    def _init_(self, driver):  # Fix the typo by using double underscores
        self.driver = driver

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def click(self, *locator):
        self.find_element(*locator).click()

    def send_keys(self, text, *locator):
        self.find_element(*locator).send_keys(text)

    def get_title(self):
        return self.driver.title