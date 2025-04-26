import pytest

from Tests.validate_response import validate_response
from api import PetsApi
from config import LoginPageConfig
from models.pet_models import PetResponseModel, LoginResponseModel, LoginModel
from client import Client

@pytest.mark.positive

class TestApi:

    def test_login(self):
            Client().login(request=LoginModel(
            email = LoginPageConfig.LOGIN_FIELD,
            password = LoginPageConfig.PASSWORD_FIELD
        ), expected_model = LoginResponseModel(
            email= LoginPageConfig.LOGIN_FIELD,
            id = 5203
        ))
        # validate_response(response, expected_model, 200)
        # assert res[0]['email']==LoginPageConfig.LOGIN_FIELD


    def test_post_pet(self, name:str, pet_type:str, age:int, gender:str):
        response = PetsApi().post_pet(name, pet_type, age, gender)
        status_code=response[1]
        expected_model = PetResponseModel()
        assert type(response[0]['id']) is int

    def test_delete_pet(self):
        response = PetsApi().login(LoginPageConfig.LOGIN_FIELD, LoginPageConfig.PASSWORD_FIELD)
        status_code = response[1]
        assert status_code==200

    def test_patch_pet_update(self, pet_id:int, name:str, pet_type:str, age:int, gender:str):
        response = PetsApi().post_pet(pet_id, name, pet_type, age, gender)
        status_code = response[1]
        assert status_code == 200



class TestApiNegative:
    @pytest.mark.negative

    @pytest.mark.parametrize('password', ['', '123'])
    def test_login_incorrect_password(self, password):
        res = PetsApi().login(LoginPageConfig.LOGIN_FIELD, '')
        status_code = res[1]
        assert status_code==400
        assert res[0]['detail']=='Username is taken or pass issue'

    @pytest.mark.parametrize('pet_id', [12, 0])
    def test_delete_non_exist_pet(self, pet_id):
        res = PetsApi().login(LoginPageConfig.LOGIN_FIELD, LoginPageConfig.PASSWORD_FIELD)
        status_code = res[1]
        assert status_code == 400
        assert res[0]['detail'] == "Signature has expired"