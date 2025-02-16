from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('User clicks page template button')
def click_page_template_btn(context):
    context.app.add_company_page.click_page_template_btn()


@then('Verify Add Company page')
def verify_add_company(context):
    context.app.add_company_page.verify_add_company_page()


@then('Verify Publish my Company button')
def verify_publish_my_company_button(context):
    context.app.add_company_page.verify_publish_my_company_btn()

