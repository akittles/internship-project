from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Store original window')
def store_original_window(context):
    context.original_window = context.app.base_page.get_current_window()
    sleep(5)


@when('Click on support')
def click_support(context):
    context.app.settings_page.open_support()


@when('Click on news')
def click_news(context):
    context.app.telegram_page.open_news()
    # context.driver.find_elements(By.CSS_SELECTOR, "div [class*='settings-block-menu'] a[href*= 't.me/reellydxb']")


@when('Click on settings')
def click_settings(context):
    context.app.settings_page.click_settings_btn()
    # sleep(5)
    # context.driver.settings_page.click_settings()


@when('Switch to new window')
def switch_window(context):
    context.app.base_page.switch_to_new_window()
    # sleep(2)


@then('Verify Whatsapp page')
def verify_whatsapp_page(context):
    context.app.whatsapp_page.verify_url()


@then('Return to original page')
def return_to_original_window(context):
    context.app.settings_page.switch_to_window_by_id(context.original_window)
    # sleep(5)


@then('Verify Telegram page')
def verify_telegram_page(context):
    context.app.telegram_page.verify_url()
    expected_url = "https://t.me/reellydxb"  # Replace with the actual URL of the Telegram page
    assert context.driver.current_url == expected_url, f"Expected URL '{expected_url}', but got '{context.driver.current_url}'"

# @then('Close current page')
# def close(context):
#     context.app.whatsapp_page.close()
