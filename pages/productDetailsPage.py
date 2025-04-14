from selenium import webdriver
from selenium.webdriver.common.by import By


class ProductDetailsPage():
    def __init__(self, driver:webdriver.Chrome):
        self.driver = driver

    def click_to_add_to_cart_button(self):
        cartButtonElement = self.driver.find_element(By.ID, "add-to-cart-button")
        cartButtonElement.click()

    def get_product_name(self):
        productNameElement = self.driver.find_element(By.XPATH, '//h2[@aria-label="K1 S Sling Helmet Large Matte Black/Red"]')
        product_name = productNameElement.text
        print(product_name)

    def get_product_price(self):
        productPriceElement = self.driver.find_element(By.XPATH, '//span[@class="a-price"]')
        product_price = productPriceElement.text
        print(product_price)