import pytest
from selene import browser


@pytest.fixture(autouse=True)
def web_browser():
    browser.open('https://google.com')
    browser.driver.set_window_size(720, 480)
    yield browser
    browser.quit()
