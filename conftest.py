import pytest
from selenium.webdriver import Chrome, DesiredCapabilities
from selenium import webdriver

@pytest.fixture(scope='class')
def init_driver(request):
    chrome_opt = webdriver.ChromeOptions()
    prefs = {"credentials_enable_service": False,
             "profile.password_manager_enabled": False}
    chrome_opt.add_experimental_option("prefs", prefs)
    driver = Chrome(options=chrome_opt)
    driver.maximize_window()
    driver.get('https://www.saucedemo.com/')
    request.cls.driver = driver

    yield driver
