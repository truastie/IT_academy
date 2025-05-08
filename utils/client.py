import allure
import requests
from tests_api.validate_response import validate_response
from allure_helper import AllureHelper

from models.pet_models import LoginModel, LoginResponseModel, RegisterModel, RegisterResponseModel, CreatePetModel, \
    CreatePetResponseModel, PostPetImageModel, PostPetImageResponseModel, PatchPetUpdateModel


class ClientApi:
    def __init__(self, token=None):
        self.base_url = 'http://34.141.58.52:8000/'
        self.session = self._initialize_session()
        self.token = token

    @staticmethod
    def _initialize_session():
        return requests.Session()

    def request(self,
                method: str,
                url: str,
                json=None):
        headers = {}
        if self.token:
            headers['Authorization'] = f"Bearer {self.token}"
        response = self.session.request(
            method=method,
            url=self.base_url+url,
            json=json,
            headers= headers
        )
        return response


class Client(ClientApi):
    def __init__(self, token=None):
        super().__init__(token=token)

    @allure.step('POST /login')
    def login(self,
              request: LoginModel,
              expected_model=LoginResponseModel,
              status_code: int = 200):
        response = self.request(
            method='post',
            url='login',
            json=request.model_dump()
        )
        validated_response= validate_response(response=response, model=expected_model, status_code=status_code)
        token = response.json().get('token')
        self.token = token
        AllureHelper().enrich_allure(response=response)
        return validated_response

    @allure.step('POST /register')
    def registration(self,
                     request: RegisterModel,
                     expected_model: RegisterResponseModel,
                     status_code: int = 201):
        response = self.request(
            method='post',
            url='register',
            json=request.model_dump()
        )
        AllureHelper().enrich_allure(response=response)
        return validate_response(response=response, model=expected_model, status_code=status_code)

    @allure.step('DELETE /pet {pet_id}')
    def delete_pet(self,
                   pet_id:int,
                   expected_model:type,
                   status_code: int = 200):
        response = self.request(
            method='delete',
            url=f'pet/{pet_id}',
            json= None
        )
        AllureHelper().enrich_allure(response=response)
        return validate_response(response=response, model=expected_model, status_code=status_code)

#create_pet=post_pet
    @allure.step('CREATE /pet')
    def create_pet(self,
                   request:CreatePetModel,
                   expected_model,
                   status_code: int = 200):
        response = self.request(
            method='post',
            url=self.base_url+ f'pet',
            json=request.model_dump()
        )
        AllureHelper().enrich_allure(response=response)
        return validate_response(response=response, model=expected_model, status_code=status_code)

    @allure.step('POST /pet Image')
    def post_pet_image(self,
                        pet_id: int,
                        request:PostPetImageModel,
                        expected_model:PostPetImageResponseModel,
                        status_code: int = 200):
        response = self.request(
            method='post',
            url=self.base_url + f'pet/{pet_id}/image',
            json = request.model_dump()
        )
        AllureHelper().enrich_allure(response=response)
        return validate_response(response=response, model=expected_model, status_code=status_code)

    @allure.step('PATCH /pet Update')
    def patch_pet(self,
                  request: PatchPetUpdateModel,
                  expected_model,
                  status_code: int = 200):
        response = self.request(
            method='patch',
            url=f"{self.base_url}+/pet",
            json=request.model_dump()
        )
        AllureHelper().enrich_allure(response=response)
        return validate_response(response=response, model=expected_model, status_code=status_code)