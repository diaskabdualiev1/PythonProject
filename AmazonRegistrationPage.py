import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class AmazonRegistrationPage:
    def __init__(self, driver):
        self.driver = driver
        self.name_input = (By.ID, "ap_customer_name")
        self.email_input = (By.ID, "ap_email")
        self.password_input = (By.ID, "ap_password")
        self.continue_button = (By.ID, "continue")

    def register(self, name, email, password):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.name_input)).send_keys(name)
        self.driver.find_element(*self.email_input).send_keys(email)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.continue_button).click()
        time.sleep(5)


