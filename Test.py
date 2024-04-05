import time
from telnetlib import EC

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from AmazonHomePage import AmazonHomePage
from AmazonLoginPage import AmazonLoginPage
from AmazonRegistrationPage import AmazonRegistrationPage
from ProductPage import ProductPage
from SearchResultsPage import SearchResultsPage
from ShoppingCartPage import ShoppingCartPage


@pytest.fixture
def setup():
    driver = webdriver.Chrome()  # or use the webdriver of your choice
    # driver.maximize_window()
    yield driver
    driver.quit()


# def test_register_new_user(setup):
#     driver = setup
#     home_page = AmazonHomePage(driver)
#     home_page.open()
#     registration_page = AmazonRegistrationPage(driver)
#     home_page.go_to_registration_page()
#     registration_page.register("Dias", "ddias.31407@gmail.com", "testselenium1234")
#     time.sleep(5)
#     success_message = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.XPATH, '//*[@id="nav-link-accountList-nav-line-1"]'))
#     )
#     assert "Hello, Dias" in success_message.text, "Регистрация не была успешной"


def test_sign_in(setup):
    driver = setup
    driver.get("https://www.amazon.com")
    time.sleep(10)
    login_page = AmazonLoginPage(driver)
    login_page.navigate_to_sign_in()
    login_page.sign_in("ddias.31407@gmail.com", "Y6n-t4N-iKv-bEy")
    assert login_page.is_logged_in_successfully(), "Login was not successful"


def test_product_search_by_name(setup):
    driver = setup
    home_page = AmazonHomePage(driver)
    search_results_page = SearchResultsPage(driver)
    home_page.open()
    home_page.enter_search_term("The Great Gatsby book")

    assert search_results_page.is_search_result_displayed(), "The Great Gatsby book is not displayed"


def test_product_search_with_category_filtering(setup):
    driver = setup
    home_page = AmazonHomePage(driver)
    search_results_page = SearchResultsPage(driver)
    home_page.open()
    home_page.enter_search_term("The Great Gatsby book")
    search_results_page.apply_category_filter()

    assert search_results_page.is_search_result_displayed(), "Filtered search results for The Great Gatsby in Classics not displayed"


# def test_product_search_by_name_and_department(setup):
#     driver = setup
#     home_page = AmazonHomePage(driver)
#     search_results_page = SearchResultsPage(driver)
#     home_page.open()
#     home_page.select_department("Electronics")
#     home_page.enter_search_term("Bluetooth speakers")
#
#     assert search_results_page.is_search_result_displayed(), "Bluetooth speakers in Electronics not displayed"

def test_product_reviews(setup):
    driver = setup
    home_page = AmazonHomePage(driver)
    product_page = ProductPage(driver)
    home_page.open()
    home_page.enter_search_term("The Great Gatsby book")
    product_page.navigate_to_reviews()

    # Здесь добавьте ваш ассерт, например, проверку что отзывы действительно отсортированы.
    assert product_page.is_reviews_displayed(), "Отзывы не были отсортированы согласно выбранному критерию"


def test_add_product_to_cart_and_check(setup):
    driver = setup
    home_page = AmazonHomePage(driver)
    search_results_page = SearchResultsPage(driver)
    product_details_page = ProductPage(driver)
    shopping_cart_page = ShoppingCartPage(driver)

    home_page.open()
    home_page.enter_search_term("The Great Gatsby book")
    product_details_page.navigate_to_product()
    product_details_page.add_to_cart()

    shopping_cart_page.open_cart()
    assert shopping_cart_page.product_is_in_cart("The Great Gatsby"), "Товар не был добавлен в корзину"

def test_add_product_to_wish_list(setup):
    driver = setup
    login_page = AmazonLoginPage(driver)
    home_page = AmazonHomePage(driver)
    product_page = ProductPage(driver)

    driver.get("https://www.amazon.com")
    login_page.navigate_to_sign_in()
    login_page.sign_in("ddias.31407@gmail.com", "Y6n-t4N-iKv-bEy")

    home_page.enter_search_term("The Great Gatsby book")
    product_page.navigate_to_product()
    product_page.add_to_wish_list()

    home_page.go_to_wish_list()
    assert home_page.product_is_in_wish_list("The Great Gatsby"), "Товар не был добавлен в список желаемого"

def test_add_product_to_cart(setup):
    driver = setup
    login_page = AmazonLoginPage(driver)
    home_page = AmazonHomePage(driver)
    product_page = ProductPage(driver)
    shopping_cart_page = ShoppingCartPage(driver)

    driver.get("https://www.amazon.com")
    login_page.navigate_to_sign_in()
    login_page.sign_in("ddias.31407@gmail.com", "Y6n-t4N-iKv-bEy")

    home_page.enter_search_term("The Great Gatsby book")
    product_page.navigate_to_product()
    product_page.add_to_cart()

    shopping_cart_page.open_cart()
    assert shopping_cart_page.product_is_in_cart("The Great Gatsby"), "Товар не был добавлен в корзину или отсутствует в корзине"

def test_checking_todays_deals(setup):
    driver = setup
    home_page = AmazonHomePage(driver)
    home_page.open()
    home_page.go_to_today_deals()
    assert "Today's Deals" in driver.title, "Страница сегодняшних акций не отображает текущие предложения"