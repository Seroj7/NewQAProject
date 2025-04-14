from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def _find_element(self, locator):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
            return element
        except:
            print("Error: element not visible")
            exit(7)

    def _click_to_web_element(self, element):
        element.click()
        print("Click to element")

    def _fill_text_field_by_element(self, element, text):
        element.send_keys(text)