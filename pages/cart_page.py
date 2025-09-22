from selenium.webdriver.common.by import By

from pages.base_page import Page

class CartPage(Page):
    CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
    TOTAL_TXT = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")

    def verify_empty_cart_msg(self):
        self.verify_text('Your cart is empty', *self.CART_EMPTY_MSG)

    def open_cart_page(self):
        self.open_url('https://www.target.com/cart')

    def verify_cart_items(self,amount):
        self.verify_partial_text(amount,*self.TOTAL_TXT)
