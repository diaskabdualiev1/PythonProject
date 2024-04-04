import time
from telnetlib import EC

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from AmazonHomePage import AmazonHomePage
from AmazonLoginPage import AmazonLoginPage
from AmazonRegistrationPage import AmazonRegistrationPage


@pytest.fixture
def setup():
    driver = webdriver.Chrome()  # or use the webdriver of your choice
    # driver.maximize_window()
    yield driver
    driver.quit()


def test_register_new_user(setup):
    driver = setup
    driver.get("https://www.amazon.com")
    home_page = AmazonHomePage(driver)
    registration_page = AmazonRegistrationPage(driver)
    home_page.go_to_registration_page()
    registration_page.register("Dias", "ddias.31407@gmail.com", "testselenium1234")
    time.sleep(5)
    success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="nav-link-accountList-nav-line-1"]'))
    )
    assert "Hello, Dias" in success_message.text, "Регистрация не была успешной"


def test_sign_in(setup):
    driver = setup
    driver.get("https://www.amazon.com")

    login_page = AmazonLoginPage(driver)
    login_page.navigate_to_sign_in()
    login_page.sign_in("ddias.31407@gmail.com", "Y6n-t4N-iKv-bEy")  # Использование неверного пароля
    time.sleep(5)
    error_message = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'Your password is incorrect')]"))
    )
    assert "Your password is incorrect" in error_message.text, "Expected error message not found"