from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.basePage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super(BasePage,self).__init__(driver)
        self.driver = driver
        self.__loginFieldLocator = self.driver.find_element(By.ID, "ap_email")
        self.__continueButtonLocator = self.driver.find_element(By.ID, "continue")
        self.__passwordFieldLocator = self.driver.find_element(By.ID, "ap_password")
        self.__signInButtonLocator = self.driver.find_element(By.ID, "signInSubmit")

    def fill_login_field(self, login):
        loginFieldElement = self._find_element(self.__loginFieldLocator)
        self._fill_text_field_by_element(loginFieldElement, login)

    def click_to_continue_button(self):
        continueButtonElement = self._find_element(self.__continueButtonLocator)
        self._click_to_web_element(continueButtonElement)
                                               
    def fill_password_field(self, password):
        passwordFieldElement = self._find_element(self.__passwordFieldLocator)
        self._fill_text_field_by_element(passwordFieldElement, password)

    def click_to_sign_in_button(self):
        signInButtonElement = self.driver.find_element(By.ID, "signInSubmit")
        self._click_to_web_element(signInButtonElement)
