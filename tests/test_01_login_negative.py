import allure
import pytest
from pages.login import LoginPage
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.feature("Login")
@allure.story("Negative Test")
@allure.severity(allure.severity_level.CRITICAL)
class TestLoginNegative:

    @pytest.mark.parametrize(
        "username,password,expected_error",
        [
            ("user_salah", "secret_sauce", "Username and password do not match any user in this service."),
            ("standard_user", "password_salah", "Username and password do not match any user in this service."),
            ("", "secret_sauce", "Username is required"),
            ("standard_user", "", "Password is required"),
            ("", "", "Username is required"),
        ],
    )
    @allure.title("Login negatif - Validasi error message")
    @allure.description("Verifikasi berbagai skenario login gagal dengan kombinasi username/password yang salah atau kosong")
    def test_login_negative(self, setup, username, password, expected_error):
        """
        Test login gagal dengan berbagai variasi input username/password
        """
        login = LoginPage(setup)

        with allure.step(f"Input username: '{username}' dan password: '{password}'"):
            login.input_username(username)
            login.input_password(password)

        with allure.step("Klik tombol login"):
            login.click_button()

        with allure.step("Verifikasi pesan error muncul"):
            wait = WebDriverWait(setup, 5)
            error_element = wait.until(
                EC.presence_of_element_located(
                    (AppiumBy.XPATH, f'//android.widget.TextView[@text="{expected_error}"]')
                )
            )
            assert error_element.is_displayed(), f"Pesan error '{expected_error}' tidak muncul!"
