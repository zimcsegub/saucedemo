from selenium.webdriver import Chrome
import time


class BasePage:
    def __init__(self, driver: Chrome):
        self.driver = driver

    def get_element(self, locator):
        return self.driver.find_element(*locator)

    def get_elements(self, locator):
        return self.driver.find_elements(*locator)

    def enter_text(self, locator, text):
        web_element = self.get_element(locator)
        web_element.clear()
        time.sleep(2)
        web_element.send_keys(text)

    def click_element(self, locator):
        time.sleep(2)
        self.get_element(locator).click()
        time.sleep(2)

    def get_text(self, locator):
        return self.get_element(locator).text.strip()
