from selenium.webdriver.common.by import By
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time

class LoginPage(BasePage):
    USERNAME_LOCATOR = (By.ID, 'user-name')
    PASSWORD_LOCATOR = (By.ID, 'password')
    LOGIN_BTN_LOCATOR = (By.ID, 'login-button')
    PASSWORD_ERROR_LOCATOR = (By.CSS_SELECTOR, 'form [data-test="error"]')
    LOGIN_SUCCESSFULLY_LOCATOR = (By.ID, "react-burger-menu-btn")

    def perform_login(self, username='', password=''):
        # WebDriverWait(self.driver, 10).until(
        #     EC.presence_of_element_located((By.ID, "user-name"))
        # )
        wait = WebDriverWait(self.driver, 10)


        if len(self.driver.find_elements(By.CSS_SELECTOR, '#shopping_cart_container a')) == 1:
            print('You are already logged in.')
        else:
            self.enter_text(self.USERNAME_LOCATOR, username)
            self.enter_text(self.PASSWORD_LOCATOR, password)
            self.click_element(self.LOGIN_BTN_LOCATOR)
            print('Login performed successfully...')

    def get_error_msg(self):
        return self.get_text(self.PASSWORD_ERROR_LOCATOR)

    def check_login_successfully_or_not(self):
        return self.get_text(self.LOGIN_SUCCESSFULLY_LOCATOR)
