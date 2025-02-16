from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify send my cv button')
def verify_send_my_cv_btn(context):
    context.app.view_page_template.verify_send_my_cv_btn()