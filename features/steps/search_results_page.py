from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SEARCH_RESULTS_TXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")



@when('Click on add to cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    sleep(6)



@then('Verify search results are shown for {product}')
def verify_search_results(context, product):
    actual_text = context.driver.find_element(*SEARCH_RESULTS_TXT).text
    assert product in actual_text, f'Error. Expected text {product} but got {actual_text}'

