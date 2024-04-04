from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AmazonHomePage:
    def __init__(self, driver):
        self.driver = driver
        self.account_lists = (By.ID, "nav-link-accountList")
        self.start_here_link = (By.ID, 'createAccountSubmit')

    def go_to_registration_page(self):
        account_lists_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.account_lists))
        account_lists_btn.click()
        start_here_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.start_here_link))
        start_here_btn.click()
