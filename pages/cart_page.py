from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class CartPage(BasePage):
    CART_ICON_LOCATOR = (By.CSS_SELECTOR, "#shopping_cart_container a")
    CHECK_CART_PAGE_OPEN_LOCATOR = (By.ID, "continue-shopping")
    ITEM_COUNT_IN_CART_LOCATOR = (By.XPATH, "//div[@id='shopping_cart_container']//span[@class='shopping_cart_badge']")
    CHECKOUT_BTN_LOCATOR = (By.ID, "checkout")
    FIRST_NAME_LOCATOR = (By.ID, "first-name")
    LAST_NAME_LOCATOR = (By.ID, "last-name")
    POSTAL_CODE_FIELD_LOCATOR = (By.ID, "postal-code")
    MISSING_FIRSTNAME_ERROR_MSG_LOCATOR = (By.XPATH, "//h3[@data-test='error']")
    MISSING_LASTNAME_ERROR_MSG_LOCATOR = (By.XPATH, "//h3[@data-test='error']")
    MISSING_POSTALCODE_ERROR_MSG_LOCATOR = (By.XPATH, "//h3[@data-test='error']")
    ALL_ITEMS_ADD_TO_CART_LOCATOR = (By.XPATH, "//div[@class='cart_item_label']")

    def get_product_description(self, product_name):
        product_desc_locator = f'//*[text()="{product_name}"]/ancestor::div[@class="inventory_item_description"]'
        return self.get_text((By.XPATH, product_desc_locator))

    def get_product_price(self, product_name):
        product_description_locator = f'//*[text()="{product_name}"]/ancestor::div[@class="inventory_item_description"]//div[@class="inventory_item_price"]'
        product_price_in_text = self.get_text((By.XPATH, product_description_locator)).replace('$', '')
        return float(product_price_in_text)

    def add_product_to_cart(self, product_name):
        add_button_locator = f'//*[text()="{product_name}"]/ancestor::div[@class="inventory_item_description"]//button'
        self.click_element((By.XPATH, add_button_locator))

    def get_cart_page_product_price(self, product_name):
        cart_page_price_locator = f"//div[@class='inventory_item_name' and text()='{product_name}']/ancestor::div[@class='cart_item_label']//div[@class='inventory_item_price']"
        return float(self.get_text((By.XPATH, cart_page_price_locator)).replace("$", ""))

    def get_cart_page_product_desc(self, product_name):
        cart_page_description_locator = f"//div[@class='inventory_item_name' and text()='{product_name}']/ancestor::div[@class='cart_item_label']//div[@class='inventory_item_desc']"
        self.get_text((By.XPATH, cart_page_description_locator))

    def get_item_count_in_cart(self):
        return int(self.get_text(self.ITEM_COUNT_IN_CART_LOCATOR))

    def goto_cart_page(self):
        self.click_element(self.CART_ICON_LOCATOR)

    def get_check_cart_page_text(self):
        return self.get_text(self.CHECK_CART_PAGE_OPEN_LOCATOR)

    def click_checkout_button(self):
        self.click_element(self.CHECKOUT_BTN_LOCATOR)

    def information_table(self, first_name = "", last_name = "", postal_code = ""):
        self.enter_text(self.FIRST_NAME_LOCATOR, first_name)
        self.enter_text(self.LAST_NAME_LOCATOR, last_name)
        self.enter_text(self.POSTAL_CODE_FIELD_LOCATOR, postal_code)

    def click_continue_button(self):
        self.click_element((By.ID, "continue"))

    def get_checkout_page_heading_text(self):
        return self.get_text((By.XPATH, "//div[@data-test='secondary-header']//span[@data-test='title']"))

    def get_firstname_error_msg(self):
        return self.get_text(self.MISSING_FIRSTNAME_ERROR_MSG_LOCATOR)

    def get_lastname_error_msg(self):
        return self.get_text(self.MISSING_LASTNAME_ERROR_MSG_LOCATOR)

    def get_postalcode_error_msg(self):
        return self.get_text(self.MISSING_POSTALCODE_ERROR_MSG_LOCATOR)

    def get_items_list(self):
        return self.get_elements(self.ALL_ITEMS_ADD_TO_CART_LOCATOR)
