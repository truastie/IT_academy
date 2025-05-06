import re

import allure
import pytest

from utils.config import LoginPageConfig
from pages.login_page import LoginPage

@pytest.mark.positive

class TestLogin:
    def test_login(self, page, login):
        login_page =LoginPage(page)
        with allure.step('Open login page'):
            login_page.open_page(LoginPageConfig.LOGIN_PAGE_URL)
        with allure.step(f'Fill login field with {login}'):
            login_page.fill_login_field(LoginPageConfig.LOGIN_FIELD)
        with allure.step(f'Fill password field with {LoginPageConfig.PASSWORD_FIELD}'):
            login_page.fill_password_field(LoginPageConfig.PASSWORD_FIELD)
        with allure.step('Click Submit button'):
            login_page.click_submit_button()
        with allure.step('Check profile page'):
            login_page.check_profile_page()


@pytest.mark.negative
@allure.title('Test Login Negative')
@allure.severity(allure.severity_level.CRITICAL)
class TestLoginNegative:

    @pytest.mark.dependency(name='test_login_invalid_email')
    @pytest.mark.parametrize('email', ['a', '', '@gmail.com', '2'])
    @allure.description('Log in with incorrect email and expect an error message')
    def test_login_invalid_email(self, page, email):
        login_page = LoginPage(page)
        with allure.step('Open login page'):
            login_page.open_page(LoginPageConfig.LOGIN_PAGE_URL)
        with allure.step(f'Fill email field with {email}'):
            login_page.fill_login_field(email)
        with allure.step(f'Fill password field with {LoginPageConfig.PASSWORD_FIELD}'):
            login_page.fill_password_field(LoginPageConfig.PASSWORD_FIELD)
        with allure.step('Click Submit button'):
            login_page.click_submit_button()
        with allure.step('Check if error message is visible'):
         login_page.check_invalid_email()


    @pytest.mark.dependency(depends=['test_login_invalid_email'])
    @pytest.mark.parametrize('email, password', [('a', ''), ('', ''), ('@gmail.com', 'a'), ('a@gmail.com', '')])
    def test_login_invalid_data(self, page, email, password):
        login_page = LoginPage(page)
        with allure.step('Open login page'):
            login_page.open_page(LoginPageConfig.LOGIN_PAGE_URL)
        with allure.step(f'Fill email field with {email}'):
            login_page.fill_login_field(email)
        with allure.step(f'Fill password field with {LoginPageConfig.PASSWORD_FIELD}'):
            login_page.fill_login_field(password)
        with allure.step('Click submit button'):
            login_page.click_submit_button()
        if len(re.findall('.*@gmail.com', email)) == 0:
            login_page.check_invalid_email()
        if len(password) == 0:
            login_page.check_empty_password()