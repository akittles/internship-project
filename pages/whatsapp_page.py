from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class WhatsAppPage(Page):
    def verify_url(self, expected_url_fragment="https://api.whatsapp.com/send?phone"):
        assert expected_url_fragment in self.driver.current_url, (
            f"Expected URL to contain '{expected_url_fragment}', "
            f"but got '{self.driver.current_url}'")