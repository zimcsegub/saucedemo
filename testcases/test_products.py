import pytest
from pages.product_page import ProductPage
from pages.login_page import LoginPage
from testcases.base_test import BaseTest
from selenium.webdriver.common.by import By
import random


class TestProducts(BaseTest):

    @pytest.fixture(autouse=True)
    def setup_testcase(self):
        self.product_page = ProductPage(self.driver)
        LoginPage(self.driver).perform_login('standard_user', 'secret_sauce')

    # @pytest.fixture(scope='class', autouse=True)
    # def setup_suite(self, init_driver):
    #     print(self.driver.title, '*' * 30)

    # def test_product(self):
    #     self.product_page.add_product_to_cart('Sauce Labs Bike Light')
    #     product_price_in_product_page = self.product_page.get_product_price('Sauce Labs Bike Light')
    #     total_added_products_count = self.product_page.get_total_added_item_to_cart()
    #     assert product_price_in_product_page == 9.99
    #     assert total_added_products_count == 1
    def test_all_product(self):
        products = self.product_page.get_items()
        print(products)
        product_page_item = {}
        for index, item in enumerate(products):
            if index>=3:
                break
            item_title = item.find_element(By.XPATH, "//div[@class='inventory_item_name ']").text.strip()
            item_price = item.find_element(By.XPATH, "//div[@class='inventory_item_price']").text.replace("$","").strip()
            print(item_title + "*****")
            self.product_page.add_product_to_cart(item_title)
            product_page_item[item_title] = float(item_price)
            remove_btn_text = item.find_element(By.XPATH, "//div[@class='pricebar']//button").text.strip()
            print(remove_btn_text)
            assert remove_btn_text == 'Remove'
            print(item_title)