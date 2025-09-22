from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SIGNIN_PAGE_VERIFY = (By.CSS_SELECTOR,"h1[class*='styles_ndsHeading']")

@then('Verify sign in page is opened')
def verify_sign_in(context):
    context.app.signin_page.verify_sign_in()
