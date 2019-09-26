from time import sleep

import pytest
from selenium import webdriver

from models.objects.testqc_object import LoginOBject
from utils_customs.constants import SiteUrls, AuthenticationInfo


class TestQC:
    login_object = LoginOBject()

    @pytest.mark.parametrize("email, password, message",
                             [('thu@cc.com', 'q', 'Email hoặc mật khẩu không đúng!'),
                              ('thu@cc.com', '', 'Bắt buộc phải nhập "Mật khẩu"'),
                              ('', 'q1', 'Bắt buộc phải nhập "Email"'),
                              ('', '', 'Bắt buộc phải nhập "Email" \n Bắt buộc phải nhập "Mật khẩu"')])
    def test_qc_parameterized(self, email, password, message):
        driver = webdriver.Chrome()
        try:

            driver.get(SiteUrls.TESTQC_URL)
            self.login_object.user_login_with_username_password(driver, email, password)
            sleep(5)
            a = driver.find_element_by_xpath('//*[@id="client-login"]/form/div[1]').text
            print(a)
            assert a == message
        finally:
            driver.quit()
