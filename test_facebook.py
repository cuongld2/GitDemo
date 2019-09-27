from random import randint
from time import sleep

from selenium import webdriver

from models.objects.facebook_object import LoginOBject
from utils_customs.constants import AuthenticationInfo, SiteUrls


def random_sleep(min_s, max_s):
    sleep(randint(min_s, max_s))


class TestTestFacebook:
    login_object = LoginOBject()

    def test_login_testfacebook_success(self):
        driver = webdriver.Chrome()
        try:
            driver.get(SiteUrls.FACEBOOK_URL)
            self.login_object.user_login_with_username_password(driver, AuthenticationInfo.FACEBOOK_EMAIL,
                                                                AuthenticationInfo.FACEBOOK_PASSWORD)
            assert 'facebook' in driver.current_url
            random_sleep(1, 5)

        finally:
            driver.quit()
