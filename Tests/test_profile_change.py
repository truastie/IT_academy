from config import ProfilePageConfig
from pages.profile_change_pet import ChangePet



class TestProfileChange:
    def test_change_pet(self,page, login):
        profile_page=ChangePet(page)
        profile_page.open_page(ProfilePageConfig.PROFILE_PAGE_URL)
        profile_page.click_edit_button()
        profile_page.clear_pet_name()
        profile_page.fill_pet_name_field('Mikki')
        profile_page.click_save_button()
