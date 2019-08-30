import pytest
from selenium import webdriver

from models.objects.facebook_object import StartPageObject
from utils_customs.constants import SiteUrls


class TestHandleElements:

    start_page_object = StartPageObject()

    @pytest.fixture(scope='module')
    def set_up_browser(self):
        driver = webdriver.Chrome()
        yield driver
        driver.quit()

    def test_handle_drop_down_list(self, set_up_browser):

        set_up_browser.get(SiteUrls.FACEBOOK_URL)
        self.start_page_object.choose_date_birthday(set_up_browser, 11)

    def test_handle_radio_button(self, set_up_browser):
        set_up_browser.get(SiteUrls.FACEBOOK_URL)
        self.start_page_object.choose_female_sex(set_up_browser)






