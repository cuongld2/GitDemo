import time

import pyautogui as pyautogui
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from models.elements.basepage_elements import BasePageElement


class SettingsElements(BasePageElement):
    def find_language(self, driver):
        return self.find_shadow_element(driver, 'settings-ui', 'settings-main', 'settings-basic-page', 'settings-appearance-page', 'settings-toggle-button', 'cr-toggle', '#bar')
    def find_spell_checker(self, driver):
        return self.find_shadow_element(driver, 'settings-ui', 'settings-main', 'settings-basic-page',
                                 'settings-languages-page', '#enableSpellcheckingToggle')
