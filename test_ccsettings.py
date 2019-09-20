from selenium import webdriver

from models.elements.ccsettings_elements import SettingsElements
from models.objects.testrail_object import LoginOBject, HomePageObject, AddResultObject
from utils_customs.constants import SiteUrls, AuthenticationInfo
from pynput.keyboard import Key



class TestCCSettings:
    settings = SettingsElements()


    def test_click_show_home_button(self):
        driver = webdriver.Chrome()
        try:
            driver.get('coccoc://settings')
            element = self.settings.find_language(driver)
            element.click()
        finally:
            driver.quit()

    def test_click_spell_checker_button(self):
        driver = webdriver.Chrome()
        try:
            driver.get('coccoc://settings/languages')
            element = self.settings.find_spell_checker(driver)
            element.click()
        finally:
            driver.quit()


