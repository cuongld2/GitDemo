import time

from selenium import webdriver


class TestSettingPageSpellChecker:

    def test_click_find_spell_checker(self):
        driver = webdriver.Chrome()
        driver.get('coccoc://settings/languages')
        time.sleep(7)
        driver.execute_script('document.querySelector("body > settings-ui").shadowRoot.querySelector('
                              '"#main").shadowRoot.querySelector("settings-basic-page").shadowRoot.querySelector('
                              '"#advancedPage > settings-section:nth-child(3) > '
                              'settings-languages-page").shadowRoot.querySelector('
                              '"#enableSpellcheckingToggle").shadowRoot.querySelector("#control").click()')
        driver.quit()



