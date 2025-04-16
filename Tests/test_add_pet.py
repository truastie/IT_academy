from generator import random_name
from generator_age import random_age
from pages.prolife_page import ProfilePage


class TestAddPet:
    def test_add_pet(self, page, login):
        page = ProfilePage(page)
        page.click_add_pet_button()
        page.fill_name_field(random_name(6))
        page.fill_age(random_age(1, 10))
        page.click_type_dropdown()
        page.click_type_item('dog')
        page.click_gender_dropdown()
        page.click_type_gender('Female')
        page.click_confirm_new_pet('Submit')
        page.click_going_to_profile()
        page.check_profile_page()