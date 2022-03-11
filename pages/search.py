"""
This module contains DuckDuckGoSearchPage,
the page object for the DuckDuckGo search page.
"""
from playwright.sync_api import Page

class DuckDuckGoSearchPage:

    SEARCH_BUTTON_SELECTOR = '#search_button_homepage'
    SEARCH_INPUT_SELECTOR = '#search_form_input_homepage'

    URL = 'https://www.duckduckgo.com'

    def __init__(self, page: Page):
        self.page = page
        self.search_button = page.locator(self.SEARCH_BUTTON_SELECTOR)
        self.search_input = page.locator(self.SEARCH_INPUT_SELECTOR)
    
    def load(self):
        self.page.goto(self.URL)
    
    def search(self, phrase):
        self.search_input.fill(phrase)
        self.search_button.click()
