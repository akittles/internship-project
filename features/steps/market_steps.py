from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('User pages forward through market')
def user_pages_forward(context):
    context.app.market_page.pages_forward()


@when('User pages backwards through market')
def user_pages_backward(context):
    context.app.market_page.pages_backward()


@when('User clicks on developers tab')
def user_clicks_developers(context):
    context.app.market_page.click_developer_tab()


@then('User clicks on market')
def click_market(context):
    context.app.market_page.click_market_btn()


@then('Verify market page')
def verify_market_page(context):
    context.app.market_page.verify_market_page()


@then('Verify cards have license tag')
def verify_license_tag(context):
    context.app.market_page.verify_license_tags()


@then('User clicks Add Company button')
def click_add_company(context):
    context.app.market_page.click_add_company_btn()

