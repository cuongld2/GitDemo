from models.elements.basepage_elements import BasePageElement


class SettingsElements(BasePageElement):
    def find_spell_checker(self, driver):
        return self.find_shadow_element(driver, 'settings-ui', 'settings-main', 'settings-basic-page', 'settings-languages-page', 'settings-checkbox-toggle', 'cr-checkbox', '#ink')