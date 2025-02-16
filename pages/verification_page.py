from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class VerificationPage(Page):
    UPLOAD_IMAGE_BTN = (By.CSS_SELECTOR, "label[for='input_file']")
    NEXT_STEP_BTN = (By.CSS_SELECTOR, "div[class='next-step--']")

    def verify_verification_page(self):
        self.verify_url('https://soft.reelly.io/verification/step-0')

    def verify_upload_image_btn(self):
        # self.driver.find_element(*self.UPLOAD_IMAGE_BTN)
        assert self.driver.find_element(*self.UPLOAD_IMAGE_BTN).is_displayed()

    def verify_next_step_btn(self):
        assert self.driver.find_element(*self.NEXT_STEP_BTN).is_displayed()