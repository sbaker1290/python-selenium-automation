from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep



@then('Verify sign in page is opened')
def verify_sign_in(context):
    actual_result = context.driver.find_element(By.CSS_SELECTOR,"h1[class*='styles_ndsHeading']")
    expected_result = 'Sign in or create account'
    assert expected_result in actual_result.text
