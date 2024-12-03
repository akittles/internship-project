from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open sign-in page')
def open_sign_in_page(context):
    context.driver.get('https://soft.reelly.io/sign-in')


@given('User enters username and password')
def enter_username_password(context):
    context.app.sign_in_page.sign_in()


@then('User clicks continue')
def click_continue_button(context):
    context.app.sign_in_page.click_continue()


# @when('Click on open in browser button')
# def open_in_browser_button(context):
#     context.driver.find_element(By.CSS_SELECTOR, "a[href*='sign-in']").click()


# @then('Verify signin page UI')
# def verify_signin_page(context):
#     context.app.sign_in_page.verify_ui_text()
#     expected_texted = 'Sign in or create new account'
#     actual_text = context.driver.find_element(By.CSS_SELECTOR, ".form-container").text
#     assert expected_texted in actual_text, f'Expected {expected_texted} not in {actual_text}'


# @then('Verify user on signin page')
# def verify_url(context):
#     url = context.driver.current_url
#     assert url == 'https://soft.reelly.io/sign-in'

