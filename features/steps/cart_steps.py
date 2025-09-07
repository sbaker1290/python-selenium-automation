from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_main(context):
    context.driver.get('https://www.target.com/')
    sleep(5)

@when('Click on cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR,'a[data-test="@web/CartLink"]').click()
    sleep(5)

@then('Verify empty message is shown')
def verify_empty_message(context):
    actual_text = context.driver.find_element(By.CSS_SELECTOR,"h1[class*='styles_ndsHeading']").text
    expected_text = 'Your cart is empty'
    assert expected_text in actual_text
