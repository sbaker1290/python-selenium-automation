from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from support.logger import logger

class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def open_url(self, url):
        logger.info(f'Opening page {url}')
        self.driver.get(url)

    def find_element(self, *locator):
        logger.info(f'Searching for element by {locator}')
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        logger.info(f'Searching for elements by {locator}')
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        logger.info(f'Clicking on element by {locator}')
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        logger.info(f'Inputting text {text} by {locator}')
        self.driver.find_element(*locator).send_keys(text)

    def get_original_window(self):
        return self.driver.current_window_handle

    def switch_to_newly_opened_window(self, old_windows):
        self.wait.until(EC.new_window_is_opened(old_windows))
        current_windows = self.driver.window_handles
        print('Current windows: ', current_windows)
        print('Switching to window', current_windows[1])
        self.driver.switch_to.window(current_windows[1])

    def switch_to_window_by_id(self, window_id):
        logger.info(f'Switching to window {window_id}')
        # print('Switching to window', window_id)
        self.driver.switch_to.window(window_id)

    def hover_element(self, *locator):
        element = self.find_element(*locator)
        actions = ActionChains(self.driver)
        actions.move_to_element(element)
        actions.perform()


    def close(self):
        self.driver.close()

    def wait_until_clickable_click(self, *locator):
        self.wait.until(
            EC.element_to_be_clickable(locator),
            message=f'Element by {locator} is not clickable'
        ).click()

    def wait_until_element_appear(self, *locator):
        element = self.wait.until(
            EC.visibility_of_element_located(locator),
            message=f'Element by {locator} did not appear'
        )
        return element


    def wait_until_element_disappear(self, *locator):
        self.wait.until(
            EC.invisibility_of_element(locator),
            message=f'Element by {locator} did not diappear'
        )

    def wait_until_url_contains(self,partial_url):
        self.wait.until(
            EC.url_contains(partial_url),
            message=f'Current url dose not contain {partial_url}'
        )


    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text == actual_text, \
            f'Expected {expected_text}, but got {actual_text}'

    def verify_partial_text(self, expected_partial_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_partial_text in actual_text, \
            f'Expected {expected_partial_text}, not in {actual_text}'

    def verify_url(self, expected_url):
        actual_url = self.driver.current_url
        assert expected_url == actual_url, \
            f'Expected {expected_url}, but got {actual_url}'

    def verify_partial_url(self, expected_partial_url):
        actual_url = self.driver.current_url
        assert expected_partial_url in actual_url, \
            f'Expected {expected_partial_url}, not in {actual_url}'





