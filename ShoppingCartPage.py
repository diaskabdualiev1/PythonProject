import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShoppingCartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_button = (By.ID, "nav-cart")
        self.product_title_in_cart = (By.CLASS_NAME, 'a-truncate-cut')
        self.quantity_selector = (By.NAME, "quantity")
        self.update_cart_button = (By.NAME, "quantity']")
        self.remove_link = (By.XPATH, "//input[@value='Delete']")

    def open_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.cart_button)).click()

    def product_is_in_cart(self, product_name):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.product_title_in_cart))
        product_titles = self.driver.find_elements(*self.product_title_in_cart)
        for title in product_titles:
            if product_name in title.text:
                return True
        return False

    def change_quantity(self, quantity):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.quantity_selector)).click()

    def remove_item(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.remove_link)).click()

    def is_cart_empty(self):
        # empty_cart_message = WebDriverWait(self.driver, 10).until(
        #     EC.visibility_of_element_located((By.CLASS_NAME, "a-spacing-mini a-spacing-top-base')]")))
        time.sleep(5)
        empty_cart_message = self.driver.find_element(By.XPATH, '//*[@id="sc-active-cart"]/div/div/div/h1')
        print(empty_cart_message.text)
        return "Your Amazon Cart is empty." in empty_cart_message.text
