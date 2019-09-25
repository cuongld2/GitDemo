from models.elements.coccoc_settings_elements import CocCocSettingsElements


class SettingsPageObject:
    coccoc_settings_elements = CocCocSettingsElements()

    def choose_spell_checker(self, driver):
        element_outside = self.coccoc_settings_elements.find_settings_toggle_button(driver)
        driver.execute_script("arguments[0].click()", element_outside)


