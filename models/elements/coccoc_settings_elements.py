from models.elements.basepage_elements import BasePageElement


class SettingsElements(BasePageElement):
    def find_spell_checker(self, driver):
        return self.find_shadow_element(driver, 'body > settings-ui', '#main', 'settings-basic-page', '#basicPage > settings-section:nth-child(6) > settings-languages-page', '#pages > div > settings-checkbox-toggle', '#checkbox', '#checkbox')

    def find_spell_checker_new(self, driver):
        return self.find_shadow_element(driver, 'body > settings-ui', '#main', 'settings-basic-page', "#advancedPage > settings-section:nth-child(3) > settings-languages-page", "#enableSpellcheckingToggle", "#labelWrapper > div:nth-child(1)")