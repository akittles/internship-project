# from webbrowser import Chrome
from pages.base_page import Page
from pages.sign_in_page import SigninPage
from pages.settings_page import SettingsPage
from pages.main_page import MainPage
from pages.whatsapp_page import WhatsAppPage
from pages.telegram_page import TelegramPage
from pages.gen_info_page import GenInfoPage
from pages.market_page import MarketPage
from pages.verification_page import VerificationPage
from pages.add_company_page import AddCompanyPage
from pages.view_page_template_page import ViewPageTemplate


class Application:
    def __init__(self, driver):
        self.base_page = Page(driver)

        self.main_page = MainPage(driver)
        self.sign_in_page = SigninPage(driver)
        self.settings_page = SettingsPage(driver)
        self.whatsapp_page = WhatsAppPage(driver)
        self.telegram_page = TelegramPage(driver)
        self.gen_info_page = GenInfoPage(driver)
        self.market_page = MarketPage(driver)
        self.verification_page = VerificationPage(driver)
        self.add_company_page = AddCompanyPage(driver)
        self.view_page_template = ViewPageTemplate(driver)
