from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class TelegramPage(Page):

    def verify_url(self, expected_url="https://t.me/reellydxb"):
        assert expected_url in self.driver.current_url, (
            f"Expected URL to contain '{expected_url}', "
            f"but got '{self.driver.current_url}'")