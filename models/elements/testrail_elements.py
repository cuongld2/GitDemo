from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from models.locators.testrail_locators import LoginLocators, HomePageLocators


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


class HomePageElements:

    def find_browser_mobile(self, driver):
        wait = WebDriverWait(driver, 5)
        return wait.until(ec.presence_of_element_located(HomePageLocators.BROWSER_MOBILE_LOCATOR))

    def find_test_case_result(self, driver):
        wait = WebDriverWait(driver, 5)
        return wait.until(ec.presence_of_element_located(HomePageLocators.TEST_CASE_RESULT_LOCATOR))

