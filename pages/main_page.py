from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from time import sleep


class MainPage(Page):
    SETTINGS_BTN = (By.CSS_SELECTOR, "[class*= 'menu_grid'] a[href*= 'settings']")
    FILTER_BTN = (By.CSS_SELECTOR, "a[wized='openFiltersWindow'][class*='w-inline-block']")
    FROM_FIELD = (By.CSS_SELECTOR, "input[wized='unitPriceFromFilter']")
    TO_FIELD = (By.CSS_SELECTOR, "input[wized='unitPriceToFilter']")
    APPLY_FILTERS_BTN = (By.CSS_SELECTOR, "a[wized='applyFilterButton']")
    PRICE_VALUE = (By.XPATH, "//div[contains(@class, 'price-value') and starts-with(., 'AED') and contains(., ',')]")
    NEXT_PAGE_BTN = (By.CSS_SELECTOR, "[wized='nextPageProperties']")

    def open(self):
        self.open_url('https://soft.reelly.io/')

    def click_settings_btn(self):
        self.wait_and_click(*self.SETTINGS_BTN)

    def click_filters_btn(self):
        self.wait_and_click(*self.FILTER_BTN)

    def filter_price_range(self):
        from_field = self.driver.find_element(*self.FROM_FIELD).send_keys('1200000')
        to_field = self.driver.find_element(*self.TO_FIELD).send_keys('2000000')

    def click_apply_filter_btn(self):
        self.wait_and_click(*self.APPLY_FILTERS_BTN)

    def verify_prices_on_page(self):
        self.driver.execute_script("window.scrollBy(0,2000)", "")
        sleep(4)
        self.driver.execute_script("window.scrollBy(0,2000)", "")

        min_price = 1200000
        max_price = 2000000

        for page in range(1, 9):
            all_cards = self.find_elements(*self.PRICE_VALUE)

            print(f"Checking prices on page {page}")  # Log current page number

            for card in all_cards:
                self.wait.until(EC.visibility_of(card.find_element(*self.PRICE_VALUE)))
                price_text = card.find_element(*self.PRICE_VALUE).text.replace('AED', '').replace(',', '')

                price_value = float(price_text)

                assert min_price <= price_value <= max_price, f"Price {price_value} is outside of range"

        self.click_next_page_btn()
        sleep(2)

    def click_next_page_btn(self):
        self.wait_and_click(*self.NEXT_PAGE_BTN)
