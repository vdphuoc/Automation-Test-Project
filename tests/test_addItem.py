from pages.addItem import AddItemPage

def test_add_item_to_cart(login):
    page = login
    add_item_page = AddItemPage(page)

    # Add item to cart
    add_item_page.add_item_to_cart()
    add_item_page.go_to_cart()

    # Verify item is in cart
    assert page.inner_text(".inventory_item_name") == "Sauce Labs Backpack", "Item not added to cart."
