import time

from selenium import webdriver

from models.objects.testrail_object import LoginOBject, HomePageObject, AddResultObject
from utils_customs.constants import SiteUrls, AuthenticationInfo
from pynput.keyboard import Key


class TestTestRail:
    login_object = LoginOBject()
    homepage_object = HomePageObject()
    add_result_object = AddResultObject()

    def test_login_testrail_success(self):
        driver = webdriver.Chrome()
        try:
            driver.get(SiteUrls.TESTRAIL_URL)
            self.login_object.user_login_with_username_password(driver, AuthenticationInfo.TESTRAIL_EMAIL,
                                                            AuthenticationInfo.TESTRAIL_PASSWORD)
            assert 'dashboard' in driver.current_url
        finally:
            driver.quit()

    def test_click_mobile_browser(self):
        driver = webdriver.Chrome()
        try:
            driver.get(SiteUrls.TESTRAIL_URL)
            self.login_object.user_login_with_username_password(driver, AuthenticationInfo.TESTRAIL_EMAIL,
                                                                AuthenticationInfo.TESTRAIL_PASSWORD)
            self.homepage_object.click_browser_mobile(driver)
        finally:
            driver.quit()

    def test_click_test_run(self):
        driver = webdriver.Chrome()
        try:
            driver.get(SiteUrls.TESTRAIL_URL)
            self.login_object.user_login_with_username_password(driver, AuthenticationInfo.TESTRAIL_EMAIL,
                                                                AuthenticationInfo.TESTRAIL_PASSWORD)
            self.homepage_object.click_browser_mobile(driver)
            self.homepage_object.click_test_run(driver)
        finally:
            driver.quit()

    def test_click_add_result(self):
        driver = webdriver.Chrome()
        try:
            driver.get(SiteUrls.TESTRAIL_URL)
            self.login_object.user_login_with_username_password(driver, AuthenticationInfo.TESTRAIL_EMAIL,
                                                                AuthenticationInfo.TESTRAIL_PASSWORD)
            self.homepage_object.click_browser_mobile(driver)
            self.homepage_object.click_test_run(driver)
            self.add_result_object.click_add_result(driver)
            self.keyboard.press(Key.enter)
        finally:
            driver.implicitly_wait(5)

