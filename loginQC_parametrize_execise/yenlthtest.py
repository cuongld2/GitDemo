from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

from models.objects.qc_object import LoginOBject
from utils_customs.constants_qc import SiteInfo, UserInfo
from models.locators.qc_locators import LoginLocators

from selenium.webdriver.support import expected_conditions as ec
import pytest


class TestLoginQC:
    login_object = LoginOBject()

    @pytest.mark.parametrize(('email_qc', 'pass_qc', 'expect_notify'), [
            ('','123','Bắt buộc phải nhập "Email"'),
            ('0612@yen.vn', '', 'Bắt buộc phải nhập "Mật khẩu"'),
            ('rewrwe', '123', 'Email bạn nhập không hợp lệ. Vui lòng thử lại (Ví dụ: abc@example.com).'),
            ('hrioew@gmail.com', '123', 'Email hoặc mật khẩu không đúng!'),
            ('0612@yen.vn', '123', 'Sai mật khẩu'),
            ('rewrwe', '', 'Email bạn nhập không hợp lệ. Vui lòng thử lại (Ví dụ: abc@example.com).\nBắt buộc phải nhập "Mật khẩu"'),
            ('', '', 'Bắt buộc phải nhập "Email"\nBắt buộc phải nhập "Mật khẩu"')
    ])
    def test_login_qc_parametrized(self, email_qc, pass_qc, expect_notify):
        driver = webdriver.Chrome()
        try:
            driver.get(SiteInfo.QC_URL)
            self.login_object.user_login_with_username_password(driver, email_qc, pass_qc)
            wait = WebDriverWait(driver, 120)
            wait.until(ec.visibility_of_element_located(LoginLocators.NOTIFY_LOCATOR))

            valueAttribute = driver.find_element_by_xpath(LoginLocators.NOTIFY_XPATH).text

            print(valueAttribute)

            assert valueAttribute == expect_notify
        finally:
            driver.quit()
