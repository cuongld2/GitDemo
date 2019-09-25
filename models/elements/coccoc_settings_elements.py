from models.elements.basepage_elements import BasePageElement


class CocCocSettingsElements(BasePageElement):

    def find_settings_toggle_button(self, driver):
        return self.find_shadow_element(driver, 'body > settings-ui', '#main', 'settings-basic-page',
                                 '#basicPage > settings-section:nth-child(6) > settings-languages-page',
                                        '#pages > div > settings-checkbox-toggle',
                                        '#checkbox')

    def find_settings_paper_ink_button(self, driver):
        return self.find_shadow_element(driver, 'body > settings-ui', '#main', 'settings-basic-page',
                                        '#basicPage > settings-section:nth-child(6) > settings-languages-page',
                                        '#pages > div > settings-checkbox-toggle',
                                        '#checkbox',
                                        '#ink')

    def find_paper_ripple(self, driver):
        return self.find_shadow_element(driver, 'settings-ui', 'settings-main', 'settings-basic-page',
                                        'settings-languages-page',
                                        'settings-checkbox-toggle',
                                        'cr-checkbox[id="checkbox"]',
                                        'paper-ripple[id="ink"]')



