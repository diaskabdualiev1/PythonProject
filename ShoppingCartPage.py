from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShoppingCartPage:
    def __init__(self, driver):
        self.driver = driver
        self.cart_button = (By.ID, "nav-cart")
        self.product_title_in_cart = (By.CLASS_NAME,'a-truncate-cut')

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
