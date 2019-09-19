from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from models.elements.basepage_elements import BasePageElement
from models.locators.test_cc_settings_locators import SpellCheckLocator


class SpellCheckElements(BasePageElement):

    def find_spell_check(self, driver):
        return self.find_shadow_element(driver, 'settings-ui', 'settings-main', 'settings-basic-page',
                                        'settings-languages-page', '#enableSpellcheckingToggle')
