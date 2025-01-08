from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('User clicks on market')
def click_market(context):
    context.app.market_page.click_market_btn()


@then('Verify market page')
def verify_market_page(context):
    context.app.market_page.verify_market_page()


@when('User pages forward through market')
def user_pages_forward(context):
    context.app.market_page.pages_forward()


@when('User pages backwards through market')
def user_pages_backward(context):
    context.app.market_page.pages_backward()

