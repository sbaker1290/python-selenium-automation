from selenium.webdriver.common.by import By

from pages.base_page import Page

class SignInPage(Page):
    SIGNIN_PAGE_VERIFY = (By.CSS_SELECTOR, "h1[class*='styles_ndsHeading']")
    TERMS_AND_CONDITIONS =(By.CSS_SELECTOR, "[aria-label*= 'terms & conditions']")


    def verify_sign_in(self):
        self.verify_text('Sign in or create account',*self.SIGNIN_PAGE_VERIFY)


    def open_sign_in_page(self):
        self.open_url('https://www.target.com/orders?lnk=acct_nav_my_account')


    def click_terms_and_conditions(self):
        self.click(*self.TERMS_AND_CONDITIONS)


