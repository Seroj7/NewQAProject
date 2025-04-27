from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.basePage import BasePage

class NavigationBar(BasePage):
    def __init__(self, driver: webdriver.Chrome):
        super(BasePage,self).__init__(driver)
        self.driver = driver
        self.__searchFieldLocator = self.driver.find_element(By.ID, "twotabsearchtextbox")
        self.__searchButtonLocator = self.driver.find_element(By.ID, "nav-search-submit-button")
        self.__cartButtonLocator = self.driver.find_element(By.ID, "nav-cart-text-container")
        self.__accountButtonLocator = self.driver.find_element(By.ID, "nav-link-accountList")

    def fill_search_field(self, search):
        searchFieldElement = self._find_element(self.__searchFieldLocator)
        self._click_to_web_element(searchFieldElement)

    def click_to_search_button(self):
        searchButtonElement = self._find_element(self.__searchButtonLocator)
        self._click_to_web_element(searchButtonElement)

    def click_to_cart_button(self):
        cartButtonElement = self._find_element(self.__cartButtonLocator)
        self._click_to_web_element(cartButtonElement)

    def mouse_move_to_account_button(self):
        accountButtonElement = self._find_element(self.__accountButtonLocator)
        self._move_to_element(accountButtonElement)