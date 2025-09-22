from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page


class SideMenu(Page):
    SIGNIN_BTN = (By.XPATH, "//button[@data-test='accountNav-signIn']")
    SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")

    def click_signin(self):
        self.wait_until_clickable_click(*self.SIGNIN_BTN)

    def side_nav_click_add_to_cart(self):
        self.wait_until_clickable_click(*self.SIDE_NAV_ADD_TO_CART_BTN)
