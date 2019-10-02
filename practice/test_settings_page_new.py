import time

from selenium import webdriver

from models.objects.testrail_object import SpellCheckerObject
from utils_customs.constants import SettingsPageUrlsNew


class TestSettingsPageNew:
    spell_checker_object_new=SpellCheckerObject()

    def test_settings_page_new(self):
        driver= webdriver.Chrome()
        try:
            driver.get(SettingsPageUrlsNew.URL_SETTINGS_PAGE_NEW)
            time.sleep(2)
            self.spell_checker_object_new.click_spell_checker_new(driver)
        finally:
            time.sleep(3)