from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.reviews_section = (By.XPATH, '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div['
                                          '2]/div/div/span/div/div/div/div[2]/div/div/div[2]/div[1]/span['
                                          '2]/div/span/a/span')
        self.product_rating = (By.XPATH, "//span[@id='acrCustomerReviewText']")
        self.sort_by_dropdown = (By.ID, "sort-order-dropdown")
        self.sort_by_most_helpful = (By.XPATH, "//a[@id='dropdown1']")  #
        self.add_to_cart_button = (By.ID, "add-to-cart-button")
        self.add_to_wish_list_button = (By.ID, "add-to-wishlist-button-submit")

    def navigate_to_reviews(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.reviews_section)
        ).click()

    def is_reviews_displayed(self):
        # search_input = WebDriverWait(self.driver, 10).until(
        #     EC.visibility_of_element_located(self.driver.title))
        return 'The Great Gatsby' in self.driver.title

    def add_to_cart(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_to_cart_button)).click()

    def navigate_to_product(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.reviews_section)
        ).click()

    def add_to_wish_list(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.add_to_wish_list_button)).click()