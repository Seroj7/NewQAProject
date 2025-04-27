from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.basePage import BasePage


class ProductDetailsPage(BasePage):
    def __init__(self, driver:webdriver.Chrome):
        super(BasePage,self).__init__(driver)
        self.driver = driver
        self.__cartButtonLocator = self.driver.find_element(By.ID, "add-to-cart-button")
        self.__productNameLocator = self.driver.find_element(By.XPATH,'//h2[@aria-label="K1 S Sling Helmet Large Matte Black/Red"]')
        self.__productPriceLocator = self.driver.find_element(By.XPATH, '//span[@class="a-price"]')



    def click_to_add_to_cart_button(self):
        cartButtonElement = self._find_element(self.__cartButtonLocator)
        self._click_to_web_element(cartButtonElement)

    def get_product_name(self):
        productNameElement = self._find_element(self.__productNameLocator)
        product_name = productNameElement.text
        print(product_name)

    def get_product_price(self):
        productPriceElement = self._find_element(self.__productPriceLocator)
        product_price = productPriceElement.text
        print(product_price)