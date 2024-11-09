from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class SettingsPage(Page):
    SETTINGS_BTN = (By.CSS_SELECTOR, "[class*= 'menu_grid'] a[href*= 'settings']")
    SUPPORT_BTN = (By.CSS_SELECTOR, "a[href*= 'send?phone']")

    def click_settings_btn(self):
        self.wait_and_click(*self.SETTINGS_BTN)

    def open_support(self):
        self.wait_and_click(*self.SUPPORT_BTN)





