from appium.webdriver.common.appiumby import AppiumBy
from locators.checkout_information import Loc
import allure

class CheckoutInfoPage:
    def __init__(self, driver):
        self.driver = driver

    def input_first_name(self, first_name):
        with allure.step("Masukkan nama pertama"): 
            self.driver.find_element(AppiumBy.XPATH,Loc.FIRST_NAME).send_keys(first_name)

    def input_last_name(self, last_name):
        with allure.step("Masukkan nama terakhir"): 
            self.driver.find_element(AppiumBy.XPATH,Loc.LAST_NAME).send_keys(last_name)

    def input_postal_code(self, postal_code):
        with allure.step("Masukkan kode pos"): 
            self.driver.find_element(AppiumBy.XPATH,Loc.POSTAL_CODE).send_keys(postal_code)

    def click_continue(self):
        with allure.step("Klik continue untuk melanjutkan"): 
            self.driver.find_element(AppiumBy.XPATH,Loc.CONTINUE_BUTTON).click()

            

    

    