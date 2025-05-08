import requests
import json

from utils.config import LoginPageConfig


class PetsApi:
    def __init__(self):
        self.base_url='http://34.141.58.52:8000/'

    def login(self, request)-> json :
        response = requests.post(self.base_url + 'login', data=json.dumps(request))
        # data ={
        #     'email': email,
        #     'password': password
        # }
        # token = res.json()['token']
        # id = res.json()['id']
        # status_code = res.status_code
        # return token, id, status_code
        return response.json(), response.status_code


    def post_pet(self,pet_id:int, name:str, pet_type:str, age:int, gender:str)-> json:
        login_data = PetsApi().login(LoginPageConfig.LOGIN_FIELD, LoginPageConfig.PASSWORD_FIELD)
        headers = {'Authorization': f'Bearer {login_data[0]["token"]}'}
        data = {
                "pet_id": 0,
                "name": name,
                "type": pet_type,
                "age": age,
                "gender": gender,
                "owner_id": login_data[0]['id']
        }
        response = requests.post(self.base_url + f'pet/{pet_id}', data=json.dumps(data), headers=headers)
        return response.json(), response.status_code

    def get_pet(self, pet_id:int)-> json:
        login_data = PetsApi().login(LoginPageConfig.LOGIN_FIELD, LoginPageConfig.PASSWORD_FIELD)
        headers = {'Authorization': f'Bearer {login_data[0]["token"]}'}
        response = requests.get(self.base_url + f'pet/{pet_id}', headers=headers)
        return response.json(), response.status_code

    def post_pet_image(self, pet_id:int)-> json:
        login_data = PetsApi().login(LoginPageConfig.LOGIN_FIELD, LoginPageConfig.PASSWORD_FIELD)
        headers = {'Authorization': f'Bearer {login_data[0]["token"]}'}
        files = {
            'pic': ('parrot.png', open('../tests_api/parrot.png', 'rb'), 'image/png')
        }
        response = requests.post(self.base_url + f'pet/{pet_id}/image', headers=headers, files=files)
        return response.json(), response.status_code

    def delete_pet_id(self, pet_id:int) -> json:
        login_data = PetsApi().login(LoginPageConfig.LOGIN_FIELD, LoginPageConfig.PASSWORD_FIELD)
        headers = {'Authorization': f'Bearer {login_data[0]["token"]}'}
        response = requests.delete(self.base_url+ f'pet/{pet_id}', headers=headers)
        return response.json(), response.status_code

    def patch_pet_update(self, pet_id:int, name:str, pet_type:str, age:int, gender:str)-> json:
        login_data = PetsApi().login(LoginPageConfig.LOGIN_FIELD, LoginPageConfig.PASSWORD_FIELD)
        headers = {'Authorization': f'Bearer {login_data[0]["token"]}'}
        data = {
                "pet_id": 0,
                "name": name,
                "type": pet_type,
                "age": age,
                "gender": gender,
                "owner_id": login_data[1],
        }
        response = requests.post(self.base_url + 'pet', data=json.dumps(data), headers=headers)
        return response.json(), response.status_code


