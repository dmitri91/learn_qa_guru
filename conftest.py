import pytest
from selene import browser


@pytest.fixture(autouse=True)
def web_browser():
    browser.open('https://google.com')
    browser.driver.maximize_window()
    yield browser
    browser.quit()
