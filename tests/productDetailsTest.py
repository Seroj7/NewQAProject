import unittest
from selenium import webdriver
from pages.productDetailsPage import ProductDetailsPage
from pages.navigationBar import NavigationBar

class ProductDetailsTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.get("https://www.amazon.com/ref=nav_logo")
        self.productDetailsPageObj = ProductDetailsPage(self.driver)
        self.navigationBarObj = NavigationBar(self.driver)

    def test_get_product_name(self):
        self.navigationBarObj.fill_search_field("AGV helmet")
        self.navigationBarObj.click_to_search_button()
        self.productDetailsPageObj.get_product_name()

    def test_get_product_price(self):
        self.navigationBarObj.fill_search_field("AGV helmet")
        self.navigationBarObj.click_to_search_button()
        self.productDetailsPageObj.get_product_price()

    def tearDown(self):
        self.driver.close()

