from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify at least one option tab is available')
def verify_options_tab(context):
    context.app.gen_info_page.verify_options_tab()