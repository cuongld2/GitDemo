from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from models.locators.qc_locators import LoginLocators


class LoginPageElements:

    def find_email_field(self, driver):
        wait = WebDriverWait(driver, 5)
        return wait.until(ec.presence_of_element_located(LoginLocators.EMAIL_LOCATOR))

    def find_password_field(self, driver):
        wait = WebDriverWait(driver, 5)
        return wait.until(ec.presence_of_element_located(LoginLocators.PASSWORD_LOCATOR))


    def find_login_button(self, driver):
        wait = WebDriverWait(driver, 5)
        return wait.until(ec.presence_of_element_located(LoginLocators.LOGIN_BUTTON_LOCATOR))




