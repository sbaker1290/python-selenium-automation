from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from pages.base_page import Page

class HelpPage(Page):
    Header = (By.XPATH, "//h1[text()=' {SUBSTR}']")
    SELECT_TOPIC_DD = (By.CSS_SELECTOR, "select[id*='ViewHelpTopics']")

    def get_locator(self, expected_header_text):
        return [self.Header[0], self.Header[1].replace('{SUBSTR}', expected_header_text)]

    def open_help_returns(self):
        self.driver.get('https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges')

    def select_promotions(self, help_topic):
        dd = self.find_element(*self.SELECT_TOPIC_DD)
        select = Select(dd)
        select.select_by_value(help_topic)

    def verify_header(self, expected_header_text):
        locator = self.get_locator(expected_header_text)
        self.wait_until_element_appear(*locator)

