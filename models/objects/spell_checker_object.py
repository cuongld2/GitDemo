from models.elements.test_cc_setting_element import SpellCheckElements


class ClickSpellCheck:
    click_spell_check = SpellCheckElements()

    def user_click_spell_checker(self, driver):
        self.click_spell_check.find_spell_check(driver).click()