from appium.webdriver.common.appiumby import AppiumBy
from locators.checkout_overview import Loc
import allure

class CheckoutOverviewPage:
    def __init__(self, driver):
        self.driver = driver

    def ov_price1(self, price1):
        with allure.step("Compare price 1 checkout dengan keranjang"): 
            co_product1 = self.driver.find_element(AppiumBy.XPATH,Loc.OVERLAPSE_PRICE1).text
            ov_prod1 = co_product1.replace("$", "")
            print(f"Product 1 price at checkout: ${ov_prod1}")
            print(f"Price validation 1: {ov_prod1} == {price1} -> {ov_prod1 == price1}")
            assert ov_prod1 == price1

    def ov_price2(self, price2):
        with allure.step("Compare price 2 checkout dengan keranjang"): 
            co_product2 = self.driver.find_element(AppiumBy.XPATH,Loc.OVERLAPSE_PRICE2).text
            ov_prod2 = co_product2.replace("$", "")
            print(f"Product 2 price at checkout: ${ov_prod2}")
            print(f"Price validation 2: {ov_prod2} == {price2} -> {ov_prod2 == price2}")
            assert ov_prod2 == price2

    def compare_and_checkout(self, total):
        with allure.step("Masukkan kode pos"): 
            finish_btn = self.driver.find_element(
                AppiumBy.ANDROID_UIAUTOMATOR,Loc.SCROLL_FINISH                
            )

            item_total = self.driver.find_element(AppiumBy.XPATH,Loc.VALIDATE_TOTAL).text
            itemTotal = item_total.replace("Item total: $", "")
            print(f"Item total at checkout: ${itemTotal}")
            print(f"Calculated total: ${total}")
            print(f"Total validation: {float(itemTotal)} == {total} -> {float(itemTotal) == total}")
            assert float(itemTotal) == total

            tax = self.driver.find_element(AppiumBy.XPATH,Loc.TAX).text
            pajak = tax.replace("Tax: $", "")
            assert float(pajak) == 3.20

            grand_total = self.driver.find_element(AppiumBy.XPATH,Loc.GRAND_TOTAL).text
            grandTotal = grand_total.replace("Total: $", "")
            assert float(grandTotal) == 43.18
            finish_btn.click()

    
    
    

            

    

    