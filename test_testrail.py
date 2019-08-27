import time

from selenium import webdriver

from models.objects.testrail_object import LoginOBject, HomePageObject
from utils_customs.constants import SiteUrls, AuthenticationInfo


class TestTestRail:
    login_object = LoginOBject()
    homepage_object = HomePageObject()

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

