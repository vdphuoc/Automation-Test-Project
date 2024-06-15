import pytest
from pages.sorting import SortingPage

def test_sort_items_by_price_low_to_high(login):
    page = login
    sorting_page = SortingPage(page)

    # Sort items by price (low to high)
    sorting_page.sort_items_by_price_low_to_high()

    # Verify items are sorted correctly
    prices = sorting_page.get_sorted_prices()
    assert prices == sorted(prices), "Items are not sorted by price (low to high)."
