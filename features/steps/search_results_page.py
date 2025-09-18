from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

SEARCH_RESULTS_TXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
PRODUCT_IMG = (By.CSS_SELECTOR, 'img')
PRODUCT_TITLE =(By.CSS_SELECTOR, "[data-test='product-title']")

@when('Click on add to cart button')
def click_on_add_to_cart_button(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()
    context.driver.wait.until(
        EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME),
        message = 'Side navigation product did not appear'
    )
    context.driver.wait.until(
        EC.element_to_be_clickable(SIDE_NAV_ADD_TO_CART_BTN),
        message = 'Side navigation add to cart btn not clickable'
    )


@when('Store product name')
def store_product_name(context):
    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    print('Product name stored :', context.product_name)


@when('Confirm Add to cart button from side navigation')
def side_nav_click_add_to_cart(context):
    context.driver.find_element(*SIDE_NAV_ADD_TO_CART_BTN).click()
    sleep(5)


@then('Verify search results are shown for {product}')
def verify_search_results(context, product):
    context.app.search_results_page.verify_search_results(product)


@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    sleep(0.5)
    context.driver.execute_script("window.scrollBy(0,1000)", "")

    products = context.driver.find_elements(*LISTINGS)

    for product in products:
        title = product.find_element(*PRODUCT_TITLE).text
        assert title, 'Product title not shown'
        print(f'{title}')
        product.find_element(*PRODUCT_IMG)

