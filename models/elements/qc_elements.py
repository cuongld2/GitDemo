from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from models.locators.qc_locators import LoginPageLocators


class LoginPageElements:

    def find_email_field(self, driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(ec.presence_of_element_located(LoginPageLocators.EMAIL_FIELD))

    def find_password_field(self, driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(ec.presence_of_element_located(LoginPageLocators.PASSWORD_FIELD))

    def find_login_button(self, driver):
        wait = WebDriverWait(driver, 10)
        return wait.until(ec.presence_of_element_located(LoginPageLocators.LOGIN_BUTTON))

        return wait.until(ec.invisibility_of_element_located())