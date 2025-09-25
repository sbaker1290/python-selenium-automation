from pages.base_page import Page

class TermsAndConditionsPage(Page):

    def verify_tc_opened(self):
        self.wait_until_url_contains('terms-conditions')