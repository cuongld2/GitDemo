from selenium import webdriver

from models.objects.coccoc_settings_object import SettingsPageObject


class TestSettingsCocCoc:

    settings_page_object = SettingsPageObject()

    def test_login_testrail_success(self):
        driver = webdriver.Chrome()
        try:
            driver.get('coccoc://settings/languages')
            self.settings_page_object.choose_spell_checker(driver)
        finally:
            driver.quit()

