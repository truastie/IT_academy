from utils.config import RegistrationPageConfig

from pages.registration_page import RegistrationPage


class TestRegistration:
  def test_registration(self, page):
        registr_page=RegistrationPage(page)
        registr_page.open_page(RegistrationPageConfig.REGISTR_PAGE_URL)
        registr_page.fill_login_field(RegistrationPageConfig.REGISTR_FIELD)
        registr_page.fill_password_field(RegistrationPageConfig.PASSWORD_FIELD)
        registr_page.click_submit_button()
