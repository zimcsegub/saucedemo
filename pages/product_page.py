from selenium.webdriver.common.by import By
from pages.base_page import BasePage


class ProductPage(BasePage):
    PRODUCT_ITEM_LOCATOR = (By.CLASS_NAME, 'inventory_item_name')
    CART_ICON_LOCATOR = (By.CSS_SELECTOR, '#shopping_cart_container a')
    ITEM_COUNT_IN_CART_LOCATOR = (By.CSS_SELECTOR, '#shopping_cart_container  span')
    ITEMS_LOCATOR = (By.XPATH, "//div[@class='inventory_item']")

    def add_product_to_cart(self, product_name):
        add_button_locator = f'//*[text()="{product_name}"]/ancestor::div[@class="inventory_item_description"]//button'
        self.click_element((By.XPATH, add_button_locator))

    def get_product_description(self, product_name):
        product_price_locator = f'//*[text()="{product_name}"]/ancestor::div[@class="inventory_item_description"]'
        return self.get_text((By.XPATH, product_price_locator))

    def get_product_price(self, product_name):
        product_description_locator = f'//*[text()="{product_name}"]/ancestor::div[@class="inventory_item_description"]//div[@class="inventory_item_price"]'
        product_price_in_text = self.get_text((By.XPATH, product_description_locator)).replace('$', '')
        return float(product_price_in_text)

    def goto_cart_page(self):
        self.click_element(self.CART_ICON_LOCATOR)

    def get_total_added_item_to_cart(self):
        return int(self.get_text(self.ITEM_COUNT_IN_CART_LOCATOR))

    def get_items(self):
        return self.get_elements(self.ITEMS_LOCATOR)