import time
import unittest
from selenium import webdriver

from models.locators.coccoc_settings_locators import SettingsPageLocators
from models.objects.testrail_object import SpellCheckerObject
from utils_customs.constants import SettingsPageUrls


class TestSettingsPage:
    spell_checker_object = SpellCheckerObject()

    def test_settings_language_page(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        try:
            driver.get('coccoc://settings/languages')
            time.sleep(2)
            self.spell_checker_object.click_spell_checker(driver)
        finally:
            driver.quit()

    def test_settings_download_page(self):
        driver = webdriver.Chrome()
        try:
            driver.get(SettingsPageUrls.URL_DOWNLOAD_PAGE)
            time.sleep(2)
            assert ('Add link', SettingsPageLocators.ADD_LINK_BUTTON)
            assert ('Add torrent', SettingsPageLocators.ADD_TORRENT_BUTTON)
            assert ('Clear all', SettingsPageLocators.CLEAR_ALL_BUTTON)
        finally:
            driver.quit()