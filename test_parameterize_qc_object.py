from time import sleep

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from models.objects.testqc_object import LoginOBject
from utils_customs.constants import SiteUrls


class TestQC:
    login_object = LoginOBject()

    @pytest.mark.parametrize("email, password, message",
                             [('thu@cc.com', 'q', 'Email hoặc mật khẩu không đúng!'),
                              ('thu@cc.com', '', 'Bắt buộc phải nhập "Mật khẩu"'),
                              ('', 'q1', 'Bắt buộc phải nhập "Email"'),
                              ('', '', 'Bắt buộc phải nhập "Email"\nBắt buộc phải nhập "Mật khẩu"')])
    def test_qc_parameterized(self, browser, email, password, message):
        browser.get(SiteUrls.TESTQC_URL)
        self.login_object.user_login_with_username_password(browser, email, password)
        wait = WebDriverWait(browser, 5)
        error_message_element = wait.until(ec.presence_of_element_located((By.XPATH,
                                                                           ('//*[@id="client-login"]/form/div[1]['
                                                                            'string-length(text()) > 3]'))))
        a = error_message_element.text
        assert a == message

