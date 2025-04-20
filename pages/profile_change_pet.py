from playwright.sync_api import expect
from pytest_playwright.pytest_playwright import page
from pages.base_page import BasePage


class ChangePet(BasePage):
    def __init__(self, page, timeout=50000):
        super().__init__(page,timeout)
        self.page = page
        self.EDIT_BUTTON=self.page.locator('//div[@class="col-12"][1]//button[@class="p-button p-component"]')
        self.PET_NAME_FIELD=self.page.locator('//input[@id="name"]')
        self.SAVE_BUTTON=self.page.locator('//*[@id="app"]/main/div/form/div/div[2]/div[3]/button')


    def click_edit_button(self):
        self.EDIT_BUTTON.click(timeout=self.timeout)

    def clear_pet_name(self):
        self.PET_NAME_FIELD.clear(timeout=self.timeout)

    def fill_pet_name_field(self, name):
        self.PET_NAME_FIELD.fill(name, timeout=self.timeout)

    def click_save_button(self):
        self.SAVE_BUTTON.click(timeout=self.timeout)

