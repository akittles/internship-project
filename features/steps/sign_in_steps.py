from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open main page')
def open_main_page(context):
    context.driver.get('https://reelly.io/')


@given('Open sign-in page')
def open_sign_in_page(context):
    context.driver.get('https://soft.reelly.io/sign-in')


@when('Click on open in browser button')
def open_in_browser_button(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[href*='sign-in']").click()


@then('Verify signin page UI')
def verify_signin_page(context):
    # context.driver.find_element(By.CSS_SELECTOR, "div.html-logo.w-embed").click()
    context.app.sign_in_page.verify_ui_text()
    context.app.sign_in_page.verify_ui_text()
    context.app.sign_in_page.verify_ui_text()
    context.app.sign_in_page.verify_ui_text()
    context.app.sign_in_page.verify_ui_text()

    # expected_texted = 'Sign in or create new account'
    # actual_text = context.driver.find_element(By.CSS_SELECTOR, ".form-container").text
    # assert expected_texted in actual_text, f'Expected {expected_texted} not in {actual_text}'


@then('Verify user on signin page')
def verify_url(context):
    url = context.driver.current_url
    assert url == 'https://soft.reelly.io/sign-in'

