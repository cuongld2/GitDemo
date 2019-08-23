import time

from selenium import webdriver

from models.objects.testrail_object import LoginOBject
from utils_customs.constants import SiteUrls, AuthenticationInfo


class TestTestRail:
    login_object = LoginOBject()

    def test_login_testrail_success(self):
        driver = webdriver.Chrome()
        try:
            driver.get(SiteUrls.TESTRAIL_URL)
            self.login_object.user_login_with_username_password(driver, AuthenticationInfo.TESTRAIL_EMAIL,
                                                            AuthenticationInfo.TESTRAIL_PASSWORD)
            assert 'dashboard' in driver.current_url
        finally:
            driver.quit()

