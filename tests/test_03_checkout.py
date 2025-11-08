import allure
from pages.login import LoginPage
from pages.product import ProductPage
from pages.cart import CartPage
from pages.login import LoginPage
from pages.checkout_information import CheckoutInfoPage
from pages.checkout_overview import CheckoutOverviewPage

@allure.title("Test Checkout and validasi price product")
@allure.description("Test end-to-end login lalu checkout 2 produk")
def test_checkout(setup):    
    login = LoginPage(setup)
    product = ProductPage(setup)
    cart = CartPage(setup)
    co_info = CheckoutInfoPage(setup)
    co_overview = CheckoutOverviewPage(setup)

    with allure.step("Login ke aplikasi"):
        login.input_username('standard_user')
        login.input_password('secret_sauce')
        login.click_button()

    with allure.step("Validasi price product dan tambah produk ke keranjang"):
        product.check_product_page()        
        price1 = product.choose_product1()
        product.add_to_cart1()
        price2 = product.choose_product2()
        total = product.add_to_cart2(price1, price2)

    with allure.step("Buka keranjang dan checkout"):
        cart.open_cart()
        cart.scroll_and_checkout()

    with allure.step("Masukkan detail informasi customer"):
        co_info.input_first_name('Alfani')
        co_info.input_last_name('Zidni')
        co_info.input_postal_code('123')
        co_info.click_continue() 

    with allure.step("Compare price di page checkout dan keranjang"):
        co_overview.ov_price1(price1)
        co_overview.ov_price2(price2)
        co_overview.compare_and_checkout(total)
