from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='cartItem-title']")
TOTAL_TXT = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")


@when('Open cart page')
def open_cart_page(context):
    context.app.cart_page.open_cart_page()


@then('Verify “Your cart is empty” message is shown')
def verify_empty_cart_msg(context):
    context.app.cart_page.verify_empty_cart_msg()


@then('Verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    context.app.cart_page.verify_cart_items(amount)

