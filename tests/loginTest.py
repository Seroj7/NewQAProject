import unittest
from selenium import webdriver
from pages.loginPage import LoginPage
from time import sleep


class LoginTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.delete_all_cookies()
        self.driver.implicitly_wait(10)
        self.driver.get("https://www.amazon.com/ap/signin?ie=UTF8&ie=UTF8&openid.pape.max_auth_age=900&openid.return_to=https%3A%2F%2Fwww.amazon.com%3F&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&fromAuthPrompt=1&switch_account=signin&ignoreAuthState=1&disableLoginPrepopulate=1&ref_=ap_sw_aa")
        self.loginPageObj = LoginPage(self.driver)


    def test_positive_login_test(self):
        self.loginPageObj.fill_login_field("manukyanedgars@gmail.com")
        self.loginPageObj.click_to_continue_button()
        self.loginPageObj.fill_password_field("AAB0663634")
        self.loginPageObj.click_to_sign_in_button()

        self.assertEqual()


    def tearDown(self):
        self.driver.close()