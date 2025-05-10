import allure

from models.pet_models import RegisterModel, RegisterResponseModel
from utils.client import Client
from utils.config import RegistrationPageConfig

from pages.registration_page import RegistrationPage


class TestRegistration:
  def test_registration(self, page):
      registr_page=RegistrationPage(page)
      with allure.step('Open registration page'):
            registr_page.open_page(RegistrationPageConfig.REGISTR_PAGE_URL)
      with allure.step(f'Fill email with {RegistrationPageConfig.REGISTR_FIELD}'):
            registr_page.fill_login_field(RegistrationPageConfig.REGISTR_FIELD)
      with allure.step(f'Fill password with {RegistrationPageConfig.PASSWORD_FIELD}'):
            registr_page.fill_password_field(RegistrationPageConfig.PASSWORD_FIELD)
      with allure.step(f'Fill password with {RegistrationPageConfig.PASSWORD_FIELD}'):
            registr_page.fill_confirm_password(RegistrationPageConfig.PASSWORD_FIELD)
      with allure.step('Click Submit button'):
            registr_page.click_submit_button()
      request_model=RegisterModel()
      expected_model = RegisterResponseModel()
      Client().registration(request_model, expected_model=expected_model)


