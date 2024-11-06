# from webbrowser import Chrome
from pages.base_page import Page
from pages.sign_in_page import SigninPage


class Application:
    def __init__(self, driver):

        self.base_page = Page(driver)

        self.sign_in_page = SigninPage(driver)

