import os
import sys
import pytest
from playwright.sync_api import sync_playwright

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