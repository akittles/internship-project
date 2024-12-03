from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open main page')
def open_reelly(context):
    context.driver.get('https://soft.reelly.io/')
    # context.app.main_page.open()


@when('Click on settings')
def click_settings(context):
    context.app.main_page.click_settings_btn()
    # sleep(5)
    # context.driver.settings_page.click_settings()