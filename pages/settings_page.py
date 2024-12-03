from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class SettingsPage(Page):
    NEWS_BTN = (By.CSS_SELECTOR, "div [class*='settings-block-menu'] a[href*= 't.me/reellydxb']")
    SUPPORT_BTN = (By.CSS_SELECTOR, "a[href*= 'send?phone']")

    def open_support(self):
        self.wait_and_click(*self.SUPPORT_BTN)

    def open_news(self):
        self.wait_and_click(*self.NEWS_BTN)







