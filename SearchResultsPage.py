from telnetlib import EC

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class SearchResultsPage:
    def __init__(self, driver):
        self.driver = driver
        self.books_category_filter = (By.XPATH, '//span[text()="Books"]')
        self.classics_subcategory_filter = (By.XPATH, '//span[text()="Literature & Fiction"]')


    def is_search_result_displayed(self):
        # search_input = WebDriverWait(self.driver, 10).until(
        #     EC.visibility_of_element_located(self.driver.title))
        return 'The Great Gatsby' in self.driver.title

    def apply_category_filter(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.books_category_filter)
        ).click()
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.classics_subcategory_filter)
        ).click()
