from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class MainPage(Page):
    SETTINGS_BTN = (By.CSS_SELECTOR, "[class*= 'menu_grid'] a[href*= 'settings']")

    def open(self):
        self.open_url('https://soft.reelly.io/')

    def click_settings_btn(self):
        self.wait_and_click(*self.SETTINGS_BTN)