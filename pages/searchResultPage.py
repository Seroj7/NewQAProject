from selenium import webdriver
from selenium.webdriver.common.by import By



class SearchResultPage():
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def click_to_first_product(self):
        firstProductButton = self.driver.find_element(By.XPATH, '//h2[@aria-label="K1 S Street Helmet-Matte Black-XL"]')
        firstProductButton.click()

    def click_to_second_product(self):
        secondProductButton = self.driver.find_element(By.XPATH, '//h2[@aria-label="Sponsored Ad - Holt Helmet – Adult All-Season Helmet – Lightweight Protection for Skiing, Skating, Snowboarding & Snowsports – for Men & Women"]')
        secondProductButton.click()
