import pytest
from testcases.base_test import BaseTest
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from selenium.webdriver.common.by import By

class TestCart(BaseTest):

    @pytest.fixture(autouse=True)
    def setup_testcase(self, request):
        self.cart_page = CartPage(self.driver)
        LoginPage(self.driver).perform_login('standard_user', 'secret_sauce')

    def test_product_add_to_cart(self):
        item1 = "Sauce Labs Backpack"
        item2 = "Sauce Labs Bike Light"
        desc1 = self.cart_page.get_product_description(item1)
        desc2 = self.cart_page.get_product_description(item2)
        price1 = self.cart_page.get_product_price(item1)
        price2 = self.cart_page.get_product_price(item2)
        products_information = {item1: {"price": price1, "description": desc1},
                               item2: {"price": price2, "description": desc2}}
        for i in item1, item2:
            self.cart_page.add_product_to_cart(i)

    def test_products_add_to_cart(self):
        count = self.cart_page.get_item_count_in_cart()
        assert count == 2


    def test_cart_page(self):
        self.cart_page.goto_cart_page()
        check_cart_page_title = self.cart_page.get_check_cart_page_text()
        assert check_cart_page_title == "Continue Shopping"

    @pytest.mark.sanity
    def test_cart_page_product(self):
        product_lists = self.cart_page.get_items_list()
        product_map = {}
        for index, item in enumerate(product_lists):
            if index >= 2:
                break
            item_title = item.find_element(By.CLASS_NAME, "inventory_item_name").text.strip()
            item_desc = item.find_element(By.XPATH, "//div[@class='inventory_item_desc']").text.strip()
            item_price = item.find_element(By.XPATH, "//div[@class='inventory_item_price']").text.replace("$", "").strip()
            product_map[item_title] = float(item_price)
        print(product_map)
    # def test_product_buying_process(self):
    #     self.cart_page.click_checkout_button()
    #     continue_btn_text = self.cart_page.get_checkout_page_heading_text()
    #     assert continue_btn_text == "Checkout: Your Information"

    # def test_invalid_customer(self):
        # self.cart_page.information_table("", "islam", "79999")
        # self.cart_page.click_continue_button()
        # firstname_error_msg = self.cart_page.get_firstname_error_msg()
        # assert firstname_error_msg == "Error: First Name is required"

        # self.cart_page.information_table("Lucifer", "", "436598")
        # self.cart_page.click_continue_button()
        # lastname_error_msg = self.cart_page.get_lastname_error_msg()
        # assert lastname_error_msg == "Error: Last Name is required"

        # self.cart_page.information_table("Asif", "Akbar", "")
        # self.cart_page.click_continue_button()
        # postalcode_error_msg = self.cart_page.get_postalcode_error_msg()
        # assert postalcode_error_msg == "Error: Postal Code is required"

    # def test_customer_information_page(self):
    #     self.cart_page.information_table("Zahid", "Khan", "2010")
    #     self.cart_page.click_continue_button()
