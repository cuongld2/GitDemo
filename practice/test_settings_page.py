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
        add_link_text = browser.find_element_by_class_name('js-addLink addButton headerButton').get
        #add_torrent_text = driver.find_element_by_xpath('//*[@id="root"]/div/header/div/button[2]').text
        #clear_all_text = driver.find_element_by_xpath('//*[@id="root"]/div/header/div/button[5]').text

        print(add_link_text)
        #print(add_torrent_text)
        #print(clear_all_text)
        #print(search_download_text)
        #assert ('Add link' in add_link_text)
        #assert ('Add torrent' in add_torrent_text)
        #assert ('Clear all' in clear_all_text)
