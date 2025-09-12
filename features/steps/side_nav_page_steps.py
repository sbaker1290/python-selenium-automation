from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

SIGNIN_BTN = (By.XPATH, "//button[@data-test='accountNav-signIn']")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")

@when('Click on sign in button')
def click_sign_in(context):
    context.driver.find_element(*SIGNIN_BTN).click()
    sleep(5)


@when('Confirm Add to Cart button from side navigation')
def side_nav_click_add_to_cart(context):
    context.driver.find_element(*SIDE_NAV_ADD_TO_CART_BTN).click()
    sleep(5)