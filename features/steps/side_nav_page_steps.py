from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SIGNIN_BTN = (By.XPATH, "//button[@data-test='accountNav-signIn']")


@when('Click on sign in button')
def click_sign_in(context):
    context.app.side_menu.click_signin()



