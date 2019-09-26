import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from models.objects.qc_object import LoginObject
from utils_customs.constants import QcPageUrl


class TestParametrize:
    login_object = LoginObject()

    @pytest.mark.parametrize("email, password, message",
                             [("phamduongtest1@gmail.com", "", 'Bắt buộc phải nhập "Mật khẩu"'),
                             ("", "abc123", 'Bắt buộc phải nhập "Email"'),
                             ("phamduongtest1@gmail.com", "123", "Sai mật khẩu"),
                             ("phamduong@gmail.com", "123", "Email hoặc mật khẩu không đúng!"),
                             ("","", 'Bắt buộc phải nhập "Email"\nBắt buộc phải nhập "Mật khẩu"')])
    def test_qc_parametrize(self, email, password, message):
        driver = webdriver.Chrome()

        try:
            driver.get(QcPageUrl.URL_QC_PAGE)
            self.login_object.user_login_with_username_password(driver, email, password)
            wait = WebDriverWait(driver, 10)
            error_message_element = wait.until(ec.presence_of_element_located((By.XPATH, '//*[@id="client-login"]/form/div[1][string-length(text()) > 3]')))
            error_message_text = error_message_element.text
            print(error_message_text)
            print(message)
            assert error_message_text == message
        finally:
            driver.quit()
