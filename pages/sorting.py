from playwright.sync_api import Page

class SortingPage:
    def __init__(self, page):
        self.page = page
        self.sort_dropdown_selector = ".product_sort_container"
        self.inventory_item_price_selector = ".inventory_item_price"

    def sort_items_by_price_low_to_high(self):
        self.page.select_option(self.sort_dropdown_selector, "lohi")

    def get_sorted_prices(self):
        prices = self.page.query_selector_all(self.inventory_item_price_selector)
        return [float(price.inner_text().replace('$', '')) for price in prices]
