from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class TelegramPage(Page):
    NEWS_BTN = (By.CSS_SELECTOR, "div [class*='settings-block-menu'] a[href*= 't.me/reellydxb']")

    def open_news(self):
        self.wait_and_click(*self.NEWS_BTN)

    def verify_url(self, expected_url="https://t.me/reellydxb"):
        assert expected_url in self.driver.current_url, (
            f"Expected URL to contain '{expected_url}', "
            f"but got '{self.driver.current_url}'")