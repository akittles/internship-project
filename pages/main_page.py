from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class MainPage(Page):
    def open(self):
        self.open_url('https://soft.reelly.io/sign-in')
        sleep(2)
