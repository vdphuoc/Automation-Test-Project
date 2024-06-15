from pages.addItem import AddItemPage
from pages.order import OrderPage
## 2 test cases will be FAILED

def test_order_success(login):
    page = login
    add_item_page = AddItemPage(page)
    order_page = OrderPage(page)

    # Add item to cart
    add_item_page.add_item_to_cart()
    order_page.go_to_cart()

    # Perform checkout
    order_page.checkout("John", "Doe", "12345")
    order_page.finish_order()

    # Verify order is successful
    success_message = order_page.get_success_message()
    assert success_message == "THANK YOU FOR YOUR ORDER", "Order was not successful."


def test_order_failure(login):
    page = login
    add_item_page = AddItemPage(page)
    order_page = OrderPage(page)

    # Add item to cart
    add_item_page.add_item_to_cart()
    order_page.go_to_cart()

    # Perform checkout with missing postal code
    order_page.checkout("John", "Doe", "")
    order_page.finish_order()

    # Verify error message is displayed
    error_message = order_page.get_error_message()
    assert "Error: Postal Code is required" in error_message, "Expected error message was not displayed."
