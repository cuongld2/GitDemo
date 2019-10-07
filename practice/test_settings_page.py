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

    def test_settings_download_page(self, browser):
        browser.get('coccoc://downloads/')
        time.sleep(2)
        add_link = browser.find_elements_by_xpath('//*[@title="Add link"]')
        assert len(add_link) == 1
        add_torrent = browser.find_elements_by_xpath('//*[@title="Add torrent"]')
        assert len(add_torrent) == 1
        clear_all = browser.find_elements_by_xpath('//*[@title="Clear all"]')
        assert len(clear_all) == 1
