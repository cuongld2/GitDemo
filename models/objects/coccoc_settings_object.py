from models.elements.coccoc_settings_elements import CocCocSettingsElements


class SettingsPageObject:
    coccoc_settings_elements = CocCocSettingsElements()

    def choose_spell_checker(self, driver):
        self.coccoc_settings_elements.find_settings_toggle_button(driver).click()
