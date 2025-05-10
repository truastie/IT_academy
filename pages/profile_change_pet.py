from playwright.sync_api import expect
from pytest_playwright.pytest_playwright import page
from pages.base_page import BasePage


class ChangePet(BasePage):
    def __init__(self, page, timeout=5000):
        super().__init__(page,timeout)
        self.page = page
        self.LOGIN_FIELD = self.page.locator('//*[@id="login"]')
        self.PASSWORD_FIELD = self.page.locator('//*[@id="password"]/input')
        self.SUBMIT_BUTTON = self.page.get_by_text('Submit')
        self.EDIT_BUTTON=self.page.locator('//*[@id="app"]/main/div/div/div[2]/div/div[2]/div/div[2]/button[1]')
        self.PET_NAME_FIELD=self.page.locator('//*[@id="name"]')
        self.SAVE_BUTTON=self.page.locator('//*[@id="app"]/main/div/form/div/div[2]/div[3]/button')

    def fill_login_field(self, login):
        self.LOGIN_FIELD.fill(login, timeout=self.timeout)

    def fill_password_field(self, password):
        self.PASSWORD_FIELD.fill(password, timeout=self.timeout)
        self.LOGIN_FIELD.click(timeout=self.timeout)

    def click_submit_button(self):
        self.SUBMIT_BUTTON.click(timeout=self.timeout)

    def check_profile_page(self):
        expect(self.page).to_have_url('http://34.141.58.52:8080/#/profile', timeout=self.timeout)

    def click_edit_button(self):
        self.EDIT_BUTTON.click(timeout=self.timeout)

    def clear_pet_name(self):
        self.PET_NAME_FIELD.clear(timeout=self.timeout)

    def fill_pet_name_field(self, name):
        self.PET_NAME_FIELD.fill(name, timeout=self.timeout)

    def click_save_button(self):
        self.SAVE_BUTTON.click(timeout=self.timeout)

