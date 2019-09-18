from selenium import webdriver

from models.objects.spell_checker_object import ClickSpellCheck
from utils_customs.constants import SiteUrls, AuthenticationInfo


class TestCheckOnSpellChecker:

    click_spell = ClickSpellCheck()

    def test_turn_on_spellchecker_success(self):
        driver = webdriver.Chrome()
        try:
            driver.get(SiteUrls.TEST_CC_SETTINGS_PAGE_URL)
            assert 'languages' in driver.current_url
            self.click_spell.user_click_spell_checker(driver)
        finally:
            driver.quit()
