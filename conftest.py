import os
import sys
import pytest
from playwright.sync_api import sync_playwright

from pages.login import LoginPage

sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

@pytest.fixture(scope="function")
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context()
        context.set_default_timeout(60000)
        page = context.new_page()
        yield page
        context.close()
        browser.close()

@pytest.fixture(scope="module")
def read_data():
    def _read_data(file_path):
        import json
        with open('data/'+file_path) as f:
            return json.load(f)

    return _read_data

@pytest.fixture(scope="function")
def login(browser_context, read_data):
    user_data = read_data('user.json')
    page = browser_context
    login_page = LoginPage(page)
    login_page.load()
    login_page.login(user_data['valid']['username'], user_data['valid']['password'])
    yield page