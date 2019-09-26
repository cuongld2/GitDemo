from models.elements.coccoc_settings_elements import SettingsElements
from models.elements.testrail_elements import LoginPageElements, HomePageElements, AddResultElements


class LoginOBject:
    login_page_element = LoginPageElements()

    def user_login_with_username_password(self, driver, email, password):
        email_field = self.login_page_element.find_email_field(driver)
        email_field.click()
        email_field.send_keys(email)

        password_field = self.login_page_element.find_password_field(driver)
        password_field.click()
        password_field.send_keys(password)

        login_button = self.login_page_element.find_login_button(driver)
        login_button.click()


class HomePageObject:
    home_page_element = HomePageElements()

    def click_browser_mobile(self, driver):
        self.home_page_element.find_browser_mobile(driver).click()

    def click_test_run(self, driver):
        self.home_page_element.find_test_run(driver).click()


class AddResultObject:
    add_result_element = AddResultElements()

    def click_add_result(self, driver):
        self.add_result_element.find_add_result_btn(driver).click()

    def click_add_result_sm(self, driver):
        self.add_result_element.find_add_result_sm_btn(driver).click()


class SpellCheckerObject:
    find_shadow_element = SettingsElements()

    def click_spell_checker(self, driver):
        self.find_shadow_element.find_spell_checker(driver).click()

    def click_spell_checker_new(self, driver):
        self.find_shadow_element.find_spell_checker_new(driver).click()
