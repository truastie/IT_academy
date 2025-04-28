import pytest

from Tests.validate_response import validate_response
from api import PetsApi
from config import LoginPageConfig
from models.pet_models import PetResponseModel, LoginResponseModel, LoginModel, RegisterModel, RegisterResponseModel, \
    DeletePetModel, DeleteResponsePetModel, CreatePetModel, CreatePetResponseModel, \
    PostPetImageModel, PostPetImageResponseModel, PatchPetUpdateModel, PatchPetUpdateResponseModel
from client import Client, ClientApi


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


    def test_registration(self):
        Client().registration(request=RegisterModel(
            email= "str@gmail.com",
            password= "string",
            confirm_password = "string"
        ), expected_model = RegisterResponseModel(
            email="str@gmail.com",
            id=5381
        ))
    #
    # def test_post_pet(self, name:str, pet_type:str, age:int, gender:str):
    #     response = PetsApi().post_pet('Hi', 'dog', 4, 'aa')
    #     status_code=response[1]
    #     expected_model = PetResponseModel()
    #     assert type(response[0]['id']) is int

    def test_create_pet(self):
        client = Client(token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDU5MTUzMDcsImlhdCI6MTc0NTg0MzMwNywic3ViIjo1MjAzfQ.BmUuqhhyfh_xDhOjkdDCwJCGge9b6bTMgWrUoXPHq70")
        create_request=CreatePetModel(
            name = "Testik",
            type= "cat",
            age= 5
        )
        created_pet=client.create_pet(
            request=create_request,
            expected_model=CreatePetResponseModel,
            status_code=200
        )

    def test_delete_pet(self, created_pet=None):
            client = Client(token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDU5MTUzMDcsImlhdCI6MTc0NTg0MzMwNywic3ViIjo1MjAzfQ.BmUuqhhyfh_xDhOjkdDCwJCGge9b6bTMgWrUoXPHq70")
            create_request = CreatePetModel(
                name="Testik",
                type="cat",
                age=5
            )
            created_pet = client.create_pet(
                request=create_request,
                expected_model=CreatePetResponseModel,
                status_code=200
            )

            pet_id_to_delete = created_pet.id
            response_model = client.delete_pet(
                pet_id=pet_id_to_delete,
                expected_model=DeleteResponsePetModel,
                status_code=200
        )

    def test_post_pet_image(self):
        client = Client(token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDU5MTUzMDcsImlhdCI6MTc0NTg0MzMwNywic3ViIjo1MjAzfQ.BmUuqhhyfh_xDhOjkdDCwJCGge9b6bTMgWrUoXPHq70")
        create_request = CreatePetModel(
                name="checkpic",
                type ="cat",
                age=5
        )
        created_pet = client.create_pet(
            request=create_request,
            expected_model=CreatePetResponseModel,
            status_code=200
        )
        file= {
            'pic':('parrot.png', open('C:\\Users\\nasty\\PycharmProjects\\AutoProject\\Tests/tests_api/parrot.png', 'rb'), 'image/png')
        }
        response = client.session.post(
            f"{client.base_url}/pet/{created_pet.id}/image",
            files=file,
            headers={'Authorization': f"Bearer {client.token}"}
        )

    def test_patch_pet_update(self):
        client = Client(token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE3NDU5MTUzMDcsImlhdCI6MTc0NTg0MzMwNywic3ViIjo1MjAzfQ.BmUuqhhyfh_xDhOjkdDCwJCGge9b6bTMgWrUoXPHq70")
        client.patch_pet(request=PatchPetUpdateModel(
            id = 0,
            name= 'helloworld',
            type= 'non',
            age=5
        ), expected_model=PatchPetUpdateResponseModel,
            status_code=200
        )



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
        assert status_code == 505
        assert res[0]['detail'] == 'Internal Server Error'