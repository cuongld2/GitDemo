import time
from selenium import webdriver
from models.objects.coccoc_settings_object import SettingsPageObject
from utils_customs.constants import CocCocSettingsUrls


class TestSettingsCocCoc:

    settings_page_object = SettingsPageObject()

    def test_login_testrail_success(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        try:
            driver.get(CocCocSettingsUrls.SETTINGS_LANGUAGES)
            time.sleep(2)
            self.settings_page_object.choose_spell_checker(driver)
        finally:
            driver.quit()

