from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from time import sleep


class MarketPage(Page):
    MRKT_BTN = (By.CSS_SELECTOR, "a[href = '/market-companies']")
    NEXT_BTN = (By.CSS_SELECTOR, "[wized = 'nextPageMarket']")
    BACK_BTN = (By.CSS_SELECTOR, "[wized = 'previousPageMarket']")
    DEV_TAB = (By.CSS_SELECTOR, "div[fs-queryparam-name=markettagdeveloper")
    LICENSE_TAGS = (By.CSS_SELECTOR, "div.license-block")

    def click_market_btn(self):
        self.wait_and_click(*self.MRKT_BTN)

    def verify_market_page(self):
        self.verify_url('https://soft.reelly.io/market-companies')

    def pages_forward(self):
        self.driver.execute_script("window.scrollBy(0,2000)", "")
        sleep(4)
        self.driver.execute_script("window.scrollBy(0,2000)", "")

        for page in range(1, 9):
            all_page_nums = self.find_elements(*self.NEXT_BTN)

            print(f"Checking page {page}")  # Log current page number

            for page_num in all_page_nums:
                self.wait_and_click(*self.NEXT_BTN)
                # self.wait.until(EC.visibility_of(card.find_element(*self.PRICE_VALUE)))
        self.wait_and_click(*self.NEXT_BTN)
        sleep(2)

    def pages_backward(self):
        self.driver.execute_script("window.scrollBy(0,2000)", "")
        sleep(4)
        self.driver.execute_script("window.scrollBy(0,2000)", "")

        for page in range(8, 0, -1):
            all_page_nums = self.find_elements(*self.BACK_BTN)

            print(f"Checking page {page}")  # Log current page number

            for page_num in all_page_nums:
                self.wait_and_click(*self.BACK_BTN)
        self.wait_and_click(*self.BACK_BTN)

    def click_developer_tab(self):
        self.wait_and_click(*self.DEV_TAB)

    def verify_license_tags(self):
        self.driver.execute_script("window.scrollBy(0,2000)", "")
        sleep(4)
        self.driver.execute_script("window.scrollBy(0,2000)", "")

        all_tags = self.driver.find_elements(*self.LICENSE_TAGS)

        for tag in all_tags:
            assert tag.text != "", "License tag text is empty"



