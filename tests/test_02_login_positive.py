from pages.login import LoginPage
from pages.product import ProductPage
import allure

@allure.title("Login Test")
@allure.description("Test untuk login")
@allure.severity(allure.severity_level.CRITICAL)

def test_login(setup):    
    login = LoginPage(setup)
    product = ProductPage(setup)

    login.input_username('standard_user')
    login.input_password('secret_sauce')
    login.click_button()
    product.check_product_page()