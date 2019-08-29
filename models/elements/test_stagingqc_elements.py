from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from models.locators.testqc_locators import LoginStagingLocator


class LoginPageElements:

    def find_email_field(self, driver):
        wait = WebDriverWait(driver, 5)
        return wait.until(ec.presence_of_element_located(LoginStagingLocator.EMAIL_LOCATOR))

    def find_password_field(self, driver):
        wait = WebDriverWait(driver, 5)
        return wait.until(ec.presence_of_element_located(LoginStagingLocator.PASSWORD_LOCATOR))

    def find_login_button(self, driver):
        wait = WebDriverWait(driver, 5)
        return wait.until(ec.presence_of_element_located(LoginStagingLocator.LOGIN_BUTTON_LOCATOR))
