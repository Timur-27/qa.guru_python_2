from pytest import fixture
from selene import have
from selene.support.shared import browser





@fixture()
def init_browser():
    browser.open('https://google.com').driver.set_window_size(160, 300)


def test_search_selene(init_browser):

    browser.element('[name="q"]').type('selene user').press_enter()
    browser.element('[id = "search"]').should(have.text(' User-oriented Web'))



def test_search_invalid_selene(init_browser):
    browser.element('[name="q"]').type('selene user').press_enter()
    browser.element('[id = "search"]').should(have.text(' User-oriented Web'))