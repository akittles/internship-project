from selenium.webdriver.common.by import By

from pages.base_page import Page
from time import sleep


class SigninPage(Page):
    EMAIL = (By.CSS_SELECTOR, "#email-2")
    PASS = (By.CSS_SELECTOR, "[name= 'Password']")
    CONTINUE_BTN = (By.CSS_SELECTOR, "form [href= '#']")
    LOGO = (By.CSS_SELECTOR, "div.html-logo.w-embed")  # Reelly logo
    SIGN_IN_UI1 = (By.CSS_SELECTOR, ".form-container")  #Sign in or create new account
    FORGOT_PASS_LINK = (By.CSS_SELECTOR, "a[href*='request-password-reset']")
    CREATE_ACCOUNT_LINK = (By.CSS_SELECTOR, "div.sing-in-text")

    def sign_in(self):
        username = self.driver.find_element(By.CSS_SELECTOR, "#email-2").send_keys('akittlesak4@gmail.com')
        password = self.driver.find_element(By.CSS_SELECTOR, "[name= 'Password']").send_keys('betUdontfight9')

    def click_continue(self):
        self.click(*self.CONTINUE_BTN)
    #
    # def verify_ui_text(self):
    #     actual_logo = self.driver.find_element(*self.LOGO).text
    #     sign_in_text = self.driver.find_element(*self.SIGN_IN_UI1).text
    #     assert 'Sign in or create new account' in sign_in_text, f'Expected text not in {sign_in_text}'
    #     actual_forgot_pass = self.driver.find_element(*self.FORGOT_PASS_LINK).text  # forgot password
    #     assert 'Forgot password?' in actual_forgot_pass, f'Expected forgot password link not in {actual_forgot_pass}'
    #     actual_create_acct = self.driver.find_element(*self.CREATE_ACCOUNT_LINK).text  # create account
    #     assert 'Create account' in actual_create_acct, f'Expected create account link not in {actual_create_acct}'
    #     actual_email_link = self.driver.find_element(*self.EMAIL_LINK).text  # email
    #
    # def verify_url(self):
    #     url = self.driver.current_url
    #     assert url == 'https://soft.reelly.io/sign-in', f'Expected URL not in {url}'
