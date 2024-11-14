from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open main page')
def open_reelly(context):
    context.app.main_page.open()
