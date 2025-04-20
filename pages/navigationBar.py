from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


class NavigationBar():
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def fill_search_field(self, search):
        searchFieldElement = self.driver.find_element(By.ID, "twotabsearchtextbox")
        searchFieldElement.send_keys(search)

    def click_to_search_button(self):
        searchButtonElement = self.driver.find_element(By.ID, "nav-search-submit-button")
        searchButtonElement.click()

    def click_to_cart_button(self):
        cartButtonElement = self.driver.find_element(By.ID, "nav-cart-text-container")
        cartButtonElement.click()

    def mouse_move_to_account_button(self):
        accountButtonElement = self.driver.find_element(By.ID, "nav-link-accountList")
        ActionChains(self.driver).move_to_element(accountButtonElement).perform()