from selenium import webdriver

from utils_automation.const import Urls


class Browser:
    def browser_incognito(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--incognito")
        return webdriver.Chrome(options=chrome_options)

    def get_user_data_path(self):
        from models.pageobject.version import VersionPageObject
        version_page_object = VersionPageObject()
        local_driver = webdriver.Chrome()
        local_driver.maximize_window()
        local_driver.get(Urls.COCCOC_VERSION_URL)
        path_full = version_page_object.get_profile_path(local_driver)
        split_after = path_full.split('\\Local')
        return split_after[0]+u'\\Local\\CocCoc\\Browser\\User Data'
