from selenium.webdriver.common.by import By

from pages.base_page import Page

class SearchResultsPage(Page):
    SEARCH_RESULTS_TXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")



    def verify_search_results(self, product):
        self.verify_partial_text(product,*self.SEARCH_RESULTS_TXT)

    def verify_product_url(self, product):
        self.verify_partial_text(f'searchTerm={product}')

    def click_on_add_to_cart(self):
        self.wait_until_clickable_click(*self.ADD_TO_CART_BTN)
