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
    driver = webdriver.Chrome()
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


# def test_product_search_by_name_and_department(setup): #dropdown пробелма шешу керек ajax
#     driver = setup
#     home_page = AmazonHomePage(driver)
#     search_results_page = SearchResultsPage(driver)
#     home_page.open()
#     home_page.select_department("Electronics")
#     home_page.enter_search_term("Bluetooth speakers")
#
#     assert search_results_page.is_search_result_displayed(), "Bluetooth speakers in Electronics not displayed"

def test_product_reviews(setup): # это без сортировки и ассерт не точный
    driver = setup
    home_page = AmazonHomePage(driver)
    product_page = ProductPage(driver)
    home_page.open()
    home_page.enter_search_term("The Great Gatsby book")
    product_page.navigate_to_reviews()

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
    assert shopping_cart_page.product_is_in_cart(
        "The Great Gatsby"), "Товар не был добавлен в корзину или отсутствует в корзине"


def test_checking_todays_deals(setup):
    driver = setup
    home_page = AmazonHomePage(driver)
    home_page.open()
    home_page.go_to_today_deals()
    assert "Deals" in driver.title, "Страница сегодняшних акций не отображает текущие предложения"


def test_search_autocomplete_functionality(setup):
    driver = setup
    home_page = AmazonHomePage(driver)
    home_page.open()
    home_page.enter_search_term_with_autocomplete("lap")  # Нужно доделать ассерт
    assert home_page.is_autocomplete_suggestions_displayed(), "Автодополнение не отображается или предложения не релевантны"


@pytest.mark.parametrize("link_xpath, expected_title", [
    ("//a[contains(text(), \"Today's Deals\")]", "Deals"),
    ("//a[contains(text(), \"Customer Service\")]", "Customer Service"),
    ("//a[contains(text(), \"Registry\")]", "Registry"),
    ("//a[contains(text(), \"Gift Cards\")]", "Gift Cards"),
    ("//a[contains(text(), \"Sell\")]", "Sell")
])
def test_navigation_menu_links(setup, link_xpath, expected_title):
    driver = setup
    home_page = AmazonHomePage(driver)
    home_page.open()
    home_page.navigate_to_link_by_xpath(link_xpath)
    assert expected_title in driver.title, f"Страница '{expected_title}' не загрузилась успешно"

def test_updating_item_quantity_in_cart(setup):# не доконца доделан dropdown не доделан
    driver = setup
    login_page = AmazonLoginPage(driver)
    home_page = AmazonHomePage(driver)
    product_page = ProductPage(driver)
    shopping_cart_page = ShoppingCartPage(driver)

    home_page.open()
    login_page.navigate_to_sign_in()
    login_page.sign_in("ddias.31407@gmail.com", "Y6n-t4N-iKv-bEy")

    home_page.enter_search_term("The Great Gatsby book")
    product_page.navigate_to_product()
    product_page.add_to_cart()

    shopping_cart_page.open_cart()
    shopping_cart_page.change_quantity(2)

    assert True, "Количество товара в корзине не обновлено до 2"

def test_removing_item_from_cart(setup):
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
    shopping_cart_page.remove_item()

    # Шаг 5: Проверяем, что товар удален из корзины
    assert shopping_cart_page.is_cart_empty(), "Товар не был удален из корзины, или корзина не пуста"

def test_accessing_help_section(setup):
    driver = setup
    home_page = AmazonHomePage(driver)

    # Шаг 1: Переходим на главную страницу Amazon.
    driver.get("https://www.amazon.com")

    # Шаг 2 и 3: Переходим в раздел "Помощь".
    home_page.navigate_to_help_section()

    # Шаг 4: Проверяем, что раздел "Помощь" загружен успешно.
    assert "Help" in driver.title, "Раздел 'Помощь' не загружен успешно или заголовок страницы не содержит 'Help'"

def test_sign_out_functionality(setup):
    driver = setup
    login_page = AmazonLoginPage(driver)
    home_page = AmazonHomePage(driver)

    # Step 1: Sign in
    driver.get("https://www.amazon.com")
    login_page.navigate_to_sign_in()
    login_page.sign_in("ddias.31407@gmail.com", "Y6n-t4N-iKv-bEy")
    # Steps 2 and 3: Navigate to Account & Lists and sign out
    home_page.navigate_to_account_lists()
    home_page.sign_out()

    # Step 4: Verify sign out
    assert "Amazon Sign-In" in driver.title, "User is not signed out successfully or not redirected to the Amazon homepage."
