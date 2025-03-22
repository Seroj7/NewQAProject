import unittest
from selenium import webdriver
from pages.searchResultPage import SearchResultPage


class SearchResultTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.implicitly_wait(10)
        self.driver.get(
            "https://www.amazon.com/s?k=agv+helmet&crid=2B5DC780LN7D5&sprefix=agv%2Caps%2C524&ref=nb_sb_ss_mvt-t8-ranker_1_3")
        self.searchResultObj = SearchResultPage(self.driver)

    def test_click_to_first_product(self):
        self.searchResultObj.click_to_first_product()

    def test_click_to_second_product(self):
        self.searchResultObj.click_to_second_product()

    def tearDown(self):
        self.driver.close()
