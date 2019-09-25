import time

from selenium import webdriver

from models.objects.testrail_object import SpellCheckerObject


class TestSettingsPage:
    spell_checker_object = SpellCheckerObject()

    def test_settings_page(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        try:
            driver.get('coccoc://settings/languages')
            time.sleep(2)
            self.spell_checker_object.click_spell_checker(driver)
        finally:
            driver.quit()
