from selenium.webdriver.common.by import By

from pages.base_page import Page

class SignInPage(Page):
    SIGNIN_PAGE_VERIFY = (By.CSS_SELECTOR, "h1[class*='styles_ndsHeading']")

    def verify_sign_in(self):
        self.verify_text('Sign in or create account',*self.SIGNIN_PAGE_VERIFY)


