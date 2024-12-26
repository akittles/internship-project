from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from time import sleep


class GenInfoPage(Page):
    TAB_BTN1 = (By.CSS_SELECTOR, "a#w-tabs-0-data-w-tab-0")

    def verify_options_tab(self):
        self.wait_and_click(*self.TAB_BTN1)