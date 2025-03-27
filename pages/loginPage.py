from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage():
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def fill_login_field(self, login):
        loginFieldElement = self.driver.find_element(By.ID, "ap_email")
        loginFieldElement.send_keys(login)

    def click_to_continue_button(self):
        continueButtonElement = self.driver.find_element(By.ID, "continue")
        continueButtonElement.click()
    def fill_password_field(self, password):
        passwordFieldElement = self.driver.find_element(By.ID, "ap_password")
        passwordFieldElement.send_keys(password)
    def click_to_sign_in_button(self):
        signInButtonElement = self.driver.find_element(By.ID, "signInSubmit")
        signInButtonElement.click()
