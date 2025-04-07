import unittest
from selenium import webdriver
from pages.searchResultPage import SearchResultPage
from pages.navigationBar import NavigationBar


class SearchResultTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.amazon.com/ref=nav_logo")
        self.searchResultObj = SearchResultPage(self.driver)
        self.navigationBarObj = NavigationBar(self.driver)

    def test_click_to_first_product(self):
        self.navigationBarObj.fill_search_field("AGV Helmet")
        self.navigationBarObj.click_to_search_button()
        self.searchResultObj.click_to_first_product()

    def test_click_to_second_product(self):
        self.navigationBarObj.fill_search_field("AGV Helmet")
        self.navigationBarObj.click_to_search_button()
        self.searchResultObj.click_to_second_product()

    def tearDown(self):
        self.driver.close()
