from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click on account icon')
def click_account_icon(context):
    context.driver.find_element(By.ID, 'account-sign-in').click()
    sleep(5)

@when('Click on sign in button')
def click_sign_in(context):
    context.driver.find_element(By.XPATH, "//button[@data-test='accountNav-signIn']").click()
    sleep(5)

@then('Verify sign in page is opened')
def verify_sign_in(context):
    actual_result = context.driver.find_element(By.CSS_SELECTOR,"h1[class*='styles_ndsHeading']")
    expected_result = 'Sign in or create account'
    assert expected_result in actual_result.text
