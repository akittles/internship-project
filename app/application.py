# from webbrowser import Chrome
from pages.base_page import Page
from pages.sign_in_page import SigninPage
from pages.settings_page import SettingsPage
from pages.main_page import MainPage
from pages.whatsapp_page import WhatsAppPage
from pages.telegram_page import TelegramPage


class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)

        self.main_page = MainPage(driver)
        self.sign_in_page = SigninPage(driver)
        self.settings_page = SettingsPage(driver)
        self.whatsapp_page = WhatsAppPage(driver)
        self.telegram_page = TelegramPage(driver)
