from appium import webdriver
from appium.options.android.uiautomator2.base import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import time

@pytest.mark.parametrize("first_name,last_name,postal_code", [
    ("Alfani", "Zidn", "460677")
])
def test_checkout(first_name, last_name, postal_code):
    options = UiAutomator2Options()
    options.udid = '127.0.0.1:5555'
    options.platform_name = 'Android'
    options.app_package = 'com.swaglabsmobileapp'
    options.app_activity = 'MainActivity'

    driver = webdriver.Remote('http://127.0.0.1:4723', options=options)
    driver.implicitly_wait(10)

    # ========== LOGIN ==========
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Username").send_keys("standard_user")
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Password").send_keys("secret_sauce")
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-LOGIN").click()

    # ========== VALIDASI PRODUK ==========
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@text="PRODUCTS"]'))
    )
    print("[INFO] Login sukses, halaman PRODUCT tampil ✅")

    # Ambil dua produk
    prices_elements = driver.find_elements(AppiumBy.XPATH, '//android.widget.TextView[@content-desc="test-Price"]')
    add_buttons = driver.find_elements(AppiumBy.XPATH, '//android.view.ViewGroup[@content-desc="test-ADD TO CART"]')

    selected_prices = []
    for i in range(2):
        price_text = prices_elements[i].text.replace("$", "")
        selected_prices.append(float(price_text))
        add_buttons[i].click()
        print(f"[INFO] Produk {i+1} ditambahkan ke keranjang - Harga: ${price_text}")

    calculated_total = round(sum(selected_prices), 2)
    print(f"[INFO] Total harga dari halaman produk: ${calculated_total}")

    # Buka Cart dan Checkout
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Cart").click()
    checkout_btn = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
        'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("CHECKOUT"))')
    checkout_btn.click()

    # Isi form
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-First Name").send_keys(first_name)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Last Name").send_keys(last_name)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-Zip/Postal Code").send_keys(postal_code)
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "test-CONTINUE").click()

    time.sleep(3)

    # Tunggu halaman checkout muncul
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().textContains("Item total")'))
    )

    # Scroll ke bawah kalau belum kelihatan
    try:
        driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().textContains("Item total"))')
    except Exception:
        pass  # lanjut kalau elemen sudah ada

    # Ambil Item total, tax, total
    item_total_text = driver.find_element(AppiumBy.XPATH, '//android.widget.TextView[contains(@text,"Item total")]').text
    item_total_value = float(item_total_text.replace("Item total: $", ""))
    print(f"[INFO] Item total tampil di halaman: ${item_total_value}")

    # Validasi
    assert item_total_value == calculated_total, f"Expected {calculated_total}, got {item_total_value}"

    print("[✅] Validasi total berhasil")
    driver.quit()
