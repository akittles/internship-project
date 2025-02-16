from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('User clicks on verification button')
def click_verification_btn(context):
    context.app.settings_page.open_verification()


@then('Verify verification page')
def verify_verification_page(context):
    context.app.verification_page.verify_verification_page()


@then('Verify upload image button')
def verify_upload_image_btn(context):
    context.app.verification_page.verify_upload_image_btn()


@then('Verify next step button')
def verify_next_step_btn(context):
    context.app.verification_page.verify_next_step_btn()