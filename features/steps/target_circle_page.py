from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

BENEFIT_CELLS= (By.CSS_SELECTOR, '[data-test="@web/slingshot-components/CellsComponent/Link"]')


@given('Open target circle page')
def open_main(context):
    context.driver.get('https://www.target.com/circle')
    sleep(5)


@then('Verify there are {projected_amount} benefit cells')
def verify_benefit(context, projected_amount):
    projected_amount = int(projected_amount)
    benefits = context.driver.find_elements(*BENEFIT_CELLS)
    print(f'Benefits {benefits}')
    assert len(benefits) >= projected_amount, f'Expected {projected_amount} benefit cells, but got {len(benefits)}'