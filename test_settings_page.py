from selenium import webdriver

from utils_customs.constants import SettingsPageUrls


class TestSettingsPage:

    def test_settings_page(self):
        driver = webdriver.Chrome()
        try:
            driver.get(SettingsPageUrls.URL_SETTINGS_PAGE)

        finally:
            driver.quit()