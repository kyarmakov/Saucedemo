class AuthPage:
    _page = None

    def __init__(self, page):
        AuthPage._page = page
        self._username_input = AuthPage._page.locator("[data-test=\"username\"]")
        self._password_input = AuthPage._page.locator("[data-test=\"password\"]")
        self._login_btn = AuthPage._page.locator("[data-test=\"login-button\"]")

    def navigate(self):
        AuthPage._page.goto("https://www.saucedemo.com/")
        return self

    def login(self, username, password):
        self._username_input.fill(username)
        self._password_input.fill(password)
        self._login_btn.click()
        return ProductsPage(AuthPage._page)
    

class ProductsPage:
    _page = None

    def __init__(self, page):
        ProductsPage._page = page
        self._item = ProductsPage._page.locator("[data-test=\"item-4-title-link\"]")

    def select_item(self):
        self._item.click()
        return ItemPage(ProductsPage._page)


class ItemPage:
    _page = None

    def __init__(self, page):
        ItemPage._page = page
        self._add_to_cart_btn = ItemPage._page.locator("[data-test=\"add-to-cart\"]")
        self._cart_link = ItemPage._page.locator("[data-test=\"shopping-cart-link\"]")

    def add_to_cart(self):
        self._add_to_cart_btn.click()
        self._cart_link.click()
        return CartPage(ItemPage._page)


class CartPage:
    _page = None

    def __init__(self, page):
        CartPage._page = page
        self._checkout_btn = CartPage._page.locator("[data-test=\"checkout\"]")
        self._item = CartPage._page.locator("[data-test=\"inventory-item-name\"]")
        

    def checkout(self):
        self._checkout_btn.click()
        return CheckoutPage(CartPage._page)
    
    def get_item(self):
        return self._item


class CheckoutPage:
    _page = None

    def __init__(self, page):
        CheckoutPage._page = page
        self._first_name = CheckoutPage._page.locator("[data-test=\"firstName\"]")
        self._last_name = CheckoutPage._page.locator("[data-test=\"lastName\"]")
        self._postal_code = CheckoutPage._page.locator("[data-test=\"postalCode\"]")
        self._continue_btn = CheckoutPage._page.locator("[data-test=\"continue\"]")
        

    def enter_first_name(self, first_name):
        self._first_name.fill(first_name)
        return self

    def enter_last_name(self, last_name):
        self._last_name.fill(last_name)
        return self

    def enter_postal_code(self, postal_code):
        self._postal_code.fill(postal_code)
        return self

    def click_continue(self):
        self._continue_btn.click()
        return OverviewPage(CheckoutPage._page)


class OverviewPage:
    _page = None

    def __init__(self, page):
        OverviewPage._page = page
        self._finish_btn = OverviewPage._page.locator("[data-test=\"finish\"]")
        
    def click_finish(self):
        self._finish_btn.click()
        return CompletePage(OverviewPage._page)


class CompletePage:
    _page = None

    def __init__(self, page):
        CompletePage._page = page
        self._complete_header = CompletePage._page.locator("[data-test=\"complete-header\"]")
        self._complete_text = CompletePage._page.locator("[data-test=\"complete-text\"]")

    def get_complete_header(self):
        return self._complete_header
    
    def get_complete_text(self):
        return self._complete_text
    
