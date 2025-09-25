from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SIGNIN_PAGE_VERIFY = (By.CSS_SELECTOR,"h1[class*='styles_ndsHeading']")

@given('Open sign in page')
def open_sign_in_page(context):
    context.app.signin_page.open_sign_in_page()


@when('Click on Target terms and conditions link')
def click_target_terms_and_conditions(context):
    context.app.signin_page.click_terms_and_conditions()


@then('Verify sign in page is opened')
def verify_sign_in(context):
    context.app.signin_page.verify_sign_in()

@then('Verify Terms and Conditions page is opened')
def verify_tc_opened(context):
    context.app.terms_and_conditions_page.verify_tc_opened()





