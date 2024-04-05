import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AmazonLoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.account_lists = (By.ID, "nav-link-accountList")
        self.sign_in_button = (By.ID, "signInSubmit")
        self.email_input = (By.ID, "ap_email")
        self.password_input = (By.ID, "ap_password")
        self.continue_button = (By.ID, "continue")
        self.hello_text_zone = (By.CLASS_NAME, "nav-line-1-container")

    def navigate_to_sign_in(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.account_lists)).click()

    def sign_in(self, email, password):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.email_input)).send_keys(email)
        self.driver.find_element(*self.continue_button).click()
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.password_input)).send_keys(password)
        self.driver.find_element(*self.sign_in_button).click()

    def is_logged_in_successfully(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "nav-line-1-container"))
        )
        account_name_element = self.driver.find_element(By.CLASS_NAME, "nav-line-1-container")
        print(account_name_element.text)
        return "Hello, Sign in" not in account_name_element.text

# def is_logged_in_successfully(self):
#      WebDriverWait(self.driver, 10).until(
#          EC.visibility_of_element_located(self.hello_text_zone)
#      )
#      account_name_element = self.driver.find_element(self.hello_text_zone)
#      print(account_name_element.text)  # Для отладки
#      return "Hello, Sign in" not in account_name_element.text
