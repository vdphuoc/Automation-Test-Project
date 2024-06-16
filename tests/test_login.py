import pytest
import json
from pages.login import LoginPage

def test_login_success(browser_context, read_data):
    user_data = read_data('user.json')
    page = browser_context
    login_page = LoginPage(page)
    login_page.load()
    login_page.login(user_data['valid']['username'], user_data['valid']['password'])
    assert "inventory.html" in page.url, "Login failed, not redirected to inventory page."

def test_login_failure(browser_context, read_data):
    user_data = read_data('user.json')
    page = browser_context
    login_page = LoginPage(page)
    login_page.load()
    login_page.login(user_data['invalid']['username'], user_data['invalid']['password'])
    assert "inventory.html" not in page.url, "Login should fail but it succeeded."
    assert "Epic sadface: Username and password do not match any user in this service" in page.inner_text(".error-message-container"), "Error message not displayed"
