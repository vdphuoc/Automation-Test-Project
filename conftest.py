import os
import sys
import pytest
from playwright.sync_api import sync_playwright

from pages.login import LoginPage

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

@pytest.fixture(scope="function")
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()

@pytest.fixture(scope="module")
def user_data():
    import json
    with open('data/user.json') as f:
        return json.load(f)

@pytest.fixture(scope="function")
def login(browser_context, user_data):
    page = browser_context
    login_page = LoginPage(page)
    login_page.load()
    login_page.login(user_data['valid']['username'], user_data['valid']['password'])
    yield page