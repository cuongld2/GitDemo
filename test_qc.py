from selenium import webdriver

from models.objects.testqc_object import LoginOBject
from utils_customs.constants import SiteUrls, AuthenticationInfo


class TestQC:
    login_object = LoginOBject()

    def test_login_testqc_success(self):
        driver = webdriver.Chrome()
        try:
            driver.get(SiteUrls.TESTQC_URL)
            self.login_object.user_login_with_username_password(driver, AuthenticationInfo.TESTQC_EMAIL,
                                                                AuthenticationInfo.TESTQC_PASSWORD)
            assert 'welcome' in driver.current_url
        finally:
            driver.quit()
