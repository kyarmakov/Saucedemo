from playwright.sync_api import Page
from pom.test_page_objects import *

def test_saucedemo_e2e(page: Page):
    auth_page = AuthPage(page)
    products_page: ProductsPage = auth_page.navigate().login("standard_user", "secret_sauce")

    itemPage: ItemPage = products_page.select_item()
    cartPage: CartPage = itemPage.add_to_cart()
    assert cartPage.get_item().text_content() == "Sauce Labs Backpack"

    checkoutPage: CheckoutPage = cartPage.checkout()
    overviewPage: OverviewPage = checkoutPage.enter_first_name("test first name").enter_last_name("test last name").enter_postal_code("12345").click_continue()

    completePage: CompletePage = overviewPage.click_finish()

    assert completePage.get_complete_header().text_content() == "Thank you for your order!"
    assert completePage.get_complete_text().text_content() == "Your order has been dispatched, and will arrive just as fast as the pony can get there!"