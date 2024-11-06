from selenium.webdriver.common.by import By

from pages.base_page import Page


class SigninPage(Page):
    LOGO = (By.CSS_SELECTOR, "div.html-logo.w-embed")  # Reelly logo
    SIGN_IN_UI1 = (By.CSS_SELECTOR, ".form-container")  #Sign in or create new account
    FORGOT_PASS_LINK = (By.CSS_SELECTOR, "a[href*='request-password-reset']")
    CREATE_ACCOUNT_LINK = (By.CSS_SELECTOR, "div.sing-in-text")
    EMAIL_LINK = (By.CSS_SELECTOR, "#email-2")

    # def verify_main_page(self):
    #     pass
    #
    # def verify_sign_in_page(self):
    #     pass
    #
    # def open_browser_button(self):
    #     pass

    def verify_ui_text(self):
        # actual_logo = self.driver.find_element(*self.LOGO).text
        # assert "html-logo w-embed" in actual_logo, f'Expected Logo not in {actual_logo}'
        sign_in_text = self.driver.find_element(*self.SIGN_IN_UI1).text
        assert 'Sign in or create new account' in sign_in_text, f'Expected text not in {sign_in_text}'
        actual_forgot_pass = self.driver.find_element(*self.FORGOT_PASS_LINK).text  # forgot password
        assert 'Forgot password?' in actual_forgot_pass, f'Expected forgot password link not in {actual_forgot_pass}'
        actual_create_acct = self.driver.find_element(*self.CREATE_ACCOUNT_LINK).text  # create account
        assert 'Create account' in actual_create_acct, f'Expected create account link not in {actual_create_acct}'
        actual_email_link = self.driver.find_element(*self.EMAIL_LINK).text  # email
        assert 'email-2' in actual_email_link, f'Expected email link not in {actual_email_link}'

    def verify_url(self):
        url = self.driver.current_url
        assert url == 'https://soft.reelly.io/sign-in', f'Expected URL not in {url}'
