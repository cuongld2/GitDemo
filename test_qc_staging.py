from selenium import webdriver

from models.objects.testqc_object import LoginOBject
from utils_customs.constants import SiteUrls, AuthenticationInfo


class TestStagingQC:
   login_object = LoginOBject()

   def test_login_stagingqc_success(self):
        driver = webdriver.Chrome()
        try:
            driver.get(SiteUrls.TESTQC_URL)
            self.login_object.user_login_with_username_password(driver, AuthenticationInfo.TESTQC_EMAIL,
                                                                AuthenticationInfo.TESTQC_PASSWORD)
            driver.implicitly_wait(10)
            driver.find_element_by_id('header-link-email')
        finally:
           driver.quit()