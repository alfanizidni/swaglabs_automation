import os
from appium import webdriver
from appium.options.android.uiautomator2.base import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import allure

@allure.title("Checkout Test")
@allure.description("Test untuk checkout product")
@allure.severity(allure.severity_level.CRITICAL)

def test_checkout():

    with allure.step("Buka Aplikasi"):
        options = UiAutomator2Options()

        options.udid = '127.0.0.1:5555'  # Let Appium auto-detect device
        options.platform_name = 'Android'
        options.app_package = 'com.swaglabsmobileapp'
        options.app_activity = 'MainActivity'
        driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
        driver.implicitly_wait(10)


    # Login Page
    with allure.step("Input username"): 
        driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@content-desc="test-Username"]').send_keys('standard_user')
    with allure.step("Input password"):     
        driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@content-desc="test-Password"]').send_keys('secret_sauce')
    with allure.step("Klik button Login"):     
        driver.find_element(AppiumBy.XPATH,'//android.view.ViewGroup[@content-desc="test-LOGIN"]').click()

    # Product Page
    with allure.step("Masuk ke halaman product page"): 
        judul = driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@text="PRODUCTS"]').text
        assert judul == "PRODUCTS"
    
    product1 = driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@content-desc="test-Price" and @text="$29.99"]').text
    price1 = product1.replace("$", "")
    print(f"Product 1 price from product page: ${price1}")
    driver.find_element(AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="test-ADD TO CART"])[1]').click()
    product2 = driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@content-desc="test-Price" and @text="$9.99"]').text
    price2 = product2.replace("$", "")
    print(f"Product 2 price from product page: ${price2}")
    driver.find_element(AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="test-ADD TO CART"])').click()

    total = float(price1) + float(price2)
    assert total == 39.98
    
    # buka cart
    driver.find_element(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="test-Cart"]').click()

    # scroll sampai ketemu CHECKOUT
    checkout_btn = driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiScrollable(new UiSelector().scrollable(false).instance(0))'
        '.scrollIntoView(new UiSelector().text("CHECKOUT").instance(0));'
    )
    checkout_btn.click()

    # isi form checkout
    driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@content-desc="test-First Name"]').send_keys('Alfani')
    driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@content-desc="test-Last Name"]').send_keys('Zidn')
    driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@content-desc="test-Zip/Postal Code"]').send_keys('460677')
    driver.find_element(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="test-CONTINUE"]').click()

    co_product1 = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="$29.99"]').text
    ov_prod1 = co_product1.replace("$", "")
    print(f"Product 1 price at checkout: ${ov_prod1}")
    print(f"Price validation 1: {ov_prod1} == {price1} -> {ov_prod1 == price1}")
    assert ov_prod1 == price1

    co_product2 = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="$9.99"]').text
    ov_prod2 = co_product2.replace("$", "")
    print(f"Product 2 price at checkout: ${ov_prod2}")
    print(f"Price validation 2: {ov_prod2} == {price2} -> {ov_prod2 == price2}")
    assert ov_prod2 == price2

    # scroll sampai ketemu FINISH
    finish_btn = driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiScrollable(new UiSelector().scrollable(false).instance(0))'
        '.scrollIntoView(new UiSelector().text("FINISH").instance(0));'
    )

    item_total = driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@text="Item total: $39.98"]').text
    itemTotal = item_total.replace("Item total: $", "")
    print(f"Item total at checkout: ${itemTotal}")
    print(f"Calculated total: ${total}")
    print(f"Total validation: {float(itemTotal)} == {total} -> {float(itemTotal) == total}")
    assert float(itemTotal) == total

    tax = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Tax: $3.20"]').text
    pajak = tax.replace("Tax: $", "")
    assert float(pajak) == 3.20

    grand_total = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="Total: $43.18"]').text
    grandTotal = grand_total.replace("Total: $", "")
    assert float(grandTotal) == 43.18
    finish_btn.click()

    with allure.step("Close aplikasi"): 
        driver.quit()