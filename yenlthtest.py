from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from models.objects.qc_object import LoginOBject
from utils_customs.constants_qc import SiteInfo, UserInfo
from models.locators.qc_locators import LoginLocators

from selenium.webdriver.support import expected_conditions as ec


class TestLoginQC:
    login_object = LoginOBject()

    def test_login_qc(self):
        driver = webdriver.Chrome()
        try:
            driver.get(SiteInfo.QC_URL)
            self.login_object.user_login_with_username_password(driver, UserInfo.QC_EMAIL, UserInfo.QC_PASS)

            #print(driver.current_url)
            #print(driver.get)
            #driver.implicitly_wait(10)
            #driver.find_element_by_xpath('//a[@class="hoverable"][contains(text(),"n d")]')
            wait = WebDriverWait(driver, 120)
            wait.until(ec.visibility_of_element_located(LoginLocators.HOMEPAGE_LOCATOR))

        finally:
            driver.quit()
