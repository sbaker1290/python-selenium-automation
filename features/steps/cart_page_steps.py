from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='cartItem-title']")
TOTAL_TXT = (By.XPATH, "//div[./span[contains(text(), 'subtotal')]]")


@when('Open cart page')
def open_cart_page(context):
    context.driver.get('https://www.target.com/cart')
    sleep(5)


@then('Verify “Your cart is empty” message is shown')
def verify_empty_cart_msg(context):
    context.app.cart_page.verify_empty_cart_msg()


@then('Verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    context.app.cart_page.verify_cart_items(amount)

#cart_summary = context.driver.find_element(*TOTAL_TXT).text
    #assert f'{amount} item' in cart_summary, f"Expected {amount} items but got {cart_summary}"