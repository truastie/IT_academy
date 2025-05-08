import re

import allure
import pytest

from models.pet_models import PatchPetUpdateModel, PatchPetUpdateResponseModel
from utils.client import Client
from utils.config import ProfilePageConfig
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
            pet_url = profile_page.patch_url()
            request_model=PatchPetUpdateModel(
                id=0,
                name="Mikki"
            )
            expected_model = PatchPetUpdateResponseModel()
            Client().patch_pet(pet_url,request=request_model,expected_model=expected_model)