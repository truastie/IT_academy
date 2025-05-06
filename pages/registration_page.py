from pytest_playwright.pytest_playwright import page
from pages.base_page import BasePage


class RegistrationPage(BasePage):
    def __init__(self,page):
        super().__init__(page)
        self.page = page
        self.LOGIN_FIELD=self.page.locator('//*[@id="login"]')
        self.PASSWORD_FIELD=self.page.locator('//*[@id="password"]/input')
        self.CONFIRM_PASSWORD=self.page.locator('//*[@id="confirm_password"]/input')
        self.SUBMIT_BUTTON=self.page.get_by_text('Submit')

    def fill_login_field(self,login):
        self.LOGIN_FIELD.fill(login)

    def fill_password_field(self, password):
        self.PASSWORD_FIELD.fill(password)

    def fill_confirm_password(self, password):
        self.CONFIRM_PASSWORD.fill(password)

    def click_submit_button(self):
        self.SUBMIT_BUTTON.click()

