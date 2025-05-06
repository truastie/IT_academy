import pytest

from utils.config import LoginPageConfig
from pages.login_page import LoginPage


@pytest.fixture(scope='session')
def login(playwright):
    browser = playwright.chromium.launch(headless=True)
    context = browser.new_context()
    page = context.new_page()
    login_page = LoginPage(page)
    login_page.open_page(LoginPageConfig.LOGIN_PAGE_URL)
    login_page.fill_login_field(LoginPageConfig.LOGIN_FIELD)
    login_page.fill_password_field(LoginPageConfig.PASSWORD_FIELD)
    login_page.click_submit_button()
    login_page.check_profile_page()
    return page


