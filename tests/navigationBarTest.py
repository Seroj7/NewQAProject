import unittest
from selenium import webdriver
from pages.navigationBar import NavigationBar


class NavigationBarTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.get("https://www.amazon.com/ref=nav_logo")
        self.navigationBarObj = NavigationBar(self.driver)

    def test_search(self):
        self.navigationBarObj.fill_search_field("AGV Helmet")
        self.navigationBarObj.click_to_search_button()
        self.navigationBarObj.click_to_cart_button()
        self.navigationBarObj.mouse_move_to_account_button()

    def tearDown(self):
        self.driver.close()

