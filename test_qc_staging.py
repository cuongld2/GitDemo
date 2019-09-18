from selenium import webdriver

from models.elements.test_stagingqc_elements import LoginPageElements
from models.objects.testqc_object import LoginOBject
from utils_customs.constants import SiteUrls, AuthenticationInfo


class TestStagingQC:
    login_object = LoginOBject()
    login_elem = LoginPageElements()

    def test_login_stagingqc_success(self):
        driver = webdriver.Chrome()
        try:
            driver.get(SiteUrls.TESTQC_URL)
            self.login_object.user_login_with_username_password(driver, AuthenticationInfo.TESTQC_EMAIL,
                                                                AuthenticationInfo.TESTQC_PASSWORD)
            # driver.implicitly_wait(10)
            print(self.login_elem.find_header_button(driver))
            assert self.login_elem.find_header_button(driver) is not None
            # driver.find_element_by_id('header-link-email')
            print(driver.current_url)
            assert 'welcome' in driver.current_url
        finally:
            driver.quit()

    def test_turn_on_spellchecker_success(self):
        driver = webdriver.Chrome()
        try:
            driver.get(SiteUrls.TEST_CC_SETTINGS_PAGE_URL)
            assert 'languages' in driver.current_url
        finally:
            driver.quit()



