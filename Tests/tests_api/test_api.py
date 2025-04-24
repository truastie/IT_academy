import pytest

from api import PetsApi
from config import LoginPageConfig

@pytest.mark.positive

class TestApi:

    def test_login(self):
        res = PetsApi().login(LoginPageConfig.LOGIN_FIELD, LoginPageConfig.PASSWORD_FIELD)
        status_code=res[1]
        assert res[0]['email']==LoginPageConfig.LOGIN_FIELD
        assert status_code==200

    def test_post_pet(self, name:str, pet_type:str, age:int, gender:str):
        res = PetsApi().post_pet(name, pet_type, age, gender)
        status_code=res[1]
        assert status_code==200
        assert type(res[0]['id']) is int

    def test_delete_pet(self):
        res = PetsApi().login(LoginPageConfig.LOGIN_FIELD, LoginPageConfig.PASSWORD_FIELD)
        status_code = res[1]
        assert status_code==200

    def test_patch_pet_update(self, pet_id:int, name:str, pet_type:str, age:int, gender:str):
        res = PetsApi().post_pet(pet_id, name, pet_type, age, gender)
        status_code = res[1]
        assert status_code == 200



class TestApiNegative:

    @pytest.mark.parametrize('password', ['', '123'])
    def test_login_incorrect_password(self, password):
        res = PetsApi().login(LoginPageConfig.LOGIN_FIELD, '')
        status_code = res[1]
        assert status_code==400
        assert res[0]['detail']=='Username is taken or pass issue'

    @pytest.mark.parametrize('pet_id', [ '12', '0'])
    def test_delete_non_exist_pet(self, pet_id):
        res = PetsApi().login(LoginPageConfig.LOGIN_FIELD, LoginPageConfig.PASSWORD_FIELD)
        status_code = res[1]
        assert status_code == 400
        assert res[0]['detail'] == "Signature has expired"