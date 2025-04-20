import allure
import pytest

from generator import random_name
from generator import random_age
from pages.prolife_page import ProfilePage

@pytest.mark.positive
class TestAddPet:
    def test_add_pet(self, login):
        page = ProfilePage(login)
        with allure.step('Click add pet button'):
            page.click_add_pet_button()
        with allure.step(f'Fill name field with {random_name(6)}'):
            page.fill_name_field(random_name(6))
        with allure.step(f'Fill age field with {random_age(1,10)}'):
            page.fill_age(random_age(1, 10))
        with allure.step('Click type dropdown'):
            page.click_type_dropdown()
        with allure.step('Click and choose type item "dog"'):
            page.click_type_item('dog')
        with allure.step('Click gender dropdown'):
            page.click_gender_dropdown()
        with allure.step('Click and choose type gender "Female"'):
            page.click_type_gender('Female')
        with allure.step('Click confirm new pet button'):
            page.click_confirm_new_pet('Submit')
        with allure.step('Click going to profile page'):
            page.click_going_to_profile()
        with allure.step('Check profile page'):
            page.check_profile_page()

@pytest.mark.negative
class TestNegativeAddPet:
    @pytest.mark.dependency(name='test_add_pet_invalid_name')
    @pytest.mark.parametrize('name', [''])
    @allure.description('Saving new pet without name and expect an error message')
    def test_add_pet_invalid_name(self, login, name):
        page = ProfilePage(login)
        with allure.step('Click add pet button'):
            page.click_add_pet_button()
        with allure.step(f'Fill name with {name}'):
            page.fill_name_field(name)
        with allure.step(f'Fill age field with {random_age(1,10)}'):
            page.fill_age(random_age(1, 10))
        with allure.step('Click type dropdown'):
            page.click_type_dropdown()
        with allure.step('Click and choose type item "dog"'):
            page.click_type_item('dog')
        with allure.step('Click gender dropdown'):
            page.click_gender_dropdown()
        with allure.step('Click and choose type gender "Female"'):
            page.click_type_gender('Female')
        with allure.step('Click confirm new pet button'):
            page.click_confirm_new_pet('Submit')
        if len(name)==0:
            page.check_invalid_name()

    @pytest.mark.dependency(depends=['test_add_pet_invalid_name'])
    @pytest.mark.parametrize('type', [''])
    def test_add_pet_invalid_age(self, login, type):
        page = ProfilePage(login)
        with allure.step('Click add pet button'):
            page.click_add_pet_button()
        with allure.step(f'Fill name field with {random_name(6)}'):
            page.fill_name_field(random_name(6))
        with allure.step(f'Fill age field with {random_age(1, 10)}'):
            page.fill_age(random_age(1, 10))
        with allure.step('Click gender dropdown'):
            page.click_gender_dropdown()
        with allure.step('Click and choose type gender "Female"'):
            page.click_type_gender('Female')
        with allure.step('Click confirm new pet button'):
            page.click_confirm_new_pet('Submit')
        if len(type)==0:
            page.check_empty_pet_type()

