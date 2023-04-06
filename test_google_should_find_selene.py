from selene.support.shared import browser
from selene import be, have


def test_google():
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('#search').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_incorrect_request():
    request_text = '123454656оарыовkgfgjgjfgjf'
    browser.element('[name="q"]').should(be.blank).type(request_text).press_enter()
    browser.element('#result-stats').should(have.text('Результатов: примерно 0'))
    browser.element('#result-stats').should(have.text('Результатов: примерно 0'))
