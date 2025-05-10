import re
from http.client import responses

import allure
import pytest

from models.pet_models import PatchPetUpdateModel, PatchPetUpdateResponseModel
from pages.login_page import LoginPage
from pages.prolife_page import ProfilePage
from utils.client import Client
from utils.config import ProfilePageConfig, LoginPageConfig
from pages.profile_change_pet import ChangePet


@pytest.mark.positive

class TestProfileChange:
    def test_change_pet(self,  login):
        profile_page= ChangePet(login)
        with allure.step('Open login page'):
            profile_page.open_page(LoginPageConfig.LOGIN_PAGE_URL)
        with allure.step(f'Fill email field with {LoginPageConfig.LOGIN_FIELD}'):
            profile_page.fill_login_field(LoginPageConfig.LOGIN_FIELD)
        with allure.step(f'Fill password field with {LoginPageConfig.PASSWORD_FIELD}'):
            profile_page.fill_password_field(LoginPageConfig.PASSWORD_FIELD)
        with allure.step('Click Submit button'):
            profile_page.click_submit_button()
        with allure.step('Check profile page'):
            profile_page.check_profile_page()
        with allure.step('Click edit button'):
            profile_page.click_edit_button()
        with allure.step('Clear pet name field'):
            profile_page.clear_pet_name()
        with allure.step('Fill new pet name "Mikki"'):
            profile_page.fill_pet_name_field('Mikki')
        with allure.step('Click save button'):
            profile_page.click_save_button()
            pet_url = profile_page.get_url()
            pet_id=int(pet_url.split('/')[-1])
            request_model=PatchPetUpdateModel(
                id=pet_id,
                name="Mikki"
            )
            expected_model = PatchPetUpdateResponseModel
            Client().patch_pet(request_model, expected_model)
