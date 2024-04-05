from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import locators


class AmazonHomePage:
    def __init__(self, driver):
        self.driver = driver
        self.account_lists = (By.ID, locators.NAV_LINK_ACCOUNT_LIST)
        self.start_here_link = (By.ID, locators.CREATE_ACCOUNT_SUMBIT)
        self.url = "https://www.amazon.com"
        self.search_bar = (By.ID, locators.SEARCH_BUTTON)
        self.department_dropdown = (By.ID, 'searchDropdownBox')
        self.your_lists_menu = (By.XPATH, '//*[@id="huc-view-your-list-button"]/span/a')
        self.wish_list_link = (By.PARTIAL_LINK_TEXT, "Список желаемого")
        self.product_titles_in_wish_list = (By.CLASS_NAME, 'a-link-normal')
        self.todays_deals_link = (By.LINK_TEXT, "Today's Deals")

    def go_to_registration_page(self):
        account_lists_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.account_lists))
        account_lists_btn.click()
        start_here_btn = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.start_here_link))
        start_here_btn.click()

    def open(self):
        self.driver.get(self.url)

    def enter_search_term(self, term):
        search_input = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.search_bar))
        search_input.clear()
        search_input.send_keys(term + Keys.RETURN)

    def select_department(self, department_name):
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, '/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[1]/div/div/select'))
        )
        select = Select(dropdown)
        select.select_by_visible_text("Electronics")

    def go_to_wish_list(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.your_lists_menu)).click()


    def product_is_in_wish_list(self, product_name):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_any_elements_located(self.product_titles_in_wish_list))
        product_titles = self.driver.find_elements(*self.product_titles_in_wish_list)
        for title in product_titles:
            if product_name in title.text:
                return True
        return False
    def go_to_today_deals(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.todays_deals_link)).click()