from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Store original window')
def store_original_window(context):
    context.original_window = context.app.base_page.get_current_window()


@when('Click on support')
def click_support(context):
    context.app.settings_page.open_support()


@when('Switch to new window')
def switch_window(context):
    context.app.base_page.switch_to_new_window()


@then('Verify Whatsapp page')
def verify_whatsapp_page(context):
    context.app.whatsapp_page.verify_url()
    sleep(2)


@then('Return to original page')
def return_to_original_window(context):
    context.app.settings_page.switch_to_window_by_id(context.original_window)
    # sleep(5)


@when('Click on news')
def click_news(context):
    context.app.settings_page.open_news()


@then('Verify Telegram page')
def verify_telegram_page(context):
    context.app.telegram_page.verify_url()

# @then('Close current page')
# def close(context):
#     context.app.whatsapp_page.close()
