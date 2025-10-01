from pages.base_page import Page
from pages.cart_page import CartPage
from pages.header import Header
from pages.help_page import HelpPage
from pages.main_page import MainPage
from pages.privacy_policy_page import PrivacyPolicyPage
from pages.search_results_page import SearchResultsPage
from pages.side_menu import SideMenu
from pages.signin_page import SignInPage
from pages.target_app_page import TargetAppPage
from pages.term_and_conditions_page import TermsAndConditionsPage


class Application:

    def __init__(self, driver):
        self.driver = driver

        self.page = Page(driver)
        self.header = Header(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.cart_page = CartPage(driver)
        self.side_menu = SideMenu(driver)
        self.signin_page = SignInPage(driver)
        self.target_app_page = TargetAppPage(driver)
        self.privacy_policy_page = PrivacyPolicyPage(driver)
        self.terms_and_conditions_page = TermsAndConditionsPage(driver)
        self.help_page = HelpPage(driver)