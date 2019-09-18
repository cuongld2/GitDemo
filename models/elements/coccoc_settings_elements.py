from models.elements.basepage_elements import BasePageElement


class CocCocSettingsElements(BasePageElement):

    def find_settings_toggle_button(self, driver):
        return self.find_shadow_element(driver, 'settings-ui', 'settings-main', 'settings-basic-page',
                                 'settings-languages-page', '#enableSpellcheckingToggle')



