from playwright.sync_api import expect

from pages.base_page import BasePage


class ProfilePage(BasePage):
    def __init__(self, page, timeout=5000):
        super().__init__(page, timeout)
        self.ADD_PET_BUTTON= self.page.locator('//*[@id="app"]/main/div/div/div[1]/div/div[1]/button')
        self.NAME_FIELD= self.page.locator('//*[@id="name"]')
        self.AGE_FIELD=self.page.locator('//*[@id="age"]/input')
        self.TYPE_DROPDOWN= self.page.get_by_text('Select a Type')
        self.TYPE_GENDER=self.page.get_by_text('Select a Gender')
        self.CONFIRM_NEW_PET = self.page.get_by_text('Submit')
        self.GOING_TO_PROFILE= self.page.locator('//*[@id="app"]/header/div/ul/li[1]/a/span[2]')

    def click_add_pet_button(self):
        self.ADD_PET_BUTTON.click(timeout=self.timeout)

    def fill_name_field(self, name):
        self.NAME_FIELD.fill(name, timeout=self.timeout)

    def fill_age(self, age) :
        self.AGE_FIELD.fill(age, timeout=self.timeout)

    def click_type_item(self, pet_type):
        self.page.get_by_text(pet_type).click()

    def click_type_dropdown(self):
        self.TYPE_DROPDOWN.click()

    def click_type_gender(self,gender_type):
        self.page.get_by_text(gender_type).click()

    def click_gender_dropdown(self):
        self.TYPE_GENDER.click()

    def click_confirm_new_pet(self, confirm_adding):
        self.page.get_by_text(confirm_adding).click()

    def click_going_to_profile(self):
        self.GOING_TO_PROFILE.click()

    def check_profile_page(self):
        expect(self.page).to_have_url('http://34.141.58.52:8080/#/profile')