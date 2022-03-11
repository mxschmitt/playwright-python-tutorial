"""
This module contains DuckDuckGoResultPage,
the page object for the DuckDuckGo result page.
"""
from playwright.sync_api import Page

class DuckDuckGoResultPage:

    RESULT_LINKS_SELECTOR = '.result__title a.result__a'
    SEARCH_INPUT_SELECTOR = '#search_form_input'
    
    def __init__(self, page: Page):
        self.page = page
        self.result_links = page.locator(self.RESULT_LINKS_SELECTOR)
        self.search_input = page.locator(self.SEARCH_INPUT_SELECTOR)
    
    def result_link_titles(self):
        self.result_links.nth(4).wait_for()
        return self.result_links.all_text_contents()
    
    def result_link_titles_contain_phrase(self, phrase, minimum=1):
        titles = self.result_link_titles()
        matches = [t for t in titles if phrase.lower() in t.lower()]
        return len(matches) >= minimum

    def search_input_value(self):
        return self.search_input.input_value()
    
    def title(self):
        return self.page.title()
