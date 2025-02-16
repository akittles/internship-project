from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from time import sleep


class ViewPageTemplate(Page):
    SEND_MY_CV_BTN = (By.CSS_SELECTOR, "a[href='#HR-manager'][class='button-agency w-button']")

    def verify_send_my_cv_btn(self):
        self.driver.find_element(*self.SEND_MY_CV_BTN)