import os
from appium import webdriver
from appium.options.android.uiautomator2.base import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
import pytest

def test_price_validation_should_fail():
    """Test ini sengaja dibuat untuk membuktikan validasi harga bekerja"""
    options = UiAutomator2Options()
    options.udid = '127.0.0.1:5555'
    options.platform_name = 'Android'
    options.app_package = 'com.swaglabsmobileapp'
    options.app_activity = 'MainActivity'
    driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
    driver.implicitly_wait(10)
    
    try:
        # Login
        driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@content-desc="test-Username"]').send_keys('standard_user')
        driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@content-desc="test-Password"]').send_keys('secret_sauce')
        driver.find_element(AppiumBy.XPATH,'//android.view.ViewGroup[@content-desc="test-LOGIN"]').click()

        # Ambil harga produk
        product1 = driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@content-desc="test-Price" and @text="$29.99"]').text
        price1 = product1.replace("$", "")
        print(f"Harga asli produk 1: ${price1}")
        
        # SENGAJA ubah harga untuk test validasi
        price1_fake = "25.99"  # Harga palsu
        print(f"Harga palsu untuk test: ${price1_fake}")
        
        driver.find_element(AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="test-ADD TO CART"])[1]').click()
        driver.find_element(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="test-Cart"]').click()
        
        # Scroll ke checkout
        checkout_btn = driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(false).instance(0))'
            '.scrollIntoView(new UiSelector().text("CHECKOUT").instance(0));'
        )
        checkout_btn.click()
        
        # Isi form
        driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@content-desc="test-First Name"]').send_keys('Test')
        driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@content-desc="test-Last Name"]').send_keys('User')
        driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@content-desc="test-Zip/Postal Code"]').send_keys('12345')
        driver.find_element(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="test-CONTINUE"]').click()
        
        # Ambil harga di checkout
        co_product1 = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="$29.99"]').text
        ov_prod1 = co_product1.replace("$", "")
        print(f"Harga di checkout: ${ov_prod1}")
        
        # Test dengan harga palsu - INI AKAN GAGAL
        print(f"Membandingkan: {ov_prod1} == {price1_fake}")
        assert ov_prod1 == price1_fake, f"VALIDASI BERHASIL! Harga berbeda terdeteksi: checkout=${ov_prod1}, expected=${price1_fake}"
        
    except AssertionError as e:
        print(f"✅ PROOF: {e}")
        raise
    finally:
        driver.quit()

def test_price_validation_should_pass():
    """Test ini membuktikan validasi benar ketika harga sama"""
    options = UiAutomator2Options()
    options.udid = '127.0.0.1:5555'
    options.platform_name = 'Android'
    options.app_package = 'com.swaglabsmobileapp'
    options.app_activity = 'MainActivity'
    driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
    driver.implicitly_wait(10)
    
    try:
        # Login
        driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@content-desc="test-Username"]').send_keys('standard_user')
        driver.find_element(AppiumBy.XPATH,'//android.widget.EditText[@content-desc="test-Password"]').send_keys('secret_sauce')
        driver.find_element(AppiumBy.XPATH,'//android.view.ViewGroup[@content-desc="test-LOGIN"]').click()

        # Ambil harga produk ASLI
        product1 = driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@content-desc="test-Price" and @text="$29.99"]').text
        price1 = product1.replace("$", "")
        print(f"Harga asli produk 1: ${price1}")
        
        driver.find_element(AppiumBy.XPATH, '(//android.view.ViewGroup[@content-desc="test-ADD TO CART"])[1]').click()
        driver.find_element(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="test-Cart"]').click()
        
        # Scroll ke checkout
        checkout_btn = driver.find_element(
            AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(false).instance(0))'
            '.scrollIntoView(new UiSelector().text("CHECKOUT").instance(0));'
        )
        checkout_btn.click()
        
        # Isi form
        driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@content-desc="test-First Name"]').send_keys('Test')
        driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@content-desc="test-Last Name"]').send_keys('User')
        driver.find_element(AppiumBy.XPATH, '//android.widget.EditText[@content-desc="test-Zip/Postal Code"]').send_keys('12345')
        driver.find_element(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="test-CONTINUE"]').click()
        
        # Ambil harga di checkout
        co_product1 = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[@text="$29.99"]').text
        ov_prod1 = co_product1.replace("$", "")
        print(f"Harga di checkout: ${ov_prod1}")
        
        # Test dengan harga ASLI - INI AKAN BERHASIL
        print(f"Membandingkan: {ov_prod1} == {price1}")
        assert ov_prod1 == price1
        print("✅ VALIDASI BERHASIL: Harga sama antara product page dan checkout!")
        
    finally:
        driver.quit()