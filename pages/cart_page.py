from selenium.webdriver.common.by import By

from pages.base_page import Page

class CartPage(Page):
    CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")

    def verify_empty_cart_msg(self):
        actual_text = self.driver.find_element(*self.CART_EMPTY_MSG).text
        expected_text = 'Your cart is empty'
        assert expected_text == actual_text, f'Expected: {expected_text}, but got {actual_text}'
