from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

from pages.main_page import MainPage


@given('Open target main page')
def open_main(context):
    context.app.main_page.open_main()
    sleep(5)


