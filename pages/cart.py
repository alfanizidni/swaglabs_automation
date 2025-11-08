from appium.webdriver.common.appiumby import AppiumBy
from locators.cart import Loc
import allure

class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def open_cart(self):
        with allure.step("Buka keranjang"): 
            self.driver.find_element(AppiumBy.XPATH,Loc.OPEN_CART).click()

    def scroll_and_checkout(self):
        with allure.step("Scroll keranjang dan klik button checkout"): 
            checkout_btn = self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,Loc.SCROLL_CART                
            )
            checkout_btn.click()

    

            

    

    