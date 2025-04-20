import allure
import pytest

from config import ProfilePageConfig
from pages.profile_change_pet import ChangePet


@pytest.mark.positive

class TestProfileChange:
    def test_change_pet(self, login):
        profile_page=ChangePet(login)
        with allure.step('Open login page'):
            profile_page.open_page(ProfilePageConfig.PROFILE_PAGE_URL)
        with allure.step('Click edit button'):
            profile_page.click_edit_button()
        with allure.step('Clear pet name field'):
            profile_page.clear_pet_name()
        with allure.step('Fill new pet name "Mikki"'):
            profile_page.fill_pet_name_field('Mikki')
        with allure.step('Click save button'):
            profile_page.click_save_button()
