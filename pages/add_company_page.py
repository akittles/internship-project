from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from time import sleep


class AddCompanyPage(Page):
    PUBLISH_MY_COMPANY_BTN = (By.CSS_SELECTOR, "div.buttons-block-market [href='/payment/personal']")
    VIEW_PAGE_TEMPLATE_BTN = (By.CSS_SELECTOR, "[href='https://soft.reelly.io/view-page-template?company=178']")

    def verify_add_company_page(self):
        self.verify_url('https://soft.reelly.io/presentation-for-the-agency')

    def verify_publish_my_company_btn(self):
        self.find_element(*self.PUBLISH_MY_COMPANY_BTN)

    def click_page_template_btn(self):
        self.driver.execute_script("window.scrollBy(0,2000)", "")
        sleep(4)
        self.driver.execute_script("window.scrollBy(0,2000)", "")
        self.find_element(*self.VIEW_PAGE_TEMPLATE_BTN).click()


