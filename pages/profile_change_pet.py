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
        self.EDIT_BUTTON.click()
        self.page.wait_for_timeout(2000)

    def clear_pet_name(self):
        self.PET_NAME_FIELD.clear()
        self.page.wait_for_timeout(1000)

    def fill_pet_name_field(self, name):
        self.PET_NAME_FIELD.fill(name)
        self.page.wait_for_timeout(1000)

    def click_save_button(self):
        self.SAVE_BUTTON.click()
        self.page.wait_for_timeout(1000)