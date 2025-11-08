from appium.webdriver.common.appiumby import AppiumBy
from locators.login import Loc
import allure


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def input_username(self, username):
        with allure.step("Input username"): 
            self.driver.find_element(AppiumBy.XPATH,Loc.USERNAME_FIELD).send_keys(username)
    def input_password(self, password):
        with allure.step("Input password"):     
            self.driver.find_element(AppiumBy.XPATH,Loc.PASSWORD_FIELD).send_keys(password)
    def click_button(self):    
        with allure.step("Klik button Login"):     
            self.driver.find_element(AppiumBy.XPATH,Loc.LOGIN_BUTTON).click()
