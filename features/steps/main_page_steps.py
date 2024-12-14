from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open main page')
def open_reelly(context):
    context.driver.get('https://soft.reelly.io/')


@when('Click on settings')
def click_settings(context):
    context.app.main_page.click_settings_btn()


@when('User clicks filters')
def click_filters(context):
    context.app.main_page.click_filters_btn()
    context.driver.execute_script("window.scrollBy(0,2000)", "")
    sleep(4)
    context.driver.execute_script("window.scrollBy(0,2000)", "")


@when('User enter 1200000 and 2000000 in price filter')
def filter_price_range(context):
    context.app.main_page.filter_price_range()


@when('Click on apply filter')
def click_apply_filter(context):
    context.app.main_page.click_apply_filter_btn()


@then('Verify prices on each page is in range')
def verify_prices(context):
    context.app.main_page.verify_prices_on_page()


@then('Click on next page')
def click_next_page(context):
    context.app.main_page.click_next_page_btn()

