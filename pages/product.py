from appium.webdriver.common.appiumby import AppiumBy
from locators.product import Loc
import allure

class ProductPage:
    def __init__(self, driver):
        self.driver = driver

    def check_product_page(self):
        with allure.step("Masuk ke halaman product page"): 
            judul = self.driver.find_element(AppiumBy.XPATH,Loc.PRODUCT_TITLE).text
            assert judul == "PRODUCTS"

    def choose_product1(self):
        with allure.step("Validasi price produk 1"): 
            product1 = self.driver.find_element(AppiumBy.XPATH,Loc.CHOOSE_PRODUCT1).text
            price1 = product1.replace("$", "")
            print(f"Product 1 price from product page: ${price1}")  
            return price1    

    def add_to_cart1(self):
        with allure.step("Tambah product 1 Sauce Labs backpack"): 
            self.driver.find_element(AppiumBy.XPATH,Loc.ADD_TO_CART1).click()

    def choose_product2(self):
        with allure.step("Validasi price produk 2"):            
            product2 = self.driver.find_element(AppiumBy.XPATH,Loc.CHOOSE_PRODUCT2).text
            price2 = product2.replace("$", "")
            print(f"Product 2 price from product page: ${price2}")   
            return price2

    def add_to_cart2(self, price1, price2):
        with allure.step("Tambah product 2 Sauce Labs Bike Light"): 
            self.driver.find_element(AppiumBy.XPATH,Loc.ADD_TO_CART2).click()
            total = float(price1) + float(price2)
            print(f"Total dari kedua produk: ${total}")
            assert total == 39.98, f"Expected total 39.98, got {total}"
            return total

            

    

    