class OrderPage:
    def __init__(self, page):
        self.page = page
        self.cart_button_selector = ".shopping_cart_link"
        self.checkout_button_selector = "#checkout"
        self.first_name_selector = "#first-name"
        self.last_name_selector = "#last-name"
        self.postal_code_selector = "#postal-code"
        self.continue_button_selector = "#continue"
        self.finish_button_selector = "#finish"
        self.error_message_selector = "[data-test='error']"
        self.success_message_selector = ".complete-header"

    def go_to_cart(self):
        self.page.click(self.cart_button_selector)

    def checkout(self, first_name, last_name, postal_code):
        self.page.click(self.checkout_button_selector)
        self.page.fill(self.first_name_selector, first_name)
        self.page.fill(self.last_name_selector, last_name)
        self.page.fill(self.postal_code_selector, postal_code)
        self.page.click(self.continue_button_selector)

    def finish_order(self):
        self.page.click(self.finish_button_selector)

    def get_error_message(self):
        return self.page.inner_text(self.error_message_selector)

    def get_success_message(self):
        return self.page.inner_text(self.success_message_selector)
