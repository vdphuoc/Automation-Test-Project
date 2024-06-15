from playwright.sync_api import Page

class AddItemPage:
    def __init__(self, page):
        self.page = page
        self.add_to_cart_button_selector = "button[name='add-to-cart-sauce-labs-backpack']"
        self.cart_icon_selector = ".shopping_cart_link"

    def add_item_to_cart(self):
        self.page.click(self.add_to_cart_button_selector)

    def go_to_cart(self):
        self.page.click(self.cart_icon_selector)
